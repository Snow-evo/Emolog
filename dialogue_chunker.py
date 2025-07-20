#!/usr/bin/env python3
"""
Dialogue Chunker for Emolog
Memory-efficient chunking of large dialogue log JSON files into manageable pieces

Usage:
    python dialogue_chunker.py <input_json_file> [--chunk-size <characters>] [--output-dir <directory>]
    
Example:
    python dialogue_chunker.py dialogue_logs/sample01.json --chunk-size 10000 --output-dir chunks/
"""

import json
import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional
# import ijson  # For streaming JSON processing (use when handling very large files)


class DialogueChunker:
    def __init__(self, chunk_size: int = 25000, output_dir: str = "chunks"):
        """
        Args:
            chunk_size: Target character count for each chunk (default: 25,000 characters)
            output_dir: Output directory for chunk files
        """
        self.chunk_size = chunk_size
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.current_subdir = None  # Subdirectory for current file
        
    def estimate_entry_size(self, entry: Dict[str, Any]) -> int:
        """Estimate approximate character count of a dialogue entry"""
        return len(json.dumps(entry, ensure_ascii=False))
    
    def clear_output_dir(self):
        """Clear existing chunk files in current subdirectory"""
        if self.current_subdir and self.current_subdir.exists():
            for file in self.current_subdir.glob("chunk_*.json"):
                file.unlink()
            
    def chunk_dialogue_file(self, input_file: str) -> Dict[str, Any]:
        """
        Split dialogue log file into chunks
        
        Args:
            input_file: Input JSON file path
            
        Returns:
            Chunking statistics
        """
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")
            
        # Create subdirectory from input filename
        base_name = input_path.stem  # Filename without extension
        self.current_subdir = self.output_dir / base_name
        self.current_subdir.mkdir(exist_ok=True)
        
        self.clear_output_dir()
            
        chunk_count = 0
        current_chunk = []
        current_size = 0
        total_entries = 0
        total_characters = 0
        
        try:
            # Try normal JSON loading (for smaller files)
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            if not isinstance(data, list):
                raise ValueError("JSON file must contain a list of dialogue entries")
                
            for entry in data:
                entry_size = self.estimate_entry_size(entry)
                total_characters += entry_size
                
                # Start new chunk if current chunk exceeds size limit
                if current_size + entry_size > self.chunk_size and current_chunk:
                    chunk_count += 1
                    self._save_chunk(current_chunk, chunk_count)
                    current_chunk = []
                    current_size = 0
                    
                current_chunk.append(entry)
                current_size += entry_size
                total_entries += 1
                
            # Save the last chunk
            if current_chunk:
                chunk_count += 1
                self._save_chunk(current_chunk, chunk_count)
                
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            sys.exit(1)
        except MemoryError:
            # Fallback to streaming processing on memory error
            print("File too large for memory, using streaming approach...")
            return self._chunk_dialogue_streaming(input_file)
            
        stats = {
            "input_file": str(input_path),
            "total_entries": total_entries,
            "total_characters": total_characters,
            "chunk_count": chunk_count,
            "average_chunk_size": total_characters / chunk_count if chunk_count > 0 else 0,
            "output_directory": str(self.current_subdir)
        }
        
        # Save statistics
        with open(self.current_subdir / "chunking_stats.json", 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
            
        return stats
    
    def _chunk_dialogue_streaming(self, input_file: str) -> Dict[str, Any]:
        """Streaming processing for large files"""
        # Streaming implementation using ijson
        # (implement when large file support is needed)
        raise NotImplementedError("Streaming processing not yet implemented")
        
    def _save_chunk(self, chunk_data: List[Dict[str, Any]], chunk_number: int):
        """Save chunk to file"""
        chunk_file = self.current_subdir / f"chunk_{chunk_number:03d}.json"
        
        # Add chunk metadata
        chunk_with_metadata = {
            "chunk_metadata": {
                "chunk_number": chunk_number,
                "entry_count": len(chunk_data),
                "session_id": f"E{chunk_number}"
            },
            "entries": chunk_data
        }
        
        with open(chunk_file, 'w', encoding='utf-8') as f:
            json.dump(chunk_with_metadata, f, ensure_ascii=False, indent=2)
            
        print(f"Saved chunk {chunk_number}: {len(chunk_data)} entries")


def main():
    parser = argparse.ArgumentParser(
        description="Split large dialogue JSON files into manageable chunks"
    )
    parser.add_argument(
        "input_file",
        help="Path to input JSON file containing dialogue logs"
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=25000,
        help="Target size for each chunk in characters (default: 25000)"
    )
    parser.add_argument(
        "--output-dir",
        default="chunks",
        help="Output directory for chunk files (default: chunks)"
    )
    
    args = parser.parse_args()
    
    # Initialize and run chunker
    chunker = DialogueChunker(
        chunk_size=args.chunk_size,
        output_dir=args.output_dir
    )
    
    print(f"Chunking {args.input_file} into ~{args.chunk_size} character chunks...")
    
    try:
        stats = chunker.chunk_dialogue_file(args.input_file)
        
        print("\nChunking completed successfully!")
        print(f"Total entries: {stats['total_entries']:,}")
        print(f"Total characters: {stats['total_characters']:,}")
        print(f"Number of chunks: {stats['chunk_count']}")
        print(f"Average chunk size: {stats['average_chunk_size']:,.0f} characters")
        print(f"Output directory: {stats['output_directory']}")
        
    except Exception as e:
        print(f"Error during chunking: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
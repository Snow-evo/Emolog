#!/usr/bin/env python3
"""
Dialogue Chunker for Emolog
大規模な対話ログJSONファイルをメモリ効率的にチャンクに分割する

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
# import ijson  # ストリーミングJSON処理用（大規模ファイル対応時に使用）


class DialogueChunker:
    def __init__(self, chunk_size: int = 30000, output_dir: str = "chunks"):
        """
        Args:
            chunk_size: 各チャンクの目標文字数（デフォルト: 30,000文字）
            output_dir: チャンクの出力ディレクトリ
        """
        self.chunk_size = chunk_size
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.current_subdir = None  # 現在のファイル用のサブディレクトリ
        
    def estimate_entry_size(self, entry: Dict[str, Any]) -> int:
        """対話エントリーのおおよその文字数を推定"""
        return len(json.dumps(entry, ensure_ascii=False))
    
    def clear_output_dir(self):
        """現在のサブディレクトリの既存チャンクファイルをクリア"""
        if self.current_subdir and self.current_subdir.exists():
            for file in self.current_subdir.glob("chunk_*.json"):
                file.unlink()
            
    def chunk_dialogue_file(self, input_file: str) -> Dict[str, Any]:
        """
        対話ログファイルをチャンクに分割
        
        Args:
            input_file: 入力JSONファイルパス
            
        Returns:
            分割統計情報
        """
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")
            
        # 入力ファイル名からサブディレクトリを作成
        base_name = input_path.stem  # 拡張子を除いたファイル名
        self.current_subdir = self.output_dir / base_name
        self.current_subdir.mkdir(exist_ok=True)
        
        self.clear_output_dir()
            
        chunk_count = 0
        current_chunk = []
        current_size = 0
        total_entries = 0
        total_characters = 0
        
        try:
            # 通常のJSONロードを試みる（小さいファイルの場合）
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            if not isinstance(data, list):
                raise ValueError("JSON file must contain a list of dialogue entries")
                
            for entry in data:
                entry_size = self.estimate_entry_size(entry)
                total_characters += entry_size
                
                # 現在のチャンクがサイズ制限を超える場合、新しいチャンクを開始
                if current_size + entry_size > self.chunk_size and current_chunk:
                    chunk_count += 1
                    self._save_chunk(current_chunk, chunk_count)
                    current_chunk = []
                    current_size = 0
                    
                current_chunk.append(entry)
                current_size += entry_size
                total_entries += 1
                
            # 最後のチャンクを保存
            if current_chunk:
                chunk_count += 1
                self._save_chunk(current_chunk, chunk_count)
                
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            sys.exit(1)
        except MemoryError:
            # メモリエラーの場合はストリーミング処理にフォールバック
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
        
        # 統計情報を保存
        with open(self.current_subdir / "chunking_stats.json", 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
            
        return stats
    
    def _chunk_dialogue_streaming(self, input_file: str) -> Dict[str, Any]:
        """大規模ファイル用のストリーミング処理"""
        # ijsonを使用したストリーミング実装
        # （大規模ファイル対応が必要な場合に実装）
        raise NotImplementedError("Streaming processing not yet implemented")
        
    def _save_chunk(self, chunk_data: List[Dict[str, Any]], chunk_number: int):
        """チャンクをファイルに保存"""
        chunk_file = self.current_subdir / f"chunk_{chunk_number:03d}.json"
        
        # チャンクメタデータを追加
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
        default=30000,
        help="Target size for each chunk in characters (default: 30000)"
    )
    parser.add_argument(
        "--output-dir",
        default="chunks",
        help="Output directory for chunk files (default: chunks)"
    )
    
    args = parser.parse_args()
    
    # チャンカーを初期化して実行
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
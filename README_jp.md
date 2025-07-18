# Emolog（エモログ）

**AIのための超コンパクトな対話圧縮記法**  
対話ログを約80％以上圧縮しながら、感情の深みと文脈を保持します。  
※ 圧縮率は cl100k_base など最新 tokenizer を用いた場合の実測値です

## 🎯 何を解決するの？

長期間の対話ログをAIに渡したいけど、トークン制限で入らない、要約だと薄くなる...そんな問題を解決します。

## ✨ Emologの特徴

- **📦 約80〜90%の圧縮率**  
  5万文字の対話 → 5千文字のEmologに圧縮
  
- **💝 感情・関係性を完全保持**  
  AIの語り口、ユーザーの心境変化、感情変化、登場人物の関係性まで再現可能
  
- **⚡ 検索レス高速応答**  
  圧縮ログを常時プロンプトに含められるため、RAG検索不要
  
- **🤖 AI直接解釈**  
  テキスト展開なしでAIが直接読み取り可能。中間変換プロセス不要
  
- **🔗 詳細ログとの連携**  
  出来事ID（例: `(id=E1-03)`）で元ログの特定箇所を即座に参照
  
- **🧩 拡張しやすい設計**  
  プロジェクト固有の専門用語や内輪ネタも追加可能

## 🏗️ Emologの構成要素

Emologは**「エンティティマップ＋10要素」**で対話を構造化します：

| 要素 | 説明 | 例 | 動的拡張 |
|------|------|-----|---------|
| 0. エンティティマップ | 登場人物の定義 | `👤=USER`, `🧠=AI` | セッション毎に新キャラ追加可 |
| 1. 時系列マーカー | 時間構造 | `⏪=過去回想`, `🔄=ループ` | プロジェクト応じて追加可 |
| 2. 意図マーカー | 行為の意図 | `🤔=迷い`, `🪄=再構成` | 文脈に応じて拡張可 |
| 3. 行為種別 | アクションタイプ | `💬=発言`, `💭=思考` | 対話形式に応じて追加可 |
| 4. ナラティブ視点 | 語り手の視点 | `🗣️=AI語り`, `👁️=主観` | 語り方に応じて拡張可 |
| 5. 関係性・場所・記憶 | 文脈情報 | `🔥=対立`, `🏠=家庭` | 場面に応じて動的追加 |
| 6. キー概念 | 重要語句（自動抽出） | `"重要語"` | 2回以上出現語を自動タグ化 |
| 7. 数値・評価 | 強度や評価 | `(85%)`, `(3x)`, `(★★★☆☆)` | 単位・意味は文脈で決定 |
| 8. 語り口検出システム | 話し方の特徴を自動検出 | `🌸🌊🤲=優しいカウンセラー` | 対話から語彙・語調を分析 |
| 9. 出来事ID | ログとの紐付け | `(id=E1-05)` | セッション・ユニット毎に自動付番 |
| 10. 絵文字ストーリー | 圧縮構文 | `👤💬 → 🧠🌸🌊🤲🪄 → 👤😊` | エモさ最優先で10%圧縮目標 |

### 🎭 語り口検出システムの詳細

語り口は対話ログから**自動検出**され、3つの絵文字で表現されます：

**検出要素**：
- 語彙選択（専門用語 vs 日常語 vs 俗語）
- 比喩・メタファーの使用頻度と種類  
- 感情表現の強度と表出方法
- 文の長さ・複雑さ・リズム
- ユーモア・皮肉・ジョークの有無と質
- 敬語・タメ口・方言などの言語レベル
- 共感的 vs 分析的 vs 批判的な反応パターン

**語り口例**：
- `🌸🌊🤲` = 優しいカウンセラー  
- `👔⚡➡️` = 厳格な教師
- `👕🌸🎪` = カジュアルな友人
- `⚖️🎓🧩` = 分析的な専門家
- `🎨🔥🎭` = ドラマチックな語り手


## 🚀 活用シーン（将来）
- **インデックスとして使用**： 長文対話のインデックスや全体文脈の深い把握に使用
- **長期プロジェクトの文脈継続**: 数ヶ月の議論履歴を新しいAIに即座に共有
- **カスタマーサポート**: 過去のやり取りを踏まえた対応
- **創作・ブレスト**: アイデアの発展過程を圧縮保存して継続発展
- **学習・コーチング**: 長期間の成長記録を効率的に管理

## 📂 ファイル構成

```
Emolog/
├── Emolog_define.py    # 11要素の定義ファイル：英語版
├── Emolog_define_jp.py    # 11要素の定義ファイル：日本語版
├── dialogue_chunker.py    # チャンク分割スクリプト
├── dialogue_logs/         # 元の対話ログ（JSON形式）を入れるフォルダ
├── chunks/                # チャンク化された出力ファイルが入るフォルダ
├── README_jp.md        # このファイル
└── README.md           # READMEファイル英語版
```

※ `dialogue_logs/` 配下の実際の会話ログ（.json）や `chunks/` 配下のチャンク出力は `.gitignore` によりGit管理から除外されています。サンプルやテンプレートのみリポジトリに含めてください。

## 🔧 チャンク分割スクリプトの使い方

### 1. 対話ログの準備

- `dialogue_logs/` フォルダに、**リスト形式のJSONファイル**（例: `sample01.json`）を用意します。

```json
[
  {
    "text": "こんにちは！",
    "metadata": {
      "role": "user",
      "date": "2025-05-15",
      "id": "xxxx-xxxx-xxxx"
    }
  },
  {
    "text": "こんにちは、どうされましたか？",
    "metadata": {
      "role": "assistant",
      "date": "2025-05-15",
      "id": "yyyy-yyyy-yyyy"
    }
  }
  // ...
]
```

※ 入力ファイルは「リスト形式（配列）」のJSONであれば、各エントリの中身の構造（フィールド名や内容）は自由に扱えます。
ただし、後続処理や他ツールとの連携のため、プロジェクト全体で統一した形式を使うことを推奨します。
※ 入力ファイルはJSON形式（拡張子は任意）である必要があります。他形式（CSV, YAML, Pythonリストなど）はそのままでは使えません。

### 2. チャンク化スクリプトの実行

ターミナルで以下のコマンドを実行します：

```bash
python dialogue_chunker.py dialogue_logs/sample01.json --chunk-size 10000 --output-dir chunks/
```

- `--chunk-size`：1チャンクあたりの最大文字数（省略時は30000）
- `--output-dir`：出力先ディレクトリ（省略時はchunks/）

### 3. 出力

- `chunks/sample01/` フォルダに `chunk_001.json`, `chunk_002.json` ... のように分割保存されます。
- 各チャンクにはメタデータ（エントリー数、チャンク番号など）も含まれます。


## ❓ よくある疑問

### Q1: 絵文字でなぜ感情の深みと文脈を保持できるの？

**A**: Emologは単なる絵文字変換ではありません。11要素の構造化された記法です：

- **構造化された意味**: `👤💬` = 「ユーザーの発言」、`🧠🪄` = 「AIの再構成」などを定義
- **関係性の表現**: `→` で因果関係、`🔄` でループパターン、`(85%)` で感情強度を表現
- **文脈の階層化**: エンティティマップ + 語り口検出 + 出来事IDで多層的に文脈を保存
- **AI直接解釈**: テキスト展開せずにAIが絵文字ストーリーを直接理解・推論可能
- **展開可能性**: 必要時にデコーダーで元の語調・文体を詳細再現、視点・フォーカスを変えての再構築

つまり「AIが直接読める感情豊かな構造化データ」として設計されています。

### Q2: 絵文字は3-4トークン使うから圧縮効果ないのでは？

### トークン効率（最新 / 旧 tokenizer）

**A**: トークン効率も考慮済みです：

**文字数ベースの圧縮効果**:
```
元テキスト: 
ユーザー"やっほ〜。ちょっとさー、プロジェクトがうまく進まなくて、困ってるんだよね〜。こっちの意図が相手に正確に伝わらなくて。"
AI"こんにちは！プロジェクトでコミュニケーションの問題があるんですね。まず現在のプロジェクトの状況を確認させてください。"
ユーザー"待って、まだ実行しないで。まだ計画を立てたいだけなんだ。" 
AI"なるほど！まず計画を立てたいんですね。
  Emologプロジェクトを見せていただきました。AIのための対話ログ圧縮言語の開発プロジェクトですね。
  「こっちの意図が相手に正確に伝わらなくて」という問題について、どのような計画を立てたいでしょうか？
  - プロジェクトの技術的な説明をより分かりやすくする方法？
  - ユーザーへの価値提案の伝え方？
  - それとも別の側面での計画？
  具体的にどの部分でのコミュニケーション改善を考えていますか？"
(378文字)

Emolog: "👤😰💬"プロジェクト"🔥 → 🧠🌸🌊🤲💬"計画"🤔 → 👤🙏💬"待って" → 🧠🪄📊"提案"💡" (40文字)
圧縮後サイズ: 11% (89%削減)
```

**追加圧縮例**（Emolog_define.pyより）:
```
👤😶‍🌫️⏪ → 🧠📦📖"ログ確認" 🎯       # 混乱→AI記憶確認→目標設定
👤📦📦😿 🔄 → 🧠🪄📂"解決策"          # 記憶蓄積→悲しみループ→AI再構成
🧠🔄📦"過去ログ" → 👤⏳🌱"成長"         # AI記憶回想→USER時間経過で成長
👤😿(75%) 🔄🌑 → 🧠🪄📂"サポート" 🌅    # 悲しみ75%→暗闇→AIサポート→夜明け
👤😭(80%) → 😊(40%) → 🧠🪞🌱"回復"    # 大泣き→微笑み→AI内省で回復確認
```

**トークン効率の実測**:
```
【最新 tokenizer (cl100k_base など)】
  元テキスト : 約378〜400 token  
  Emolog     : 約40〜60 token  (絵文字: 1文字≈1–2 token)  
  圧縮後サイズ: 10〜15 % (85〜90 %削減)

【旧 tokenizer (p50k 系, 2022 以前)】
  元テキスト : 約378〜756 token  
  Emolog     : 約120〜160 token (絵文字: 1文字≈3–4 token)  
  圧縮後サイズ: 16〜42 % (58〜84 %削減)

※ ほとんどの OpenAI 最新モデルでは「単一コードポイント絵文字＝1 token」で計算されます。  
  スキントーンバリエーションや ZWJ 合成絵文字は 2 token 程度になることがあります。
```

### Q3: 辞書や構文定義（デコーダー）が必要なら結局トークン増えるのでは？

**A**: その通りです。デコーダーのオーバーヘッドは存在します：

**短期セッションでの現実**:
- **３万文字未満**: Emolog使用は非推奨,デコーダーや辞書の固定コストが相対的に大きくなるため
- **10万文字以上**: 例) 原文 ~90,000 token → Emolog ~10,000 token (約 89 %削減)
- **30万文字以上**: 例) 原文 ~270,000 token → Emolog ~30,000 token (約 89 %削減)

つまりEmologは**長期間・大規模な対話セッション**に特化した技術です。短い会話には従来の方法が適しています。

## 🛠️ 今後の開発予定

- [ ] **圧縮効率の実測・検証**: 様々な長さ・種類の対話での圧縮率とトークン効率の測定
- [ ] **自動生成スクリプト**: 対話ログ → Emolog変換
- [ ] **デコーダー自動生成**: セッション固有の語り口・エンティティ検出
- [ ] **英語対応**: 英語での検証
- [ ] **Web UI**: ブラウザ、フロントエンドでの辞書読み込み・エモログ活用
- [ ] **MCP サーバー**: MCPサーバーでの辞書読み込み・エモログ活用

## 📄 ライセンス

MIT License

## 🤝 コントリビューション

Issues・PRお待ちしています！
特に以下の分野でのご協力を歓迎：
- 他言語での検証
- 実用事例の共有
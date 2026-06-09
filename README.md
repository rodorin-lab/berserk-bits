# ⚔️ Berserk B.I.T.S — サイバーパンク・バトルエンジン

![Status](https://img.shields.io/badge/status-%E9%96%8B%E7%99%BA%E4%B8%AD-yellow) ![Engine](https://img.shields.io/badge/engine-HTML5%20Canvas-blue)

**ピクセルアート × サイバーパンク** のデスクトップ常駐型バトルゲームだよ！

## 🎮 ゲーム内容

- 🦠 **ウイルスバトルシステム** — 多種多様なウイルスと戦闘！
- ⚡ **ターン制バトル** — 戦略的なコマンドバトル
- 🎨 **ピクセルアートスプライト** — 全ウイルスに個別スプライト
- 📊 **ステータスシステム** — HP / EXP / コイン
- 🤖 **AI敵** — 移動パターン・攻撃パターン搭載

## 📂 データ構造

```
game/battle_data/virus/
├── _template/    # ウイルステンプレート
├── DBOO/         # ボスウイルス
├── FROG/         # 召喚型
├── ELE/          # 電気属性
├── CAN/          # 砲台型
├── TURRB/        # タレット
├── LBOSS/        # 大ボス
└── SMINI1/       # ミニボス
```

各ウイルスに `config.json`（ステータス） + `summon.json`（召喚） + スプライトPNG

## 🚀 起動方法

```bash
cd Berserk.B.I.T.S/game
# ブラウザでdisplay_measure.htmlを開く
```

## 🛠 技術

- HTML5 Canvas (2D)
- 純粋なJSON駆動データ設計
- ピクセルアートスプライト

## 📝 作者

- **ロドリン** & **シンクロ（グラム）** 💎🛸
- rodorin-lab © 2026

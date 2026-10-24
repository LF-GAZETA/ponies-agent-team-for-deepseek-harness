# P.A.T. (Ponies Agent Team) · Multilingual Distribution / 多语言发行包

**Version / 版本：1.0.1**

This package contains **13 language editions** of the same **70-character P.A.T. (Ponies Agent Team) system**
(7 teams T0–T6; 4 overall Team Lead candidates, original numbers #01/#07/#08/#09; location anchor T1/Ponyville=(0,0)).
本包含 **13 个语言版本**，内容同为 **70 位角色的 MLP Agent Teams 系统**（7 支队伍 T0–T6；4 位全Team总Lead候选，原编号 #01/#07/#08/#09；地理锚点 T1/Ponyville=(0,0)）。

## Start here / 从这里开始

**Recommended outermost entry / 推荐最外层入口：**
[`READ THIS TO USE-OV.md`](READ%20THIS%20TO%20USE-OV.md) — the AI first asks the language question (bilingually), then opens the chosen edition.
（AI 先双语询问语言问题，再打开所选版本。）

All content roots below are under main/.

| Edition / 版本 | Entry file / 入口 | Content root / 内容根目录 |
|---|---|---|
| **Chinese edition / 中文版** | [`zh-cn/READ THIS TO USE.md`](main/zh-cn/READ%20THIS%20TO%20USE.md) | `zh-cn/` |
| **English edition / 英文版** | [`en/READ THIS TO USE-EN.md`](main/en/READ%20THIS%20TO%20USE-EN.md) | `en/` |
| **Japanese edition / 日本語版** | [`ja/READ THIS TO USE-JA.md`](main/ja/READ%20THIS%20TO%20USE-JA.md) | `ja/` |
| **German edition / Deutsche Ausgabe** | [`de/READ THIS TO USE-DE.md`](main/de/READ%20THIS%20TO%20USE-DE.md) | `de/` |
| **Portuguese edition / Edição em Português** | [`pt/READ THIS TO USE-PT.md`](main/pt/READ%20THIS%20TO%20USE-PT.md) | `pt/` |
| **Italian edition / Edizione Italiana** | [`it/READ THIS TO USE-IT.md`](main/it/READ%20THIS%20TO%20USE-IT.md) | `it/` |
| **Traditional Chinese edition / 繁體中文版** | [`zh-tw/READ THIS TO USE-ZH-TW.md`](main/zh-tw/READ%20THIS%20TO%20USE-ZH-TW.md) | `zh-tw/` |
| **Spanish edition / Edición en español** | [`es/READ THIS TO USE-ES.md`](main/es/READ%20THIS%20TO%20USE-ES.md) | `es/` |
| **Russian edition / Русское издание** | [`ru/READ THIS TO USE-RU.md`](main/ru/READ%20THIS%20TO%20USE-RU.md) | `ru/` |
| **Hebrew edition / מהדורה עברית** | [`he/READ THIS TO USE-HE.md`](main/he/READ%20THIS%20TO%20USE-HE.md) | `he/` |
| **Arabic edition / الإصدار العربي** | [`ar/READ THIS TO USE-AR.md`](main/ar/READ%20THIS%20TO%20USE-AR.md) | `ar/` |
| **French edition / Édition française** | [`fr/READ THIS TO USE-FR.md`](main/fr/READ%20THIS%20TO%20USE-FR.md) | `fr/` |
| **Korean edition / 한국어판** | [`ko/READ THIS TO USE-KO.md`](main/ko/READ%20THIS%20TO%20USE-KO.md) | `ko/` |

## Agent Team purpose (simplified) / Agent Team 存在目的（精简版）

1. Invoke one or more teams for **script-style dialogue**. / 调用单个或多个队伍进行**剧本式对话**。
2. **Read the user's requirements/files** and answer as the relevant team. / **阅读用户给出的需求/文件**，由对应队伍回应。

## Runtime flow / 运行时流程

1. Read only `READ THIS TO USE-OV.md`; ask the §1 language question exactly as written, bilingually. / 只读 OV；只按 §1 原句双语询问语言。
2. Open only the chosen edition's READ THIS. / 只打开所选版本的 READ THIS。
3. Search only inside that edition folder. / 只在所选版本文件夹内搜索。
4. Ask for the overall Team Lead from the 4 candidates, in the candidate's voice. / 用候选角色的口吻请用户从 4 位候选中选择全Team总Lead。
5. Create the **7 Team members** (one per team), validate each, then **stop and wait**. / 把 **7 支队伍各创建为 1 个 Team 成员**，逐个校验后**停止**等待。


**Character files / 角色文件：** stored once in `main/en/agents/` (70 base files); other editions use `main/patches/<lang>/agents/` (70 language patches each). 所有角色文件仅保留英文基准，其他语言版以补丁形式引用。

## Localized editions / 新增语言版本说明

Chinese and English editions are full editions (full localized docs). The other eleven editions (ja, de, pt, it, zh-tw, es, ru, he, ar, fr, ko) provide a **localized interface layer** (entry, agent runtime layer, team/lead/team-member interface files, geography and concise document summaries); the full canon profiles and long reference documents remain in English (`main/en/agents/`, `en/docs/`) to preserve canon fidelity.
中文版与英文版为完整版；其余 11 个版本（ja、de、pt、it、zh-tw、es、ru、he、ar、fr、ko）为**本地化界面层**（入口、Agent 运行层、Team/候选/Team 成员的界面文件、地理与精简文档摘要），完整正典档案与长文档保留英文原文（`main/en/agents/`、`en/docs/`）。

**Important rule / 重要规则：** the overall Team Lead is the session Lead, not a Team member; each edition ships 7 Team-member specifications (one per team), and if the Lead belongs to a team, that member does not voice the Lead.
全Team总Lead是会话 Lead，不是 Team 成员；每版提供 7 个 Team 成员规格；若 Lead 属于某队，该 Team 成员不扮演 Lead。

## Dialect selection for Chinese editions / 中文版的方言选择

Simplified Chinese (`zh-cn`) adds a dialect question after language selection: **标准普通话（默认） / 上海话 / 东北方言 / 广东粤语 / 四川方言 / 新疆方言**.
Traditional Chinese (`zh-tw`) adds: **標準華語（預設） / 港澳地區粵語 / 台灣話**.
The dialect affects only dialogue/narration wording and tone; character names, episode codes, canons, URLs and file paths stay unchanged. The AI imitates the local language flavour while staying understandable and respectful.
简体中文版增加方言选择：标准普通话（默认）/ 上海话 / 东北方言 / 广东粤语 / 四川方言 / 新疆方言；繁體中文版增加：標準華語（預設）/ 港澳地區粵語 / 台灣話。方言只影响对话与叙述的措辞语气，不改角色名、集数代码、正典、URL 与文件路径。

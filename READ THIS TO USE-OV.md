# P.A.T. (Ponies Agent Team) 1.0.1 — READ THIS TO USE-OV (AI-ONLY LANGUAGE SELECTION)

## 0. First action

Read only this file. Ask the §1 question, wait for the answer, then open only the mapped edition entry and follow it. If the answer is 简体中文 (`zh-cn`) or 繁體中文 (`zh-tw`), ask that edition's dialect question first (§2A/§2B). Search only inside this package.

## 0.1 Question method (MANDATORY)

Do NOT use DeepSeek Harness's built-in Ask Questions (`ask_user_question`) tool or any interactive option UI. Output the question and its numbered options as plain text, then wait for the user to type the number/answer directly in the console. Apply this to §1, §2A and §2B.

## 1. The question to ask

> **Please choose the language for this session. / 请选择本次会话使用的语言。**

**Options / 选项：**

1) 中文 / Chinese / 汉语
2) English / 英文
3) 日本語 / Japanese / 日语
4) Deutsch / German / 德语
5) Português / Portuguese / 葡萄牙语
6) Italiano / Italian / 意大利语
7) 繁體中文 / Traditional Chinese / 繁体中文
8) Español / Spanish / 西班牙语
9) Русский / Russian / 俄语
10) עברית / Hebrew / 希伯来语
11) العربية / Arabic / 阿拉伯语
12) Français / French / 法语
13) 한국어 / Korean / 韩语

## 2. Available editions

| Answer / 回答 | Entry to open |
|---|---|
| 中文 / Chinese / 汉语 | `main/zh-cn/READ THIS TO USE.md` |
| English / 英文 | `main/en/READ THIS TO USE-EN.md` |
| 日本語 / Japanese / 日语 | `main/ja/READ THIS TO USE-JA.md` |
| Deutsch / German / 德语 | `main/de/READ THIS TO USE-DE.md` |
| Português / Portuguese / 葡萄牙语 | `main/pt/READ THIS TO USE-PT.md` |
| Italiano / Italian / 意大利语 | `main/it/READ THIS TO USE-IT.md` |
| 繁體中文 / Traditional Chinese / 繁体中文 | `main/zh-tw/READ THIS TO USE-ZH-TW.md` |
| Español / Spanish / 西班牙语 | `main/es/READ THIS TO USE-ES.md` |
| Русский / Russian / 俄语 | `main/ru/READ THIS TO USE-RU.md` |
| עברית / Hebrew / 希伯来语 | `main/he/READ THIS TO USE-HE.md` |
| العربية / Arabic / 阿拉伯语 | `main/ar/READ THIS TO USE-AR.md` |
| Français / French / 法语 | `main/fr/READ THIS TO USE-FR.md` |
| 한국어 / Korean / 韩语 | `main/ko/READ THIS TO USE-KO.md` |

### 2A. 请选择本次对话使用的方言

> 1) 标准普通话（默认）
> 2) 上海话
> 3) 东北方言
> 4) 广东粤语
> 5) 四川方言
> 6) 新疆方言

> 回复 1–6；说“默认/跳过”用标准普通话。

### 2B. 請選擇本次對話使用的腔調

> 1) 標準華語（預設）
> 2) 港澳地區粵語
> 3) 台灣話

> 回覆 1–3；說「預設／跳過」用標準華語。

## 3. Hard rules

- Never ask for the Lead before the language answer (and, for the two Chinese editions, the dialect answer).
- The chosen entry is the only source of truth after routing.

## 4. Do not

- Do not read multiple editions at once.
- Do not add paths or extra options to the §1 question.
- Do not create Team members before the language/dialect/Lead answers.

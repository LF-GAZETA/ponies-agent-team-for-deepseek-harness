# 05 · 多网站来源台账与核验记录（Research Ledger）

> 本文件记录 mlp-ponies-agent-team 的调研范围、站点清单、实际抓取结果、事实交叉核对方式与局限。
> **原则：宁可标“低置信度/未核实”，也不编造来源。**
> 记录时间：2026-10-23（v1 语料抓取）→ 2026-10-24（本包补充多网站核对与重写）。数据库位置：`research/`。

---

## 1. 调研目标与方法

本项目要回答三类问题：

1. **角色事实（Who）：** 70 位角色的身份、外观、性格、能力、剧情、关系、台词、知识边界。
2. **地理事实（Where）：** 角色常用位置；以 T1 / Ponyville 为原点估算方位与距离带。
3. **时代与正典边界（When/What counts）：** G4、G4-EQG、G5 的差异；哪些来源算正典，哪些只算二次/参考。

**方法：**

1. **先建语料：** 抓取 Fandom（英文）角色页与地理页全文、Wikipedia 角色列表/作品页原文，形成 v1 语料库。
2. **再建档案：** 70 份英文正典档案（身份/性格/能力/剧情/关系/台词/位置/扮演指南/不确定性/来源）。
3. **本包补充多网站核对：** 官方站点、Equestria Daily（G5 地图分析）、Bilibili（小马利亚铁路资料）、中文社区
   （百度百科/萌娘百科/知乎/小红书——检索可见但抓取受限，仅作参考）、IMDb（受限）。
4. **冲突处理：** 按 P6 分级；同主题多来源不一致时，采用“动画 > 官方地图/设定集 > 二次正典 > 商品/游戏 > 同人”。
5. **落盘留证：** 下载内容存入 `research/raw_extra/`，抓取日志 `research/raw_extra/_fetch_log.tsv`。

---

## 2. 站点清单（按可信度分层）

| 层级 | 站点 | 示例 URL | 本项目用途 | 本轮可达性 |
|---|---|---|---|---|
| T1 官方 | Hasbro / My Little Pony 官方站 | https://mylittlepony.hasbro.com/en-us | 官方产品/时代信息、G5 官方定位 | ✅ 可访问（跳转全球客服页，内容有限） |
| T1 官方 | 官方 G5 电影/剧集本身 | （作品本体，不依赖网页） | 剧情与角色事实的最高依据 | ✅ 以作品为准（档案引用集数/电影名） |
| T2 百科 | Fandom — My Little Pony Wiki（英文） | https://mlp.fandom.com/wiki/Twilight_Sparkle | 51 角色页 + Ponyville/Canterlot/Cloudsdale/Crystal Empire/Everfree/Equestria 六地理页 | ⚠️ 本轮直连超时；**v1 已于 2026-10-23 抓取全文入库**（`../mlp_agents/_sources/`） |
| T2 百科 | Wikipedia（英文） | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | 角色列表、作品页交叉核对 | ⚠️ 本轮直连超时；**v1 已抓取 3 篇文本入库** |
| T2 百科 | Wikipedia（中文） | https://zh.wikipedia.org/wiki/小马宝莉 | 中文译名/概述参考 | ⚠️ 本轮直连超时（未采信） |
| T3 中文社区 | 百度百科 | https://baike.baidu.com/item/紫悦 等 | 中文译名、角色简介 | ❌ 403（反爬）；仅保留检索记录，**不据此写事实** |
| T3 中文社区 | 萌娘百科 | https://zh.moegirl.org.cn/My_Little_Pony | 中文社区译名/梗 | ❌ 403 |
| T3 中文社区 | Bilibili 专栏 | https://www.bilibili.com/opus/88954394813179970 | 小马利亚铁路线路与城镇连接（可用于地理合理性参考） | ✅ 已下载（`research/raw_extra/bilibili_rail.*`） |
| T3 中文社区 | 知乎 / 小红书 | https://zhuanlan.zhihu.com/p/108511604 等 | 中文资料索引（旅游手册/角色介绍） | 🔎 检索可见，未逐页抓取 |
| T4 粉丝媒体/分析 | Equestria Daily（EQD） | https://www.equestriadaily.com/2021/08/community-soapbox-g5-maps-gen-5-vs-gen.html | **G5 地图与 G4 大陆对照分析**（本包跨时代映射的关键参考） | ✅ 已下载全文（2.0 MB，已提取关键段落） |
| T4 粉丝媒体/分析 | EquestriaCN | https://www.equestriacn.com/2021/08/the-new-poster-for-the-film-features-a-simplified-map-of-the-g5-world.html | G5 海报简笔地图报道（检索可见） | 🔎 检索可见，未抓取 |
| T4 粉丝媒体/分析 | Fimfiction / DeviantArt / Ponerpics | https://www.fimfiction.net/... / https://www.deviantart.com/... | G5 地图讨论与同人地名整理 | 🔎 检索可见，**仅作线索，不作正典** |
| T4 影视资料 | IMDb | https://www.imdb.com/title/tt1751105/ | 演职员/作品信息 | ❌ 返回 202 反爬页（仅 2 KB） |

> T1 = 官方；T2 = 百科级；T3 = 中文社区/二次整理；T4 = 粉丝媒体/分析。**层级越低，越只能用于索引或旁证。**

---

## 3. 本轮实际执行记录（2026-10-24）

### 3.1 自动抓取（`tools/fetch_extra_sources.py` → `research/raw_extra/`）

| 结果 | 数量 | 说明 |
|---|---|---|
| ✅ 成功 | 6 | Bilibili 铁路专栏、Hasbro 官方页、EQD G5 地图长文、EQD 首页、IMDb 两条（仅反爬页，不采用） |
| ❌ 403/超时 | 18 | 百度百科 8 页、萌娘百科、Fandom G5 6 页、Wikipedia 4 页 —— 反爬或网络限制 |

抓取日志：`research/raw_extra/_fetch_log.tsv`（含 HTTP 状态、字节数、sha256 前缀、耗时、最终 URL）。

### 3.2 v1 语料（2026-10-23 抓取，本包直接复用）

| 语料 | 数量 | 位置 |
|---|---|---|
| Fandom 角色页全文（含 infobox） | 70 份，约 1.5 MB | `../mlp_agents/_sources/NN-<slug>.txt` |
| Fandom G4 地理页 | 6 份（Ponyville / Canterlot / Cloudsdale / Crystal Empire / Everfree / Equestria） | `../mlp_agents/_sources/_geo_*.txt` |
| Wikipedia 文本 | 角色列表 + A New Generation + Make Your Mark 等 | `../mlp_agents/_sources/_wiki_*.txt` |
| 角色 infobox 汇总 | `_infobox.json`（75 KB） | 同上 |
| v1 英文正典档案 | 70 份（12–25 KB/份） | `../mlp_agents/profiles/` |

### 3.3 补充检索（web_search，2026-10-24）

| 主题 | 检索式（示例） | 主要命中 | 采用情况 |
|---|---|---|---|
| 中文译名/角色概览 | 小马宝莉 角色 紫悦 云宝 柔柔 碧琪 苹果嘉儿 珍奇 | 百度百科、小红书、知乎、微信公众号 | 仅作译名旁证（未抓正文） |
| G4 地理/方位 | 小马宝莉 小马谷 坎特洛特 云中城 地图 方位 距离 | 知乎旅游手册、小红书全景地图、Bilibili | Bilibili 已下载；其余为线索 |
| G5 地图/位置 | MLP G5 玛雷泰湾 泽菲尔高地 布里德伍德 地图 位置 | EQD、EquestriaCN、Fimfiction、DeviantArt、Ponerpics | EQD 已下载并提取；Fimfiction/EquestriaCN 为线索 |
| G5 英文地图 | My Little Pony G5 Maretime Bay Zephyr Heights Bridlewood map locations | EQD、DeviantArt、Ponerpics | EQD 为准 |

### 3.4 关键提取（EQD G5 地图分析，原文摘录见 `research/raw_extra/eqd_g5_maps.txt`）

- Zephyr Heights 位于 **G4 Canterlot 所在的山上**（官方宣传图叠加旧地图）。
- Bridlewood 位于 **旧 Vanhoover 以南、Smoky Mountains 以西**（另一版本地图中可能在旧 Everfree 残余）。
- Maretime Bay 位于 **Horseshoe Bay 北端**（另一版本手绘地图中更偏西、临一片 G4 时代不存在的海）。
- 结论：两版 G5 地图不一致，任何 G4↔G5 换算都只能是 **Low confidence** 的工作假设。

### 3.5 关键提取（Bilibili 铁路资料，`research/raw_extra/bilibili_rail.*`）

- 铁路主线：Canterlot ↔ Griffonstone、Canterlot ↔ Manehattan、Canterlot ↔ Baltimare、Canterlot ↔ Ponyville 等；
- 支线连接 Appleloosa、Las Pegasus、White Tail Woods、Vanhoover、Crystal Empire、Rainbow Falls 等；
- 用途：为“Canterlot=regional / Appleloosa=far / Crystal Empire=far”一类距离带提供**合理性与旁证**；
- 注意：该文是粉丝整理（T3），未声称官方数据；本包只用作一致性检查，不作为精确距离来源。

---

## 4. 事实交叉核对矩阵

| 事实类别 | 主来源（T1/T2） | 交叉来源 | 结论/置信度 |
|---|---|---|---|
| G4 角色身份/性格/剧情 | 动画/电影本身 + Fandom 角色页 | Wikipedia 角色列表、v1 档案 | High（动画明确） |
| G4 角色台词 | Fandom 页面 quotes/wikitext（v1） | 动画集数代码 | High（引文均带集数） |
| G4 地理（Ponyville 布局） | 动画 + Fandom Ponyville | Wikipedia、Art of Equestria 地图（二次） | High（镇内）/ Medium（镇外方位） |
| G4 城镇方位与距离 | 动画旅行场景 + 官方地图（二次） | Bilibili 铁路资料、Fandom 地理页 | Medium（方位）/ Low–Medium（具体距离） |
| Everfree 方位 | Faust 表述（W） | Art of Equestria（E） | 冲突保留：W/E 两说，Medium |
| Sweet Apple Acres 方位 | Faust（SW） | Art of Equestria（SE） | 冲突保留：SW/SE 两说，High（同镇） |
| G5 三 settlement 地理 | 官方 G5 地图/电影 | EQD 分析、EquestriaCN、Fandom G5 页（v1 语料含 A New Generation/MYM） | Low（跨时代映射） |
| G5 角色性格/剧情 | G5 电影/MYM/TYT + Fandom G5 角色页（v1） | Wikipedia A New Generation/Make Your Mark | High（作品内） |
| 中文译名 | 官方中配/中文社区惯例 | 百度百科检索、Fandom 中文名（v1 cards 的 name_cn） | Medium（译名有多个版本，保留别名） |
| Equestria Girls 设定 | EQG 电影/短片 + Fandom | Wikipedia | High（作品内）/ Low（人类世界地理细节） |
| 配音/演职员 | Fandom infobox | IMDb（受限） | Medium（未逐条核验，档案只作背景） |

---

## 5. 来源分级与冲突处理规则（与 P6 一致）

1. **动画与电影**：最高；有画面即视为事实。
2. **官方地图/设定集/创作者表述**：次高；与动画冲突时以动画为准，并同时保留两种说法。
3. **官方漫画/书籍**：二次正典；引用必须写“二次/据漫画”。
4. **商品/游戏/广告**：三级；只作旁证，不写进正典叙述。
5. **粉丝 wiki/分析/同人**：只作索引与推断；推断必须标 Low，且不得包装成事实。
6. **冲突处理模板：** “A 来源说 X，B 来源说 Y；本包采用 Z，因为……；置信度 = High/Medium/Low。”

---

## 6. 51 角色来源台账

> 每个角色的**主来源**（Fandom 英文页）+ **交叉核对**（Wikipedia / 地理页 / 作品）+ 本包复核状态。
> 完整 URL 同时写入各 `agents/NN-*.md` 第 8 节。

| # | 角色 | 队伍 | 主来源（Fandom EN） | 交叉核对 / 补充来源 | 本包复核状态 |
|---|---|---|---|---|---|
| 01 | Twilight Sparkle / 紫悦 / 暮光闪闪 | T1 | https://mlp.fandom.com/wiki/Twilight_Sparkle | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Ponyville · https://mlp.fandom.com/wiki/Canterlot | **总指挥候选：重点复核** |
| 02 | Rainbow Dash / 云宝 | T1 | https://mlp.fandom.com/wiki/Rainbow_Dash | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Wonderbolt_Academy · https://mlp.fandom.com/wiki/Sonic_Rainboom | 继承 v1 语料 + 本包重建 |
| 03 | Fluttershy / 柔柔 | T1 | https://mlp.fandom.com/wiki/Fluttershy | https://mlp.fandom.com/wiki/Fluttershy%27s_Cottage · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Fluttershy_Leans_In | 继承 v1 语料 + 本包重建 |
| 04 | Pinkie Pie / 碧琪 | T1 | https://mlp.fandom.com/wiki/Pinkie_Pie | https://mlp.fandom.com/wiki/Pie_family · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/The_Last_Laugh | 继承 v1 语料 + 本包重建 |
| 05 | Applejack / 苹果嘉儿 | T1 | https://mlp.fandom.com/wiki/Applejack | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://en.wikipedia.org/wiki/Applejack_(My_Little_Pony) · https://mlp.fandom.com/wiki/Applebuck_Season | 继承 v1 语料 + 本包重建 |
| 06 | Rarity / 珍奇 | T1 | https://mlp.fandom.com/wiki/Rarity | https://mlp.fandom.com/wiki/Carousel_Boutique · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Rarity_Takes_Manehattan | 继承 v1 语料 + 本包重建 |
| 07 | Princess Celestia / Daybreaker / 塞拉斯蒂娅公主 | T0 | https://mlp.fandom.com/wiki/Princess_Celestia | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Canterlot · https://mlp.fandom.com/wiki/The_Last_Problem | **总指挥候选：重点复核** |
| 08 | Princess Luna / Nightmare Moon / 露娜公主 / 梦魇之月 | T0 | https://mlp.fandom.com/wiki/Princess_Luna | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://en.wikiquote.org/wiki/My_Little_Pony:_Friendship_is_Magic_(season_1) · https://mlp.fandom.com/wiki/Luna_Eclipsed | **总指挥候选：重点复核** |
| 09 | Princess Cadance / 韵律公主 | T0 | https://mlp.fandom.com/wiki/Princess_Cadance | https://mlp.fandom.com/wiki/The_Crystalling_-_Part_1 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/A_Canterlot_Wedding_-_Part_1 | **总指挥候选：重点复核** |
| 10 | Shining Armor / 银甲 | T0 | https://mlp.fandom.com/wiki/Shining_Armor | https://mlp.fandom.com/wiki/A_Canterlot_Wedding_-_Part_1 · https://mlp.fandom.com/wiki/The_Crystal_Empire_-_Part_2 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | 继承 v1 语料 + 本包重建 |
| 11 | Flash Sentry / 闪电卫兵 | T0 | https://mlp.fandom.com/wiki/Flash_Sentry | https://mlp.fandom.com/wiki/Flash_Sentry_(EG) · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestriagirls.fandom.com/wiki/Flash_Sentry | 继承 v1 语料 + 本包重建 |
| 12 | Queen Chrysalis / 虫茧女王 | T3 | https://mlp.fandom.com/wiki/Queen_Chrysalis | https://en.wikipedia.org/wiki/List_of_My_Little_Pony_characters · https://mlp.fandom.com/wiki/Transcripts/A_Canterlot_Wedding_-_Part_2 · https://mlp.fandom.com/wiki/Changeling_Kingdom | 继承 v1 语料 + 本包重建 |
| 13 | Lord Tirek / 提雷克领主 | T3 | https://mlp.fandom.com/wiki/Lord_Tirek | https://mlp.fandom.com/wiki/Transcripts/Twilight%27s_Kingdom_-_Part_1 · https://mlp.fandom.com/wiki/Transcripts/Twilight%27s_Kingdom_-_Part_2 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | 继承 v1 语料 + 本包重建 |
| 14 | Cozy Glow / 和煦光流 | T3 | https://mlp.fandom.com/wiki/Cozy_Glow | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/School_Raze_-_Part_2 | 继承 v1 语料 + 本包重建 |
| 15 | Sweetie Belle / 甜心宝宝 | T2 | https://mlp.fandom.com/wiki/Sweetie_Belle | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/The_Show_Stoppers | 继承 v1 语料 + 本包重建 |
| 16 | Apple Bloom / 小苹花 | T2 | https://mlp.fandom.com/wiki/Apple_Bloom | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/Call_of_the_Cutie · https://mlp.fandom.com/wiki/Transcripts/Crusaders_of_the_Lost_Mark | 继承 v1 语料 + 本包重建 |
| 17 | Scootaloo / 飞板璐 | T2 | https://mlp.fandom.com/wiki/Scootaloo | https://en.wikipedia.org/wiki/Flight_to_the_Finish · https://mlp.fandom.com/wiki/Transcripts/Flight_to_the_Finish · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | 继承 v1 语料 + 本包重建 |
| 18 | Derpy Hooves / 小呆 | T2 | https://mlp.fandom.com/wiki/Derpy_Hooves | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/Slice_of_Life · https://en.wikipedia.org/wiki/Derpy_Hooves | 继承 v1 语料 + 本包重建 |
| 19 | Lightning Dust / 闪电尘 | T2 | https://mlp.fandom.com/wiki/Lightning_Dust | https://mlp.fandom.com/wiki/Transcripts/Wonderbolts_Academy · https://mlp.fandom.com/wiki/Transcripts/The_Washouts · https://en.wikipedia.org/wiki/The_Wonderbolts | 继承 v1 语料 + 本包重建 |
| 20 | Trixie / 特丽克西 | T4 | https://mlp.fandom.com/wiki/Trixie | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/Boast_Busters · https://mlp.fandom.com/wiki/Transcripts/No_Second_Prances | 继承 v1 语料 + 本包重建 |
| 21 | Starlight Glimmer / 星光熠熠 | T4 | https://mlp.fandom.com/wiki/Starlight_Glimmer | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/The_Cutie_Re-Mark_-_Part_2 · https://mlp.fandom.com/wiki/Our_Town | 继承 v1 语料 + 本包重建 |
| 22 | Discord / 无序 | T4 | https://mlp.fandom.com/wiki/Discord | https://mlp.fandom.com/wiki/Transcripts/The_Return_of_Harmony_Part_1 · https://mlp.fandom.com/wiki/Transcripts/The_Ending_of_the_End_-_Part_2 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony_characters | 继承 v1 语料 + 本包重建 |
| 23 | Vinyl Scratch / 黑胶唱片 / DJ Pon-3 | T4 | https://mlp.fandom.com/wiki/Vinyl_Scratch | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Slice_of_Life · https://mlp.fandom.com/wiki/The_Saddle_Row_Review | 继承 v1 语料 + 本包重建 |
| 24 | Lyra Heartstrings / 天琴心弦 | T4 | https://mlp.fandom.com/wiki/Lyra_Heartstrings | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Lyra_Heartstrings_and_Sweetie_Drops_(EG) · https://mlp.fandom.com/wiki/Slice_of_Life | 继承 v1 语料 + 本包重建 |
| 25 | Octavia Melody / 奥克塔维亚 | T4 | https://mlp.fandom.com/wiki/Octavia_Melody | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Octavia_Melody_(EG) · https://mlp.fandom.com/wiki/Slice_of_Life | 继承 v1 语料 + 本包重建 |
| 26 | Bon Bon / 糖糖 / 甜心糖 | T4 | https://mlp.fandom.com/wiki/Bon_Bon | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Slice_of_Life · https://mlp.fandom.com/wiki/Call_of_the_Cutie | 继承 v1 语料 + 本包重建 |
| 27 | King Sombra / 黑晶王 | T3 | https://mlp.fandom.com/wiki/King_Sombra | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestripedia.org/wiki/King_Sombra · https://mlp.fandom.com/wiki/The_Crystal_Empire | 继承 v1 语料 + 本包重建 |
| 28 | Tempest Shadow / Fizzlepop Berrytwist / 暴风影 / 菲兹尔波普 | T4 | https://mlp.fandom.com/wiki/Tempest_Shadow | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestripedia.org/wiki/Tempest_Shadow · https://mlp.fandom.com/wiki/The_Storm_King | 继承 v1 语料 + 本包重建 |
| 29 | Spitfire / 喷火队长 | T4 | https://mlp.fandom.com/wiki/Spitfire | https://mlp.fandom.com/wiki/Wonderbolts · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Wonderbolt_Academy_(location) | 继承 v1 语料 + 本包重建 |
| 30 | Sci-Twi / Midnight Sparkle / 人类紫悦 / 午夜闪闪 | T5 | https://mlp.fandom.com/wiki/Twilight_Sparkle_(Sci-Twi) | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Equestria_Girls:_Friendship_Games · https://mlp.fandom.com/wiki/Equestria_Girls:_Legend_of_Everfree | 继承 v1 语料 + 本包重建 |
| 31 | Adagio Dazzle / 阿达吉奥 | T5 | https://mlp.fandom.com/wiki/Adagio_Dazzle | https://equestriagirls.fandom.com/wiki/Dazzlings · https://equestriagirls.fandom.com/wiki/Starswirled_Music_Festival · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | 继承 v1 语料 + 本包重建 |
| 32 | Sonata Dusk / 索纳塔 | T5 | https://mlp.fandom.com/wiki/Sonata_Dusk | https://mlp.fandom.com/wiki/The_Dazzlings · https://equestriagirls.fandom.com/wiki/Starswirled_Music_Festival · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | 继承 v1 语料 + 本包重建 |
| 33 | Aria Blaze / 阿莉娅 | T5 | https://mlp.fandom.com/wiki/Aria_Blaze | https://mlp.fandom.com/wiki/The_Dazzlings · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Equestria_Girls:_Rainbow_Rocks | 继承 v1 语料 + 本包重建 |
| 34 | Princess Flurry Heart / 风雪之心公主 | T0 | https://mlp.fandom.com/wiki/Princess_Flurry_Heart | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Crystal_Empire | 继承 v1 语料 + 本包重建 |
| 35 | Spike / 斯派克 | T1 | https://mlp.fandom.com/wiki/Spike | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation | 继承 v1 语料 + 本包重建 |
| 36 | Sunset Shimmer / 余晖烁烁 | T5 | https://mlp.fandom.com/wiki/Sunset_Shimmer | https://en.wikipedia.org/wiki/My_Little_Pony:_Equestria_Girls · https://en.wikipedia.org/wiki/My_Little_Pony:_Equestria_Girls_%E2%80%93_Rainbow_Rocks | 继承 v1 语料 + 本包重建 |
| 37 | Gloriosa Daisy / 格洛丽萨·黛西 | T5 | https://mlp.fandom.com/wiki/Gloriosa_Daisy | https://mlp.fandom.com/wiki/Camp_Everfree · https://en.wikiquote.org/wiki/My_Little_Pony:_Equestria_Girls_%E2%80%93_Legend_of_Everfree | 继承 v1 语料 + 本包重建 |
| 38 | Juniper Montage / 朱尼珀·蒙太奇 | T5 | https://mlp.fandom.com/wiki/Juniper_Montage | https://equestripedia.org/wiki/Juniper_Montage · https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/MyLittlePonyEquestriaGirlsMagicalMovieNight | 继承 v1 语料 + 本包重建 |
| 39 | Wallflower Blush / 壁花 | T5 | https://mlp.fandom.com/wiki/Wallflower_Blush | https://mlp.fandom.com/wiki/Forgotten_Friendship · https://en.wikipedia.org/wiki/My_Little_Pony:_Equestria_Girls | 继承 v1 语料 + 本包重建 |
| 40 | Big Macintosh / 大麦克 | T2 | https://mlp.fandom.com/wiki/Big_McIntosh | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Sweet_Apple_Acres | 继承 v1 语料 + 本包重建 |
| 41 | Pear Butter / 梨子黄油 | T2 | https://mlp.fandom.com/wiki/Pear_Butter | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/The_Perfect_Pear | 继承 v1 语料 + 本包重建 |
| 42 | Soarin' / 翱翔 | T6 | https://mlp.fandom.com/wiki/Soarin%27 | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Cloudsdale | 继承 v1 语料 + 本包重建 |
| 43 | Zecora / 泽科拉 | T6 | https://mlp.fandom.com/wiki/Zecora | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestripedia.org/wiki/Zecora_(Friendship_is_Magic) | 继承 v1 语料 + 本包重建 |
| 44 | Daring Do / A.K. Yearling / 无畏天马 / A.K. Yearling | T6 | https://mlp.fandom.com/wiki/Daring_Do | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Daring_Don%27t | 继承 v1 语料 + 本包重建 |
| 45 | Misty Brightdawn / 米斯蒂·黎明 | T6 | https://mlp.fandom.com/wiki/Misty | https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | 继承 v1 语料 + 本包重建 |
| 46 | Sunny Starscout / 桑妮·寻星 | T6 | https://mlp.fandom.com/wiki/Sunny_Starscout | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://en.wikipedia.org/wiki/Equestria | 继承 v1 语料 + 本包重建 |
| 47 | Izzy Moonbow / 伊兹·月弓 | T6 | https://mlp.fandom.com/wiki/Izzy_Moonbow | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://mlp.fandom.com/wiki/Cutie_Blossom_Bash | 继承 v1 语料 + 本包重建 |
| 48 | Hitch Trailblazer / 希奇·开路者 | T6 | https://mlp.fandom.com/wiki/Hitch_Trailblazer | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark | 继承 v1 语料 + 本包重建 |
| 49 | Zipp Storm / 齐普·风暴 | T6 | https://mlp.fandom.com/wiki/Zipp_Storm | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://www.equestriadaily.com/2021/08/this-updated-map-from-my-little-pony.html | 继承 v1 语料 + 本包重建 |
| 50 | Pipp Petals / 皮普·花瓣 | T6 | https://mlp.fandom.com/wiki/Pipp_Petals | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://mlp.fandom.com/wiki/Jazz_Hooves | 继承 v1 语料 + 本包重建 |
| 51 | Opaline Arcana / 奥帕琳·阿卡娜 | T6 | https://mlp.fandom.com/wiki/Opaline | https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://mlp.fandom.com/wiki/Locations · https://villains.fandom.com/wiki/Queen_Opaline | 继承 v1 语料 + 本包重建 |

---

## 7. 局限与未完成事项（必须如实告知客户）

1. **本轮无法直连 Fandom/Wikipedia/百度百科/萌娘百科**（超时/403）。角色事实依赖 2026-10-23 已抓取的 v1 语料（Fandom 全文 + Wikipedia 文本），本轮只做了增量站点（EQD/Bilibili/官方）与检索级旁证。
2. **中文百科未取得正文**：百度百科/萌娘百科只保留检索记录，不作为事实依据；中文译名以 v1 卡片与社区惯例为准，并保留多译名。
3. **G5 地图存在两版不一致**：EQD 分析明确指出；本包采用折中映射并全部标 Low。若客户需要“官方精确坐标”，目前没有这样的公开数据。
4. **距离数值是粗估**：来自 v1 项目的等距投影式换算，只用于“距离带”判断；不要引用具体 km 作为设定事实。
5. **配音/演职员信息**未逐条核验（IMDb 反爬）；档案中仅作背景，不作为角色能力/剧情依据。
6. **二次正典（IDW/官方书）** 未逐本核对；涉及处已标“二次/低一级”，未影响主线档案。
7. **时效性：** 调研截至 2026-10-24；若作品有新作/官方设定更新，应按 P6 重新分级并更新档案。

---

## 8. 证据清单（文件）

| 文件/目录 | 内容 | 大小级别 |
|---|---|---|
| `research/raw_extra/_fetch_log.tsv` | 24 条抓取记录（状态/字节/sha256/耗时/最终 URL） | 小 |
| `research/raw_extra/eqd_g5_maps.*` | EQD「G5 Maps」长文（G4↔G5 地图对照） | 2.0 MB |
| `research/raw_extra/bilibili_rail.*` | Bilibili 小马利亚铁路资料 | 57 KB |
| `research/raw_extra/official_mlp_home.*` | Hasbro 官方页（跳转全球客服） | 67 KB |
| `research/raw_extra/imdb_*` | IMDb 反爬页（不采用） | 2 KB ×2 |
| `../mlp_agents/_sources/` | v1 全量语料：51 角色页 + 6 地理页 + Wikipedia 文本 | ~2.5 MB |
| `../mlp_agents/profiles/` | v1 英文正典档案（70 份） | ~800 KB |
| `data/cards8.json` | 51 角色运行卡（含 sources 字段） | ~750 KB |
| `docs/02-geography.md` | 位置总表与 65 地点参照 | 38 KB |

---

## 9. 复核与更新建议（给后续维护者）

1. 网络可用时，重新抓取 Fandom G5 三 settlement 页、Wikipedia G5 页面，补入 `_sources`。
2. 若获得官方 G5 地图高清版/设定集，按“官方地图 > EQD 分析”更新第 5 节映射与置信度。
3. 中文百科解禁后，补做中文译名与角色简介交叉核对，更新 `name_cn` 与译名表。
4. 任何新来源入库时，必须更新：本文件、`data/cards8.json` 的 sources、相关 Agent 文件第 8 节，并跑 `tools/validate.py`。
5. 不要删除失败记录——它是“我们没核实什么”的证据，也是后续维护的路线图。

---

**版本：** v1.0（2026-10-24）｜ 维护：总指挥 + Spike（档案）｜ 变更需同步 `data/` 与 Agent 文件来源节。

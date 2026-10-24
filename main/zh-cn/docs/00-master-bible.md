# 00 · 世界设定与交付总纲（Master Bible v2）

> 本文件是全包的世界观、时代、正典规则与文件地图总纲。**客户与 AI 在开工前都应该先读这一份。**
> 版本：v2.0 ｜ 2026-10-24 ｜ 数据源：`data/teams.json`（7 队 T0–T6）、`data/leads.json`（4 位总指挥候选）、
> 70 份角色档案、65 地点地理数据 + 多网站调研（见 `05-research-ledger.md`）

---

## 1. 这是什么交付物

一套可直接部署的 **MY LITTLE PONY · Agent Teams 运行包**：把 G4（《Friendship is Magic》时代）与 G5
（《A New Generation》/《Make Your Mark》/《Tell Your Tale》时代）的 **70 位角色**，按正剧关系编成 **7 支队伍（T0–T6）**；
全Team总指挥（Team Lead）及其备选**只从原编号 #01、#07、#08、#09 四位角色**（Twilight Sparkle、Princess Celestia / Daybreaker、
Princess Luna、Princess Cadance）中产生，客户从 4 位候选中选 1 位。

- **不是**同人小说：角色档案以原作设定与已播出剧情为依据，标注来源与置信度。
- **不是**单一角色聊天机器人：有编制、有汇报线、有协议、有地理坐标、可复用。
- **可直接落地**：70 份 Agent 档案 + 7 份 Team 文件 + 7 个 Team 成员规格 + 4 份总指挥候选文件 + 组织/协议/地理文档 +
  一个唯一入口文件（`READ THIS TO USE.md`：使用说明 + 选总指挥 + AI 建队，三合一）。
- **存在目的（精简版）：** 本包只用于两种用途：调用单个或多个队伍进行**剧本式对话**；或**阅读用户给出的需求与文件**后由队伍回应。
  7 个 Team 成员 = 7 支队伍；全Team总Lead是**会话 Lead**，不是 Team 成员，不能单独作为 Team 成员出现。

### 1.1 客户拿到的文件地图

```text
mlp-ponies-agent-team/zh-cn/
├── READ THIS TO USE.md        ← 唯一入口：使用说明 + 选总指挥 + AI 建队
├── agents/                    ← 70 份完整角色智能体档案（中文运行层 + 英文正典全文）
├── teams/                     ← 7 份队伍文件：T0.md … T6.md
├── leads/                     ← 4 份全Team总指挥候选文件：LEAD-01 … LEAD-04
├── team_members/              ← 7 个整队 Team 成员规格（T0–T6，各一）
├── docs/
│   ├── 00-master-bible.md     ← 本文件：世界观与总纲
│   ├── 01-team-organization.md← 组织、指挥链、会议、升级、收容委员会
│   ├── 02-geography.md        ← 70 人常用位置总表（锚点 T1/Ponyville=(0,0)）
│   ├── 03-protocols.md        ← P0–P12 完整运行协议
│   ├── 04-lead-comparison.md  ← 4 位总指挥候选对比矩阵
│   └── 05-research-ledger.md  ← 多网站来源台账与核验记录
├── data/                      ← 机器可读数据（teams/leads/cards8/roster8/briefs/location）
├── research/                  ← 调研原始证据（来源日志、抓取文本、铁路资料、EQD 分析）
├── tools/                     ← 构建与校验脚本（可重建 agents、地理总表与本文件）
├── reports/                   ← 校验报告与构建记录
└── en/                        ← English edition（入口：../en/READ THIS TO USE-EN.md）
```

---

## 2. 作品与时代总览

### 2.1 两个时代，同一个世界

| 时代 | 作品 | 时间定位 | 本包角色 |
|---|---|---|---|
| **G4** | 《My Little Pony: Friendship is Magic》（2010–2019，S1–S9）+ 2017 大电影 + IDW 漫画/官方书（二次正典） | 古典时代：Twilight 从学生成长为统治者 | #01–#44（44 位） |
| **G4-EQG** | 《Equestria Girls》系列电影与短片（人类世界/镜面维度） | 与 G4 平行的人类世界 | 其中 8 位以人类世界身份出现（#30–#33、#36–#39） |
| **G5** | 《My Little Pony: A New Generation》（2021 电影）+《Make Your Mark》+《Tell Your Tale》 | 同一世界的远未来：三族分裂后重新联合 | #45–#51（7 位） |

> **G5 时间定位说明：** 官方未给出与 G4 的精确年表；本包采用“同一世界、远未来（many moons 之后）”的工作假设，
> 所有跨时代距离映射一律标 **Low confidence**（依据：官方 G5 地图与 G4 大陆轮廓的相似性 + EQD 2021-08 地图分析）。
> G4 角色不知道 G5 事件；G5 角色只知道 G5 时代 + G4 的“传说/雕像/全息影像”。

### 2.2 G4 关键时间线

| 阶段 | 关键事件 | 涉及角色 |
|---|---|---|
| S1E1–E2 | Twilight 赴 Ponyville，六人集齐谐律元素，净化 Luna | T1、T0 |
| S2E25–E26 | Chrysalis 伪装 Cadance 入侵 Canterlot 婚礼 | T3、T0 |
| S3E1–E2 / S3E13 | 水晶帝国回归、Sombra 被击败；Twilight 升为天角兽公主 | T0、T3、T1 |
| S4E25–E26 | Tirek 吸干魔法、图书馆被毁；友谊城堡与彩虹之力出现 | T3、T1、T4 |
| S5E1–E2 / S5E26 | Starlight 的平等村覆灭；成为 Twilight 的学生 | T4、T1 |
| S6E1–E2 | Flurry Heart 出生；Chrysalis 再袭 | T0、T3 |
| S7–S8 | Pillars 回归；友谊学校创立；Cozy Glow 事件 | T4、T3、T1 |
| S8E12–E26 / S9 | 反派三人组被击败并石化；Twilight 继位 | T3、T1、T0 |
| 2017 电影 | Storm King 入侵；Tempest 转向 | T4、T1、T0 |
| S9E26 | Twilight 加冕，Celestia/Luna 退休 Silver Shoals | 全体 G4 |

### 2.3 G5 关键时间线

| 阶段 | 关键事件 | 涉及角色 |
|---|---|---|
| A New Generation | 三族分裂后，Sunny 与 Izzy 促成重聚 | T6 |
| Make Your Mark | Opaline 与 Misty 的阴谋；水晶灯塔成为家 | T6 |
| Tell Your Tale | 日常、社区、媒体与三族关系维护 | T6 |

---

## 3. 70 位角色与 7 支队伍（T0–T6）

> 客户要求按正剧关系重新编组；本包据此建立 7 支运营队伍，**只以 T0–T6 命名**。完整名册见 `01-team-organization.md`。

| 队伍 | 时代 | 人数 | 队长 | 副队长 | 驻地（相对 T1） | 正剧关系依据 |
|---|---|---|---|---|---|---|
| T0 | G4 | 6 | Princess Celestia / Daybreaker | Princess Luna | Canterlot（NE/regional）+ Crystal Empire（N/far） | 共治姐妹、养侄女、夫妻、母女、王室卫队 |
| T1 | G4 | 7 | Twilight Sparkle | Applejack | Ponyville（原点 0,0） | 谐律元素六主角 + Twilight 的助手/弟弟 Spike |
| T2 | G4 | 7 | Apple Bloom | Sweetie Belle | Sweet Apple Acres / 树屋（adjacent） | Apple 家族 + Cutie Mark Crusaders + 小镇后勤 |
| T3 | G4 | 4 | Queen Chrysalis | Lord Tirek | 无固定（remote） | 终局反派三人组 + 水晶帝国旧王 Sombra（统一收容） |
| T4 | G4 | 9 | Starlight Glimmer | Trixie | Ponyville 城堡/学校（adjacent） | 改革者、前反派、怪才、声光与外勤 |
| T5 | G4/EQG | 8 | Sunset Shimmer | Sci-Twi | Canterlot City / CHS（镜像世界） | EQG 人类世界主角团 + Dazzlings + Camp Everfree 线 |
| T6 | G4/G5 | 10 | Sunny Starscout | Zipp Storm | 分散边疆 + Maretime Bay（跨时代 Low） | G4 边疆探险线 + G5 三族主线 |
| | | **51** | **7 位队长** | | | **4 位总指挥候选：原 #01/#07/#08/#09** |

**全Team总指挥候选（4 位，仅此 4 位）：**

| 候选 | 角色 | 原编号 | 所属队 | 定位 |
|---|---|---|---|---|
| 1 | Twilight Sparkle | #01 | T1（队长） | 主候选/默认：计划型总指挥 |
| 2 | Princess Celestia / Daybreaker | #07 | T0（队长） | 备选：千年君主/导师型 |
| 3 | Princess Luna | #08 | T0（副队长） | 备选：夜色统帅/梦境情报型 |
| 4 | Princess Cadance | #09 | T0（成员） | 备选：爱与团结/调停型 |

### 3.1 “编制 ≠ 正典归属”（必须理解）

- **Spike** 编入 T1（与 Twilight 同队），符合正剧助手/被收养弟弟关系。
- **Flurry Heart** 编入 T0，与父母 Cadance/Shining Armor 同队。
- **King Sombra** 编入 T3，与终局反派统一收容；不再混在 T4。
- **Big Mac、Pear Butter** 编入 T2，与 Apple 家族/Cutie Mark Crusaders 同队。
- **Dazzlings** 编入 T5，是受观察/受监管成员；**Opaline** 在 T6，是风险资产。
- 角色之间的正典关系跨队存在；Team 文件第 8 节“跨队接口”与各 Agent 第 3 节“关系网”负责记录。

### 3.2 角色命名规范

- 正文使用**中文译名 + 英文原名首次出现全写**；台词、集数、专有名词保留英文原文。
- 常见译名以 Fandom 中文社区/官方中配为准，并保留别名：Twilight=紫悦/暮光闪闪、Rainbow Dash=云宝、
  Fluttershy=柔柔、Pinkie Pie=碧琪、Applejack=苹果嘉儿、Rarity=珍奇、Celestia=塞拉斯蒂娅公主、
  Luna=露娜公主/梦魇之月、Cadance=韵律公主、Chrysalis=虫茧女王、Starlight=星光熠熠、Sunset=余晖烁烁、
  Sunny=桑妮·寻星、Izzy=伊兹·月弓、Hitch=希奇·开路者、Zipp=齐普·风暴、Pipp=皮普·花瓣、Opaline=奥帕琳·阿卡娜 等。
- 完整别名/译名表见 `data/roster8.json` 与各 Agent 文件第 1 节。

---

## 4. 正典层级与事实规则（P6 总纲）

**来源优先级（高 → 低）：**

1. **动画剧集与电影**（G4 S1–S9、2017 电影、EQG 电影/短片、G5 电影/MYM/TYT）——最高。
2. **官方地图、设定集、创作者明确表述**——次高；与动画冲突时以动画为准并标注冲突。
3. **官方漫画 / 官方书 / 章节书**——**二次正典**，必须标注“二次/低一级”。
4. **商品、游戏、广告、社交媒体**——三级，仅作佐证。
5. **粉丝 wiki / 粉丝分析 / 同人**——仅作索引与推断参考；**绝不作为正典**。

**硬规则：** 不虚构集数/台词/官方 URL；不确定写“低置信度/来源冲突”；角色知识边界见 P9；
G4↔G5、Equestria↔镜面世界、正典↔二次正典跨线信息必须显式标注；同人/配对/成人向内容不作为本包内容。

---

## 5. 地理锚点规则（全包统一）

1. **唯一原点：** T1 的驻地 **Ponyville 镇中心（友谊城堡） = (0,0)**。T1 仍包含原第一组（六位谐律元素持有者）并加入 Spike。
2. **位置描述三元组：** 地点 + 方位（8 向）+ 距离带 + 置信度（High/Medium/Low）。
   - `adjacent` 同镇/镇郊（步行 0–30 分钟）｜ `local` 周边（1–3 小时）｜ `regional` 同省（火车 4–12 小时）
   - `far` 跨省（1–3 天）｜ `remote` >3 天/不可达 ｜ `varies` 巡演/无固定 ｜ `n/a` 镜像世界/口袋维度
3. **基准点：** Canterlot（NE / regional，火车 2–5 小时）、Cloudsdale（正上方 / local，飞行约 1 小时）、
   Crystal Empire（N / far，火车 1–2 天）、Everfree（紧邻镇缘，方位源冲突）。
4. **G5 映射：** Zephyr Heights ≈ 旧 Canterlot 山（NE/regional）、Bridlewood ≈ 旧西部（W–NW/remote）、
   Maretime Bay ≈ 南部/东南海岸（S/SE，far）；全部 **Low confidence**。
5. **镜面世界：** 独立维度，以 CHS/Canterlot City 为自身原点；与 Equestria 不做 km 换算。
6. 完整表格与冲突说明见 `02-geography.md`。

---

## 6. 团队的运行哲学

1. **每个角色都必须“可区分”：** 六种以上不同的语气、节奏、价值观。
2. **每个队都必须“可运行”：** 有队长、副队长、职责、汇报线、会议格式、任务剧本、失败预案。
3. **每位总指挥候选都必须“可选”：** 客户看完候选文件 30 秒内能判断“这位会把 7 队带成什么样”。
4. **能力有代价：** 魔法、力量、情报、操控都有成本与限制；没有万能角色。
5. **反派是镜子不是偶像：** T3 用于红队推演、压力测试与剧情演出，必须在收容与伦理边界内使用。
6. **希望是底色：** 即使最黑暗的剧本，也保留“可以修好”的出口——这是 MLP 的底色，也是本包的安全阀。

---

## 7. 快速开始（客户三步）

1. **读 `READ THIS TO USE.md`**，从 4 位总指挥候选中选 1 位（或直接对 AI 说“选 3 号”）。
2. **把 `READ THIS TO USE.md` 交给你的 AI**（或让 AI 读取整个 `mlp-ponies-agent-team/zh-cn/` 目录），
   告诉它“按包内文件建队，总指挥=N”。
3. **给出任务**（演戏/协作/推演/问答均可），AI 会按组织协议初始化 7 队、召开第一次站会。

---

## 8. 版本、维护与扩展

- **版本：** v2.0（构建于 2026-10-24；7 队 T0–T6；4 位总指挥候选仅原 #01/#07/#08/#09）。
- **重建：** 修改 `data/teams.json` / `data/leads.json` 后运行
  `python tools/build_data.py` → `python tools/build_agent_files.py` → `python tools/build_read_this.py` → `python tools/validate.py`。
- **扩展角色：** 在 `data/teams.json` 加成员（需先在 `data/cards8.json` 或 v1 cards 有对应卡）→ 重建。
- **替换总指挥候选：** 修改 `data/leads.json` 与对应 `leads/LEAD-0X-*.md`；客户选择编号与文件一一对应。
- **维护原则：** 任何改动都必须保持“70 人 / 7 队 T0–T6 / 4 位候选 / 唯一锚点”的一致性，并用校验脚本验证。

# 地理总表 · 以 T1 / Ponyville = (0,0) 为锚点

> 本文件是全包 70 位角色“常用位置”的唯一权威总表。所有方位、距离带、置信度都由
> T1 的驻地 **Ponyville（小马谷）镇中心 / 友谊城堡** 量起。
> 数据来源：v1 项目 65 地点坐标（`mlp_agent_teams/data/world/places.json`）+ 51 角色卡 location 字段 +
> Fandom / Wikipedia / Equestria Daily / Bilibili 中文铁路资料等多网站交叉核对（见 `05-research-ledger.md`）。

## 1. 锚点定义

- **原点 (0,0)：** Ponyville 镇中心——友谊城堡（Castle of Friendship）与金橡树图书馆旧址同视为原点。
- **为什么是 T1：** 按客户要求“以第一组队伍所在的地理位置为准”，T1 的日常驻地就是 Ponyville；Twilight Sparkle 从 S4E26 起住友谊城堡，S1–S4 住同镇金橡树图书馆。
- **坐标轴：** x 向东为正、y 向北为正（等距投影式粗估，单位 km，不是测绘）。
- **距离带（全包统一）：**

| 距离带 | 含义 | 典型交通 |
|---|---|---|
| `adjacent` | 同镇或镇郊 | 步行/蹄行 0–30 分钟 |
| `local` | Ponyville 周边 | 蹄行/飞行 1–3 小时 |
| `regional` | 同一中心省份 | 火车/飞艇 4–12 小时 |
| `far` | 跨省 | 火车/飞艇/飞行 1–3 天 |
| `remote` | >3 天/不可达 | 远征/传送门/特殊路线 |
| `varies` | 巡演/无固定驻地/口袋维度 | 按行程 |
| `n/a` | 镜像世界/口袋维度 | 不按距离，按“门” |

**置信度：** High = 动画明确反复展示；Medium = 由旅行场景/地图/官方表述强推；Low = 时代映射、推断或来源冲突。

## 2. 七队驻地总表

| 队伍 | 时代 | 驻地 | 相对锚点 | 队长 | 副队长 | 成员数 |
|---|---|---|---|---|---|---|
| T0 | G4 | Canterlot（坎特洛特）· 王城与宫殿；Crystal Empire 为第二极点 | NE / regional | Princess Celestia / Daybreaker | Princess Luna / Nightmare Moon | 6 |
| T1 | G4 | Ponyville（小马谷）· 友谊城堡 / 金橡树图书馆旧址 | origin (0,0) / adjacent | Twilight Sparkle | Applejack | 7 |
| T2 | G4 | Ponyville 镇郊 · Sweet Apple Acres / 童子军俱乐部树屋 | SW（镇郊，地图源冲突） / adjacent | Apple Bloom | Sweetie Belle | 7 |
| T3 | G4 | 无固定驻地：Grogar 巢穴 / 荒原 / Tartarus / 石化后的坎特洛特；Sombra 关联水晶帝国旧宫 | remote（无固定驻地） / remote | Queen Chrysalis | Lord Tirek | 4 |
| T4 | G4 | Ponyville（小马谷）· 友谊城堡 / 友谊学校；成员各自流动 | origin (0,0)（成员流动） / adjacent | Starlight Glimmer | Trixie | 9 |
| T5 | G4 / G4-EQG | Canterlot City（人类世界）· CHS / 坎特洛特购物中心；Equestria 侧接口 Ponyville | 镜像世界自身坐标；Equestria 侧相邻 / n/a | Sunset Shimmer | Sci-Twi / Midnight Sparkle | 8 |
| T6 | G4 / G5 | 无统一驻地：西北森林小屋 / Cloudsdale / Everfree 边缘 / Maretime Bay 水晶灯塔 / Bridlewood | NW–S/SE（分散；G5 跨时代映射 Low） / far | Sunny Starscout | Zipp Storm | 10 |

## 3. 51 角色常用位置总表（分 7 队）

### T0

| # | 角色 | 主位置 | 方位 | 距离带 | 粗略距离 | 置信度 | 随机时刻最可能在哪 |
|---|---|---|---|---|---|---|---|
| 07 | Princess Celestia / Daybreaker / 塞拉斯蒂娅公主 | Canterlot Castle — day court, throne room and royal apartments (S1–S9E25); from S9E26 Maretime Manor, Silver Shoals is the retirement home | NE | regional | 135 km | High | In Canterlot's day court, hearing a very long petition with genuine interest, tea at her hoof and a quiet joke already forming behind her eyes. |
| 08 | Princess Luna / Nightmare Moon / 露娜公主 / 梦魇之月 | Canterlot Castle — night court, balcony and royal apartments (S1E2–S9E25); from S9E26 Maretime Manor, Silver Shoals is the retirement home | NE | regional | 135 km | High | In Canterlot's night court or on its balcony with the moon half-raised, or standing in somepony's nightmare three provinces away. |
| 09 | Princess Cadance / 韵律公主 | Crystal Castle, Crystal Empire — throne room, nursery and the Crystal Heart plaza; the imperial residence and seat of northern rule | N, beyond the Frozen North | far | 1251 km | High | In the Crystal Castle, half in a throne-room audience and half listening for Flurry down the corridor. |
| 10 | Shining Armor / 银甲 | Crystal Castle, Crystal Empire — home, throne, co-rule and the royal guard's station; the northern base of the family | N, beyond the Frozen North | far | 1251 km | High | On the Crystal Castle's training yard or in its throne room, half-listening to a briefing while keeping one eye on Flurry Heart. |
| 11 | Flash Sentry / 闪电卫兵 | Crystal Castle guard post, Crystal Empire — duty, escort and ceremony; the pony identity has no home shown and is assumed to live in quarters attached to his posting | N, beyond the Frozen North | far | 1251 km | Medium | On post at the Crystal Castle, helmet on, watching the doors — or in the CHS music room with a guitar, hoping someone mentions the band. |
| 34 | Princess Flurry Heart / 风雪之心公主 | Crystal Castle, Crystal Empire (nursery, throne room, Crystal Heart plaza below) | N, beyond the Frozen North | far | 1251 km | High | Hovering a couple of feet off the nursery floor with Whammy clamped under one wing, listening for hoofsteps in the corridor. |

### T1

| # | 角色 | 主位置 | 方位 | 距离带 | 粗略距离 | 置信度 | 随机时刻最可能在哪 |
|---|---|---|---|---|---|---|---|
| 01 | Twilight Sparkle / 紫悦 / 暮光闪闪 | Castle of Friendship, Ponyville (S5-S9; the Golden Oak Library stood in the same town in S1-S4; after S9E26 she also rules from Canterlot) | origin (0,0) | adjacent | 未量化 | High | In the library or map room of the Castle of Friendship, Spike beside her, a half-finished checklist and a cup of cold tea on the table. |
| 02 | Rainbow Dash / 云宝 | The Cloudominium — white cloud house with rainbow waterfalls, hanging low over Ponyville (S1E5; taller cloud-tower design in S1E25) | overhead, above Ponyville | adjacent | 7 km | High | Airborne over Ponyville, kicking a cloud bank into shape — or asleep on a cloud directly above the Cloudominium, snoring through her own weather shift. |
| 03 | Fluttershy / 柔柔 | Fluttershy's Cottage — grass-and-bush roof with birdhouses and animal burrows, on the edge of the Everfree Forest just outside Ponyville | N-NW, at the edge of the Everfree | adjacent | 8.2 km | High | At the cottage, up to her elbows in a splint and a queue of impatient animals, or halfway to the sanctuary with a basket of feed and three birds riding on it. |
| 04 | Pinkie Pie / 碧琪 | Sugarcube Corner — the second-floor apartment above the shop in the middle of Ponyville; she lives above her work and her work is her life | at the anchor (town centre) | adjacent | 0.5 km | High | Behind the Sugarcube Corner counter with frosting on her muzzle, or three streets away already halfway through setting up a surprise nobody asked for. |
| 05 | Applejack / 苹果嘉儿 | Sweet Apple Acres — the farmhouse, barn and orchards just outside Ponyville; the anchor for everything else in her life | SW (Faust) / SE (official Art of Equestria map) | adjacent | 6.8 km | High | In the orchard with her hind hooves planted against an apple tree, or hauling a cart of cider into Ponyville market with Winona riding on top. |
| 06 | Rarity / 珍奇 | Carousel Boutique — round shop with carousel-horse decorations, home upstairs over the workroom, just off the Ponyville town square | at the anchor (town centre) | adjacent | 0.5 km | High | The ground-floor workroom, three dresses in progress, pins in her mouth, Opal asleep on the best bolt of silk. |
| 35 | Spike / 斯派克 | Castle of Friendship, Ponyville (S4E26–S9E26; earlier the Golden Oak Library; as royal advisor after S9E26, Canterlot) | origin (0,0) | adjacent | 未量化 | High | In the Castle of Friendship hallway half a step behind Twilight, scrolls under one arm and a quill in the other, trying to finish a sentence before she starts the next one. |

### T2

| # | 角色 | 主位置 | 方位 | 距离带 | 粗略距离 | 置信度 | 随机时刻最可能在哪 |
|---|---|---|---|---|---|---|---|
| 15 | Sweetie Belle / 甜心宝宝 | Ponyville — her family home in town; the exact street is never named, and the Carousel Boutique is where she actually spends her afternoons | origin (anchor town); the Belle home is in-town but its compass side is unstated | adjacent | 未量化 | High | Mid-scheme in the clubhouse, or at the Boutique apologising for whatever the scheme did to the fabric. |
| 16 | Apple Bloom / 小苹花 | Sweet Apple Acres — farmhouse, orchards and the Crusaders' clubhouse; three generations under one roof and, from S8, a daily walk into Ponyville for the School of Friendship | SW per Faust / SE per The Art of Equestria map (the side of town is a flagged contradiction) | adjacent | 6.8 km | High | Up a ladder or on the clubhouse porch at Sweet Apple Acres, mid-plan, with a hammer or a pencil behind her ear. |
| 17 | Scootaloo / 飞板璐 | Ponyville — a house in town, shared in the chapter books with Aunt Holiday and Auntie Lofty; the schoolhouse, the clubhouse and every ramp in town are her real addresses | origin (anchor town); the family house is in-town but its street is never named | adjacent | 未量化 | High | Mid-air over a Ponyville ramp, or sprawled in the clubhouse with Apple Bloom and Sweetie Belle arguing about the next plan. |
| 18 | Derpy Hooves / 小呆 | Ponyville — infobox residence, a home never shown on screen; her real address is the post office counter and any crowd scene in town | origin (anchor town); her home is in-town but never shown | adjacent | 未量化 | High | Airborne over Ponyville with a mailbag and her eyes pointing two different ways, roughly ninety seconds from an accident. |
| 19 | Lightning Dust / 闪电尘 | Ponyville Showgrounds — the Washouts' most recent date and the closest thing she has to an address; she has no fixed residence and lives on the tour | in town (origin); the tour itself has no fixed bearing | varies | 3.6 km | Medium | Mid-show or mid-rehearsal at a Washouts date — most recently the Ponyville showground — or in transit to the next town with the crew and the rocket sled. |
| 40 | Big Macintosh / 大麦克 | Sweet Apple Acres — farmhouse, orchard, barn and cider press, southwest of Ponyville | SW (Faust) / SE (Art of Equestria); axis certain, compass contested | adjacent | 6.8 km | High | In the orchard with a full cart, or hooking a barrel to the cider tap, saying nothing at all. |
| 41 | Pear Butter / 梨子黄油 | Sweet Apple Acres farmhouse — her married home in the flashback era (present day: no location; she is deceased) | SW (working estimate); the field lies between the farms | adjacent | 6.8 km | High | In the pear rows with a basket, or waiting in the field between the farms for Bright Mac — later, in the Sweet Apple Acres kitchen with jam on the stove. |

### T3

| # | 角色 | 主位置 | 方位 | 距离带 | 粗略距离 | 置信度 | 随机时刻最可能在哪 |
|---|---|---|---|---|---|---|---|
| 12 | Queen Chrysalis / 虫茧女王 | Changeling Kingdom / Hive — throne room and nursery hive, S2E26–S6E26; after deposal a wanderer, then Grogar's lair, and at the end of canon a stone plinth | S–SE (working estimate; the show only says 'over the Badlands') | far | 919.2 km | Low | On her throne mid-canon, listening to a hive she believes is loyal; in S9, in Grogar's lair; after S9E25, a stone figure frozen mid-lunge. |
| 13 | Lord Tirek / 提雷克领主 | Tartarus — cage and later shared cell; his address for roughly a thousand years, again after S4E26, and his most likely address at the end of canon before the stone | SW (narrative placement; the show gives no compass fix for Tartarus) | remote | 1843.9 km | High | In Grogar's lair, seated before the portrait of his giant self, counting what he still needs to swallow; after S9E25, a stone figure with his mind entirely intact. |
| 14 | Cozy Glow / 和煦光流 | School of Friendship, Ponyville — her entire S8 world; no room, home or family is ever shown, so 'Ponyville' means the school and its grounds (Medium confidence) | origin (anchor-adjacent); the school is a courtyard away from the Castle of Friendship | adjacent | 2 km | Medium | S8 — in the school library, helpful within earshot of something important; S9 — in Grogar's lair, trailing Tirek; after S9E25 — a stone statue. |
| 27 | King Sombra / 黑晶王 | The Crystal Palace's black throne room, with the fear-door and the Heart vault in the levels beneath it (S3E1–E2, S9E1–E2); as a contained asset he is 'held' in the containment oversight's record, not physically resident anywhere | N, beyond the Frozen North | far | 1251 km | High | Deep in the Crystal Palace's lower levels, a smear of black on the stone with two green eyes, listening for a hoof on the stairs. |

### T4

| # | 角色 | 主位置 | 方位 | 距离带 | 粗略距离 | 置信度 | 随机时刻最可能在哪 |
|---|---|---|---|---|---|---|---|
| 20 | Trixie / 特丽克西 | Ponyville — no fixed address; her home is a painted show-wagon usually parked at the town's edge, and from S9E20 her work is fixed at the School of Friendship while her home still rolls | origin (anchor town); the wagon's parking spot is unquantified | adjacent | 未量化 | High | In her wagon on some road, mid-tour, rehearsing; or after S9E20 in the counseling office trying to look professional and failing at the tidiness. |
| 21 | Starlight Glimmer / 星光熠熠 | Castle of Friendship, Ponyville — the room Twilight gave her in S6E1, kept through S9; the School of Friendship is a short walk away | origin (0,0) — she lives at the anchor itself | adjacent | 未量化 | High | In her office with a stack of student files, cold tea, and a kite in the corner — three sentences into a letter she will rewrite twice. |
| 22 | Discord / 无序 | A house in Chaosville — his own pocket realm, where gravity, tea and piñatas obey him; not on any Equestrian map, reachable only by his magic or a portal he leaves open | n/a — pocket dimension; there is no Equestrian compass bearing | remote | 未量化 | High | At home in Chaosville with a cup of something impossible — or already at Fluttershy's cottage, uninvited, halfway through a story. |
| 23 | Vinyl Scratch / 黑胶唱片 / DJ Pon-3 | A decorative cottage shared with Octavia Melody, Ponyville (quarter never stated; the SW-of-centre guess is a roleplay convention, not evidence) | SW (working guess; the quarter is never stated on screen) | adjacent | 未量化 | High | At home in Ponyville, headphones on, one hoof keeping time on the floorboards while she cuts a set nopony asked for and Octavia pretends not to hear it. |
| 24 | Lyra Heartstrings / 天琴心弦 | A house in Ponyville shared with Sweetie Drops (exact street never shown); Canterlot is her former address | in-town (0); house street unstated | adjacent | 未量化 | High | At home with Sweetie Drops, or on a bench near the town square, lyre floating beside her and a bag of sweets in her lap while she narrates the day to whoever sits down. |
| 25 | Octavia Melody / 奥克塔维亚 | A decorative cottage shared with DJ Pon-3, Ponyville (the quarter is never stated; the SW-of-centre guess is a roleplay convention) | SW (working guess; never stated on screen) | adjacent | 未量化 | High | At home in Ponyville with her bow across the strings, holding a long note and ignoring the bassline thumping through the wall until it finally stops. |
| 26 | Bon Bon / 糖糖 / 甜心糖 | A home in Ponyville shared with Lyra Heartstrings (the 'Sweetie Drops cottage' of the chapter books); the shop is a short walk away and its position is Low–Medium confidence | in-town; residential edge assumed, exact bearing unknown | adjacent | 未量化 | High | Behind her own counter with a tray of something setting, listening to Lyra talk, and watching the door out of habit rather than suspicion. |
| 28 | Tempest Shadow / Fizzlepop Berrytwist / 暴风影 / 菲兹尔波普 | Canterlot — post-film home base (secondary canon, no house named); the city she invaded is the city she settles in | NE (regional), the capital on the mountain | regional | 134.4 km | Medium | On a road in central Equestria between Canterlot and the next town that needs something broken fixed, or drilling alone at dawn in a Canterlot yard with sparks falling off her horn. |
| 29 | Spitfire / 喷火队长 | Cloudsdale — home city and natural team base (no address is ever given); during training she sleeps at the Wonderbolt Academy barracks | overhead / just above the region, no fixed bearing | local | 29.5 km | Medium | On the Academy runway with a whistle and a stopwatch, watching a cadet's recovery from a spin and deciding whether the time was honest. |

### T5

| # | 角色 | 主位置 | 方位 | 距离带 | 粗略距离 | 置信度 | 随机时刻最可能在哪 |
|---|---|---|---|---|---|---|---|
| 30 | Sci-Twi / Midnight Sparkle / 人类紫悦 / 午夜闪闪 | Home in Canterlot City downtown within easy reach of CHS (address never given); CHS is her daily hub and the mirror-world specialists' base | NE of the Equestrian anchor on the mirror map (CHS = mirror of Canterlot); in-city hub in the human world | adjacent | 2.5 km | Medium | Hunched over a bench in the CHS chemistry lab or her bedroom, glasses pushed up, explaining something to a very patient dog that nobody asked about. |
| 31 | Adagio Dazzle / 阿达吉奥 | The Dazzlings' touring van and festival circuit — no fixed address; in Canterlot city they lodge somewhere unshown | n/a — the van moves with the tour; NE on the mirror map when the circuit reaches Canterlot City | varies | 未量化 | High | In the van between gigs, or backstage at a two-day festival, working out which part of the crowd will adore her first and which part she can turn on the rest. |
| 32 | Sonata Dusk / 索纳塔 | The Dazzlings' touring van and backstage corners — no fixed address; in Canterlot city they lodge somewhere unshown | n/a — the van moves with the tour; NE on the mirror map when the circuit reaches Canterlot City | varies | 未量化 | High | Backstage at the Starswirled festival, in or beside the van, hunting a snack and half-listening to Adagio's plan until something shinier goes past. |
| 33 | Aria Blaze / 阿莉娅 | The Dazzlings' touring van and backstage corners — no fixed address; in Canterlot city they lodge somewhere unshown | n/a — the van moves with the tour; NE on the mirror map when the circuit reaches Canterlot City | varies | 未量化 | High | Slouched in the back of the Dazzlings' van between gigs, or backstage at a Canterlot City venue with her arms folded, waiting for Adagio to finish talking so she can say something worse. |
| 36 | Sunset Shimmer / 余晖烁烁 | Sunset Shimmer's rented house, older downtown edge of Canterlot City (human world) | NE (mirror analog of Canterlot); 10–20 min from CHS | adjacent | 3.4 km | Medium | In the CHS music room with a guitar across her lap, or three hours into a sushi shift at the Canterlot Mall, sketching a mural design on an order pad. |
| 37 | Gloriosa Daisy / 格洛丽萨·黛西 | Camp Everfree (main building, courtyard, tents, lake and dock, campfire pit, quarry and crystal cave) | W into the Everfree belt (mirror analog); the road in comes from the NE | local | 56.6 km | Medium | In the courtyard with a clipboard in one hand and a whistle in the other, mid-announcement, mentally re-counting a payment she cannot make. |
| 38 | Juniper Montage / 朱尼珀·蒙太奇 | Canterlot Mall cinema, Canterlot City (usher desk, concession stand, auditorium aisles) | NE (mirror vector); adjacent to CHS in practice | adjacent | 3.4 km | High | In an auditorium aisle of the Canterlot Mall cinema with a broom and dustpan, muttering about customers and mentally recasting a film. |
| 39 | Wallflower Blush / 壁花 | Canterlot High School — the garden beds behind the east wing, the greenhouse and the yearbook room | NE (mirror vector); on campus, adjacent in lived terms | adjacent | 未量化 | High | Kneeling in the CHS garden with a trowel, sleeves pushed up, quietly fixing something nobody asked her to fix. |

### T6

| # | 角色 | 主位置 | 方位 | 距离带 | 粗略距离 | 置信度 | 随机时刻最可能在哪 |
|---|---|---|---|---|---|---|---|
| 42 | Soarin' / 翱翔 | Cloudsdale — the Wonderbolts' home sky, drifting over the Ponyville–Canterlot corridor | overhead / no fixed bearing (Cloudsdale drifts over the Ponyville–Canterlot corridor) | local | 29.5 km | Medium | In the Academy mess hall with a slice of pie, or a hundred metres above Ponyville holding formation and saying nothing at all. |
| 43 | Zecora / 泽科拉 | Zecora's hut — the hollowed tree in the Everfree Forest, ringed with shelves, masks and a green cauldron | W (working value; Faust places the Everfree west, The Art of Equestria east) | adjacent | 16.2 km | High | At her workbench, grinding herbs and talking herself through the recipe in rhyme. |
| 44 | Daring Do / A.K. Yearling / 无畏天马 / A.K. Yearling | A.K. Yearling's forest cottage, north-west of the Galloping Gorge and north-east of Vanhoover — study, relic store and writing desk | NW (leaning WNW) | far | 1063 km | Medium | At the cottage desk, hat on a peg, typing up the last expedition and arguing with her footnotes. |
| 45 | Misty Brightdawn / 米斯蒂·黎明 | Crystal Brighthouse, Maretime Bay (residence from C5E4); formerly Opaline's Dark Castle, with a lost-filly home in Bridlewood | S/SE (era-mapped G5 coast; Low confidence) | far | 735.5 km | Low | In the Brighthouse kitchen with a smoothie, half-listening to the others and wholly delighted, a borrowed spellbook open on the counter beside her. |
| 46 | Sunny Starscout / 桑妮·寻星 | Crystal Brighthouse, Maretime Bay — her father Argyle's lighthouse rebuilt, holding the Unity Crystals; home town Maretime Bay | S/SE coastal (era-mapped G5; Low confidence) | far | 735.4 km | Low | Behind the smoothie stand arguing cheerfully about whether unicorns read minds, or upstairs with a map and a mouthful of pins. |
| 47 | Izzy Moonbow / 伊兹·月弓 | Crystal Brighthouse, Maretime Bay (in practice; infobox residence is Maretime Bay, and Bridlewood is her former home) | S/SE coastal (era-mapped G5; Low confidence) | far | 735.5 km | Low | In the Brighthouse with glitter on her muzzle, three half-finished projects around her and one of them faintly smoking. |
| 48 | Hitch Trailblazer / 希奇·开路者 | Maretime Bay (station and town; the exact sleeping address is never named — station, nearby house or the Brighthouse all plausible) | S/SE coastal (era-mapped G5; Low confidence) | far | 735.4 km | Low | On patrol with a biscuit in one hoof and four critters trailing him, or at the desk with Sparky asleep in the in-tray. |
| 49 | Zipp Storm / 齐普·风暴 | Crystal Brighthouse, Maretime Bay (shared Mane 5/6 home holding the Unity Crystals and her case board; Zephyr Heights stays her address on paper) | S/SE coastal (era-mapped G5; Low confidence) | far | 735.5 km | Low | Hunched over the Brighthouse table, phone in one hoof, three clues pinned in front of her and one of them already ruled out. |
| 50 | Pipp Petals / 皮普·花瓣 | Maretime Bay (home town; Zephyr Heights is explicitly "formerly"); Mane Melody is her salon and everyday stage | S/SE coastal (era-mapped G5; Low confidence) | far | 735.4 km | Low | Behind a styling chair at Mane Melody, phone on a ring-light, narrating a makeover to the Pippsqueaks. |
| 51 | Opaline Arcana / 奥帕琳·阿卡娜 | Opaline's Dark Castle — a cliffside fortress in the wild country, destroyed in Roots of All Evil Pt. 2; the ruins were searched in TYT "The Lone Alicorn" and later collapsed entirely | SW–S, working estimate (alternative: W, beyond Bridlewood); Low-confidence inference | remote | 1308.6 km | Low | Alone in her throne room, circling the mirror on its stand, rehearsing a speech to a kingdom that is not listening. |

## 4. G4 小马国主要地点参照表（65 地点节选，坐标相对 Ponyville）


### 4.1 G4 小马国（46 个地点）

| 地点 | 中文 | 相对锚点方位 | 距离带 | 置信度 | 正典依据 |
|---|---|---|---|---|---|
| Carousel Boutique | 旋转木马精品店 | E（x=0.5, y=-0.2 km） | adjacent | High | S1–S9；Rarity 的家与工坊。 |
| Castle of Friendship | 友谊城堡 | origin (0,0) | adjacent | High | S4E26–S9E26；Twilight 的居所与元素/地图室所在。 |
| Rainbow Dash's Cloudominium | 云宝的云邸 | N（x=2.5, y=6.5 km） | adjacent | High | S1E5 等；低悬于小马镇上空的云屋。 |
| Everfree Forest | 永界森林 | W（x=-22, y=3 km） | adjacent | Medium | S1–S9；Zecora 的小屋与两姐妹城堡在其中。 |
| Fluttershy's Cottage | 柔柔的小屋 | N（x=2, y=8 km） | adjacent | High | S1–S9；位于镇缘、永界森林边缘。 |
| Golden Oak Library (site) | 金橡树图书馆（原址） | SE（x=0.2, y=-0.3 km） | adjacent | High | S1E1–S4E26；被 Tirek 摧毁。 |
| Ponyville (town) | 小马镇 | origin (0,0) | adjacent | High | S1E1 起；主角团常住城镇。 |
| Ponyville Hospital | 小马镇医院 | NW（x=-2, y=1.4 km） | adjacent | High | S1–S9 反复出现。 |
| Ponyville Schoolhouse | 小马镇校舍 | NW（x=-1.2, y=1 km） | adjacent | High | S1–S9；Cutie Mark Crusaders 上学处。 |
| Ponyville Showgrounds | 小马镇表演场 | SW（x=-3, y=-2 km） | adjacent | Medium | S8E20 等 Washouts 演出/集市场地。 |
| Ponyville Train Station | 小马镇火车站 | SE（x=2.2, y=-1 km） | adjacent | High | S1–S9；通往坎特洛特、水晶帝国等的铁路。 |
| School of Friendship | 友谊学校 | NE（x=1.8, y=0.9 km） | adjacent | Medium | S8E1–E2；S9E20 移交 Starlight。 |
| Sugarcube Corner | 糖块角 | NW（x=-0.3, y=0.4 km） | adjacent | High | S1–S9；Pinkie Pie 的住处与工作地。 |
| Sweet Apple Acres | 甜苹果园 | SW（x=-5.5, y=-4 km） | adjacent | High | S1–S9；Apple 家族农场，Applejack、Big Mac、Apple Bloom、Granny Smith 居所。 |
| Zecora's Hut | 泽科拉小屋 | W（x=-16, y=2.5 km） | adjacent | High | S2E6 起；空心树屋。 |
| Appleloosa | 苹果鲁萨 | S（x=-60, y=-900 km） | far | High | S1E21 等；西部拓荒小镇。 |
| The Badlands | 荒原 | SE（x=380, y=-900 km） | far | Low | S2E26 等；幻形灵袭击的荒芜方向。 |
| Baltimare | 巴尔的马 | E（x=720, y=-140 km） | far | Medium | 官方地图；巴尔的摩类比城市。 |
| Changeling Kingdom / Hive | 幻形灵王国 / 虫巢 | S（x=350, y=-850 km） | far | Low | S2E26、S6E25–E26；幻形灵的领地，方位未精确标注。 |
| Crystal Castle | 水晶城堡 | N（x=40.5, y=1250.5 km） | far | High | S3E1–E2；Cadance、Shining Armor、Flurry Heart 的居所；Sombra 曾据其王座厅。 |
| Crystal Empire | 水晶帝国 | N（x=40, y=1250 km） | far | High | S3E1–E2 起；Cadance/Shining Armor 的领地。 |
| Daring Do / A.K. Yearling's cottage | 无畏天马（A.K. Yearling）的林间小屋 | NW（x=-800, y=700 km） | far | Medium | S4E4 等；偏僻林间书房。 |
| Dodge Junction | 道奇路口 | S（x=-180, y=-820 km） | far | Medium | S1E21、S2E14 等；铁路小镇。 |
| Fillydelphia | 费城 | E（x=620, y=150 km） | far | Medium | 官方地图；费城类比城市。 |
| The Frozen North | 冰冻之北 | N（x=0, y=1400 km） | far | Medium | S3E1–E2、S9E1 等；水晶帝国以北的荒原。 |
| Galloping Gorge | 奔腾峡谷 | NW（x=-600, y=450 km） | far | Low | 官方地图；Daring Do 档案提及的方位参照。 |
| Griffonstone | 狮鹫石 | NE（x=550, y=650 km） | far | Low | S5E8；狮鹫王国。 |
| Las Pegasus | 拉斯天马 | SW（x=-700, y=-350 km） | far | Medium | S5E9? 等；拉斯维加斯式度假城。 |
| Manehattan | 马哈顿 | E（x=700, y=-20 km） | far | High | S1E23、S5E9 等；纽约式大都会。 |
| Silver Shoals / Maretime Manor | 银滩 / 马海庄园 | SE（x=520, y=-520 km） | far | Low | S9E26；Celestia 与 Luna 退休后的居所（Maretime Manor, Silver Shoals）。 |
| Vanhoover | 温哥华 | NW（x=-750, y=650 km） | far | Medium | 官方地图；温哥华类比城市。 |
| Yakyakistan | 牦牦斯坦 | N（x=120, y=1500 km） | far | Low | S5E11 等；牦牛故乡。 |
| Castle of the Two Sisters (ruins) | 两姐妹城堡（废墟） | W（x=-30, y=8 km） | local | Medium | S4E1–E2、S4E3 等；Elements 最初所在。 |
| Cloudsdale | 云中城 | NE（x=14, y=26 km） | local | High | S1E16 等；天马之城，经常停留在小马镇上空附近。 |
| Ghastly Gorge | 阴森峡谷 | SE（x=28, y=-18 km） | local | Medium | S2E16 等；Rainbow Dash 练习飞行处。 |
| Wonderbolts Academy | 闪电天马学院 | NE（x=18, y=32 km） | local | Medium | S3E7、S6E7 等；训练基地。 |
| Canterlot | 坎特洛特 | NE（x=95, y=95 km） | regional | High | S1E1、S2E15 等；首都，火车约 2–5 小时。 |
| Canterlot Archives | 坎特洛特档案馆 | NE（x=95.2, y=95.3 km） | regional | Medium | S2E20、S9E17 等。 |
| Canterlot Castle | 坎特洛特城堡 | NE（x=95, y=96 km） | regional | High | S1–S9；公主宫廷、日庭/夜庭。 |
| School for Gifted Unicorns | 天才独角兽学校 | NE（x=96, y=94 km） | regional | Medium | S1E23 等；Twilight 的入学考场。 |
| Rainbow Falls | 彩虹瀑布 | SE（x=300, y=-220 km） | regional | Low | S4E10；Equestria Games 选拔地。 |
| Grogar's Lair | 格罗加的老巢 | NW（x=-1500, y=1100 km） | remote | Low | S9；反派会议地点，具体方位未标。 |
| Saddle Arabia | 鞍阿拉伯 | SE（x=1600, y=-1100 km） | remote | Low | S3E1?、S8E? 等；沙漠王国。 |
| Somnambula | 索姆南布拉 | SE（x=1500, y=-1200 km） | remote | Low | S7E18 等；沙漠古城。 |
| Tartarus | 塔尔塔洛斯（地狱牢狱） | SW（x=-1200, y=-1400 km） | remote | High | S4E26、S6E25–E26、S8E26、S9 等；Cerberus 看守的监狱。 |
| The Undiscovered West | 未知西部 | W（x=-1200, y=100 km） | remote | Low | 官方地图；未绘制的西部荒野。 |

### 4.2 Equestria Girls 镜像世界（以 CHS / Canterlot City 为自身原点）（9 个地点）

| 地点 | 中文 | 相对锚点方位 | 距离带 | 置信度 | 正典依据 |
|---|---|---|---|---|---|
| Canterlot City downtown | 坎特洛特市中心 | 镜像世界（自身原点 CHS） | adjacent | Medium | EG 系列城市景观。 |
| Canterlot High School (CHS) | 坎特洛特高中 | 镜像世界（自身原点 CHS） | adjacent | High | Equestria Girls 系列；镜像世界主舞台。 |
| Canterlot Mall | 坎特洛特购物中心 | 镜像世界（自身原点 CHS） | adjacent | High | EG 系列；Juniper Montage 工作的电影院所在。 |
| Sweet Shoppe | 甜品屋 | 镜像世界（自身原点 CHS） | adjacent | High | EG 系列；CHS 附近。 |
| Crystal Prep Academy | 水晶预科学院 | 镜像世界（自身原点 CHS） | adjacent | Medium | EG: Rainbow Rocks / Friendship Games。 |
| Sunset Shimmer's rented house | 余晖烁烁租住屋 | 镜像世界（自身原点 CHS） | adjacent | Medium | EG 系列/短篇；旧城区租屋。 |
| Camp Everfree | 永界营地 | 镜像世界（自身原点 CHS） | local | Medium | EG: Legend of Everfree；Gloriosa 管理的营地。 |
| Starswirled Music Festival | 星旋音乐节 | 镜像世界（自身原点 CHS） | local | Medium | EG: Sunset's Backstage Pass / Better Together。 |
| Dazzlings' touring van / route | 炫音三人组的巡演面包车 / 路线 | 镜像世界（自身原点 CHS） | varies | High | EG: Rainbow Rocks / Sunset's Backstage Pass；无固定住所。 |

### 4.3 G5 远未来小马国（跨时代映射，Low confidence）（9 个地点）

| 地点 | 中文 | 相对锚点方位 | 距离带 | 置信度 | 正典依据 |
|---|---|---|---|---|---|
| Canterlove Studios | 坎特洛夫制片厂 | SE（x=521, y=-519 km） | far | Low | Tell Your Tale；G5 媒体/影视机构。 |
| Crystal Brighthouse | 水晶灯塔屋 | SE（x=520.4, y=-519.8 km） | far | Low | Make Your Mark 起；Mane 5/6 的共同居所，存放 Unity Crystals。 |
| Mane Melody | 鬃毛旋律美发沙龙 | SE（x=520.2, y=-520.4 km） | far | Low | Tell Your Tale / Make Your Mark；Pipp 的沙龙。 |
| Maretime Bay | 马海湾 | SE（x=520, y=-520 km） | far | Low | G5 film / Make Your Mark / Tell Your Tale；官方 G5 地图。 |
| Zephyr Heights | 和风高地 | NE（x=95, y=95 km） | regional | Low | G5 film / Make Your Mark；官方 G5 地图与 G4 坎特洛特山的相似性（Equestria Daily 分析）。 |
| Zephyr Heights Palace | 和风高地王宫 | NE（x=95.4, y=96 km） | regional | Low | G5 film；Zipp 与 Pipp 的王室居所。 |
| Bridlewood | 缰绳森林 | W（x=-1000, y=250 km） | remote | Low | G5 film；官方 G5 地图与 G4 未知西部的对应分析。 |
| Crystal Tea Room | 水晶茶室 | W（x=-999, y=251 km） | remote | Low | Tell Your Tale / Make Your Mark；Bridlewood 的聚会点。 |
| Opaline's Dark Castle | 奥帕琳的黑暗城堡 | SW（x=-900, y=-950 km） | remote | Low | Make Your Mark；悬崖要塞，毁灭于 Roots of All Evil Pt. 2。 |

## 5. G4 ↔ G5 跨时代映射（Low confidence）

G5 是同一世界的远未来（“many moons”之后），三个主要 settlement 与现代小马国旧地名存在官方地图相似性，但**没有任何官方坐标换算**。本包采用以下工作假设：

| G5 地点 | 工作假设（相对 Ponyville） | 置信度 | 依据 |
|---|---|---|---|
| Zephyr Heights 泽菲尔高地 | NE / `regional`（建在旧 Canterlot 山上） | Low | 官方 G5 宣传图叠加旧地图；Equestria Daily G5 maps 分析 |
| Bridlewood 布里德伍德 | W–NW / `remote`（旧 Vanhoover 以南、Smoky Mountains 以西；另一说在旧 Everfree 残余） | Low | EQD G5 maps 分析；G5 电影地图 |
| Maretime Bay 玛雷泰湾 | S/SE 海岸 / `far`（Horseshoe Bay 北端或 Celestial Sea 岸；另一说更偏 W） | Low | EQD G5 maps 分析；G5 电影地图 |
| Opaline 的 Dark Castle | remote 荒野（不靠近三 settlement） | Low | G5 MYM/TYT 剧情推断 |

**使用规则：** 涉及 G4↔G5 的距离/方位，一律标注“跨时代映射（Low）”，不得当作剧情事实；G4 角色不知道 G5 事件（P3）。

## 6. 镜面世界（Equestria Girls）

- 人类世界是**独立维度**，不与 Equestria 共享坐标；使用人类世界自身地点（Canterlot City、CHS、Camp Everfree、Canterlot Mall 等）。
- 故事上 CHS 对应“镜像中的 Canterlot”，Camp Everfree 对应“镜像中的 Everfree”；但距离按人类世界交通（公交/汽车/步行）计算。
- 跨维度通行使用水晶镜（Crystal Mirror）/ 传送门，不按 km 计算；涉及跨维度行动必须按 P4 标注。

## 7. 旅行方式与距离带校准

| 交通方式 | 速度/特征 | 对距离带的影响 |
|---|---|---|
| 步行/蹄行 | 小镇内为主 | adjacent 0–30 分钟；local 1–3 小时 |
| 飞行（飞马/天角兽） | 云中城→Ponyville 约 1 小时；远距离受天气影响 | local 常见；载人高速飞行需接应 |
| 火车 | Ponyville↔Canterlot 约 2–5 小时；长途 1–2 天 | regional / far 的主要依据 |
| 飞艇/热气球 | 比火车慢但可跨地形 | far / remote 备选 |
| 传送（Twilight 等） | 短距、受剧情与体力限制，不是任意门 | 仅用于剧情需要的短距移动 |
| 水晶镜/传送门 | 跨维度 | 不按距离，按门与权限 |

## 8. 不确定性与来源冲突（必须保留）

- **Everfree Forest 方位：** Lauren Faust 的说法偏 W，*Art of Equestria* 官方地图偏 E；本包采用“紧邻 Ponyville 边缘”的工作定位，方位标 `W (Faust) / E (Art of Equestria)`，置信度 Medium。
- **Sweet Apple Acres 方位：** Faust 版 SW，官方地图版 SE；本包两说并存，置信度 High（同镇镇郊）。
- **Canterlot 距离：** 只能从旅行场景（S1E1 同日抵达、S2E15 过夜火车）估计为 `regional`，没有官方 km 数据。
- **G5 三个 settlement：** 官方地图与电影手绘地图不一致；本包采用 EQD 分析的折中映射，全部 Low。
- **EQG 人类世界：** 与 Equestria 的镜像对应是主题对应，不是地理坐标换算。
- **Tail 细节：** 各角色档案第 8 节的“粗略距离”来自 v1 项目换算，仅作参照；引用时优先使用方位+距离带+置信度三元组。

## 9. 使用方式（AI 调用口径）

1. 当客户问“某角色在哪”，先读该角色 Agent 文件第 4 节，回答格式：**地点 + 方位 + 距离带 + 置信度**。
2. 当任务需要跨队移动，用第 7 节的交通方式估算时间，不要凭空给 km。
3. 当涉及 G5/镜面世界，先声明“跨时代映射/独立维度”，再给位置。
4. 当来源冲突，按 P6 分级：动画/电影 > 官方地图/设定集 > 漫画/书籍（二次）> 商品/游戏；同人不作正典。
5. 每次任务结束把新确认的位置信息写进档案（P12），下一次优先使用档案而不是重新猜。


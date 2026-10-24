# 05 · Multi-Site Source Ledger and Verification Record (Research Ledger)

> This file records the research scope, site list, actual fetch results, fact cross-checking method and limitations of `mlp-ponies-agent-team/en`.
> **Principle: better to mark "low confidence / unverified" than to invent a source.**
> Recorded: 2026-10-23 (v1 corpus fetch) -> 2026-10-24 (multi-site cross-check and rewrite added in this package). Raw-evidence location: the `research/` folder of the source Chinese edition (`mlp-ponies-agent-team/zh-cn/research/`); the raw-evidence folder is not shipped with this English edition.

---

## 1. Research Goals and Method

This project answers three kinds of questions:

1. **Character facts (Who):** the identity, appearance, personality, abilities, plot, relationships, quotes and knowledge boundaries of the 70 characters.
2. **Geographic facts (Where):** each character's common locations; bearings and distance bands estimated from the T1 / Ponyville origin.
3. **Era and canon boundaries (When / what counts):** the differences between G4, G4-EQG and G5; which sources count as canon and which are secondary or reference only.

**Method:**

1. **Build the corpus first:** fetch the full texts of Fandom (English) character and geography pages, plus Wikipedia character-list and work-page source texts, to form the v1 corpus.
2. **Then build the profiles:** 51 English canon profiles (identity / personality / abilities / storyline / relationships / quotes / locations / roleplay guide / uncertainty / sources).
3. **This package adds multi-site cross-checks:** official sites, Equestria Daily (G5 map analysis), Bilibili (Equestria railway material), Chinese community sites
   (Baidu Baike / Moegirlpedia / Zhihu / Xiaohongshu — visible in search but fetch-limited, reference only), IMDb (restricted).
4. **Conflict handling:** grade under P6; when several sources on the same topic disagree, use "animation > official maps/art books > secondary canon > merchandise/games > fan work".
5. **Evidence on disk:** downloads are stored in `research/raw_extra/` and the fetch log at `research/raw_extra/_fetch_log.tsv`, both retained in the source Chinese edition; the raw-evidence folder is not shipped with this English edition.

---

## 2. Site List (Graded by Reliability)

| Tier | Site | Example URL | Use in this project | Reachability this round |
|---|---|---|---|---|
| T1 Official | Hasbro / official My Little Pony site | https://mylittlepony.hasbro.com/en-us | Official product/era information, official G5 positioning | ✅ Reachable (redirects to the global support page; limited content) |
| T1 Official | The official G5 film/series themselves | (the works themselves; no web page needed) | Highest authority for plot and character facts | ✅ The works are authoritative (profiles cite episode/movie names) |
| T2 Encyclopaedic | Fandom — My Little Pony Wiki (English) | https://mlp.fandom.com/wiki/Twilight_Sparkle | 51 character pages + six geography pages (Ponyville / Canterlot / Cloudsdale / Crystal Empire / Everfree / Equestria) | ⚠️ Direct connection timed out this round; **the full texts were fetched on 2026-10-23 into the v1 corpus** (`../mlp_agents/_sources/`) |
| T2 Encyclopaedic | Wikipedia (English) | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | Character list and work pages, cross-check | ⚠️ Direct connection timed out this round; **3 texts were fetched in the v1 round** |
| T2 Encyclopaedic | Wikipedia (Chinese) | https://zh.wikipedia.org/wiki/%E5%B0%8F%E9%A9%AC%E5%AE%9D%E8%8E%89 | Chinese name translations / overview reference | ⚠️ Direct connection timed out this round (not relied upon) |
| T3 Chinese community | Baidu Baike | https://baike.baidu.com/item/%E7%B4%AB%E6%82%A6 etc. | Chinese name translations, character introductions | ❌ 403 (anti-scraping); search records kept only, **not used as a basis for facts** |
| T3 Chinese community | Moegirlpedia | https://zh.moegirl.org.cn/My_Little_Pony | Chinese-community translations / memes | ❌ 403 |
| T3 Chinese community | Bilibili columns | https://www.bilibili.com/opus/88954394813179970 | Equestria railway lines and town connections (usable as a plausibility reference for geography) | ✅ Downloaded (raw files retained in the source Chinese edition: `research/raw_extra/bilibili_rail.*`) |
| T3 Chinese community | Zhihu / Xiaohongshu | https://zhuanlan.zhihu.com/p/108511604 etc. | Chinese material index (travel guides / character introductions) | 🔎 Visible in search; not fetched page by page |
| T4 Fan media / analysis | Equestria Daily (EQD) | https://www.equestriadaily.com/2021/08/community-soapbox-g5-maps-gen-5-vs-gen.html | **Comparative analysis of the G5 maps against the G4 continent** (the key reference for this package's cross-era mapping) | ✅ Full text downloaded (2.0 MB; key passages extracted) |
| T4 Fan media / analysis | EquestriaCN | https://www.equestriacn.com/2021/08/the-new-poster-for-the-film-features-a-simplified-map-of-the-g5-world.html | Report on the simplified map in the G5 poster (visible in search) | 🔎 Visible in search; not fetched |
| T4 Fan media / analysis | Fimfiction / DeviantArt / Ponerpics | https://www.fimfiction.net/... / https://www.deviantart.com/... | G5 map discussion and fan place-name compilations | 🔎 Visible in search; **leads only, never canon** |
| T4 Film/TV reference | IMDb | https://www.imdb.com/title/tt1751105/ | Cast/crew and work information | ❌ Returns a 202 anti-scraping page (only 2 KB) |

> T1 = official; T2 = encyclopaedic; T3 = Chinese community / secondary compilation; T4 = fan media / analysis. **The lower the tier, the more it may only be used for indexing or corroboration.**

---

## 3. Actual Execution Record for This Round (2026-10-24)

### 3.1 Automated Fetching (`tools/fetch_extra_sources.py` -> `research/raw_extra/` in the source Chinese edition)

| Result | Count | Notes |
|---|---|---|
| ✅ Succeeded | 6 | Bilibili railway column, official Hasbro page, EQD G5 maps long-form article, EQD home page, two IMDb entries (anti-scraping pages only; not adopted) |
| ❌ 403 / timeout | 18 | 8 Baidu Baike pages, Moegirlpedia, 6 Fandom G5 pages, 4 Wikipedia pages — anti-scraping or network restrictions |

Fetch log: `research/raw_extra/_fetch_log.tsv` in the source Chinese edition (with HTTP status, byte count, sha256 prefix, elapsed time and final URL); the raw evidence is not shipped with this English edition.

### 3.2 v1 Corpus (fetched 2026-10-23; reused directly by this package)

| Corpus | Count | Location |
|---|---|---|
| Fandom character page full texts (including infoboxes) | 51 files, about 1.5 MB | `../mlp_agents/_sources/NN-<slug>.txt` |
| Fandom G4 geography pages | 6 files (Ponyville / Canterlot / Cloudsdale / Crystal Empire / Everfree / Equestria) | `../mlp_agents/_sources/_geo_*.txt` |
| Wikipedia texts | Character list + A New Generation + Make Your Mark, etc. | `../mlp_agents/_sources/_wiki_*.txt` |
| Character infobox compilation | `_infobox.json` (75 KB) | Same as above |
| v1 English canon profiles | 51 files (12-25 KB each) | `../mlp_agents/profiles/` |

### 3.3 Supplementary Search (web_search, 2026-10-24)

| Topic | Query (example) | Main hits | Adoption |
|---|---|---|---|
| Chinese name translations / character overviews | My Little Pony characters Twilight Sparkle Rainbow Dash Fluttershy Pinkie Pie Applejack Rarity | Baidu Baike, Xiaohongshu, Zhihu, WeChat public accounts | Name-translation corroboration only (body text not fetched) |
| G4 geography / bearings | My Little Pony Ponyville Canterlot Cloudsdale map bearing distance | Zhihu travel guides, Xiaohongshu panoramic maps, Bilibili | Bilibili downloaded; the rest are leads |
| G5 maps / locations | MLP G5 Maretime Bay Zephyr Heights Bridlewood map location | EQD, EquestriaCN, Fimfiction, DeviantArt, Ponerpics | EQD downloaded and extracted; Fimfiction/EquestriaCN are leads |
| G5 English maps | My Little Pony G5 Maretime Bay Zephyr Heights Bridlewood map locations | EQD, DeviantArt, Ponerpics | EQD is authoritative |

### 3.4 Key Extracts (EQD G5 map analysis; the source-text extract is retained in the source Chinese edition at `research/raw_extra/eqd_g5_maps.txt`)

- Zephyr Heights sits **on the mountain associated with G4 Canterlot** (official promotional art overlaid on the old map).
- Bridlewood lies **south of old Vanhoover and west of the Smoky Mountains** (in another version of the map it may lie in the remains of the old Everfree).
- Maretime Bay lies at **the northern end of Horseshoe Bay** (in another hand-drawn version it is further west, beside a sea that did not exist in the G4 era).
- Conclusion: the two G5 maps disagree, so any G4<->G5 conversion can only be a **Low confidence** working assumption.

### 3.5 Key Extracts (Bilibili railway material; retained in the source Chinese edition at `research/raw_extra/bilibili_rail.*`)

- Railway main lines: Canterlot <-> Griffonstone, Canterlot <-> Manehattan, Canterlot <-> Baltimare, Canterlot <-> Ponyville, etc.;
- Branch lines connect Appleloosa, Las Pegasus, White Tail Woods, Vanhoover, the Crystal Empire, Rainbow Falls, etc.;
- Use: to provide **plausibility and corroboration** for distance bands such as "Canterlot = regional / Appleloosa = far / Crystal Empire = far";
- Note: the article is a fan compilation (T3) and does not claim official data; this package uses it only as a consistency check, never as a source of precise distances.

---

## 4. Fact Cross-Check Matrix

| Fact category | Main source (T1/T2) | Cross-check sources | Conclusion / confidence |
|---|---|---|---|
| G4 character identity / personality / plot | The animation/films themselves + Fandom character pages | Wikipedia character lists, v1 profiles | High (explicit in the animation) |
| G4 character quotes | Fandom page quotes/wikitext (v1) | Animation episode codes | High (every quote carries an episode code) |
| G4 geography (Ponyville layout) | Animation + Fandom Ponyville | Wikipedia, the Art of Equestria map (secondary) | High (inside town) / Medium (bearings outside town) |
| G4 town bearings and distances | Animation travel scenes + official maps (secondary) | Bilibili railway material, Fandom geography pages | Medium (bearing) / Low-Medium (exact distances) |
| Everfree bearing | Faust's statement (W) | Art of Equestria (E) | Conflict retained: W/E two readings, Medium |
| Sweet Apple Acres bearing | Faust (SW) | Art of Equestria (SE) | Conflict retained: SW/SE two readings, High (same town) |
| Geography of the three G5 settlements | Official G5 maps/films | EQD analysis, EquestriaCN, Fandom G5 pages (v1 corpus includes A New Generation/MYM) | Low (cross-era mapping) |
| G5 character personality / plot | G5 films/MYM/TYT + Fandom G5 character pages (v1) | Wikipedia A New Generation/Make Your Mark | High (within the works) |
| Chinese translated names | Official Chinese dub / Chinese-community convention | Baidu Baike search, Fandom Chinese names (`name_cn` in the v1 cards) | Medium (several name versions exist; aliases retained) |
| Equestria Girls setting | EQG films/shorts + Fandom | Wikipedia | High (within the works) / Low (human-world geographic detail) |
| Voice cast / crew | Fandom infoboxes | IMDb (restricted) | Medium (not verified item by item; background only in profiles) |

---

## 5. Source Grading and Conflict-Handling Rules (Consistent with P6)

1. **Animation and films:** highest; what is shown on screen is treated as fact.
2. **Official maps / art books / creator statements:** second highest; when they conflict with the animation, the animation wins, and both readings are retained.
3. **Official comics/books:** secondary canon; any citation must say "secondary / per the comic".
4. **Merchandise / games / advertising:** third tier; corroboration only, never written into the canon narrative.
5. **Fan wikis / analysis / fan work:** indexing and inference only; inferences must be marked Low and must never be dressed up as fact.
6. **Conflict-handling template:** "Source A says X, source B says Y; this package adopts Z because ...; confidence = High/Medium/Low."

---

## 6. 51-Character Source Ledger

> Each character's **main source** (English Fandom page) + **cross-checks** (Wikipedia / geography pages / the works) + this package's review status.
> Full URLs are also written into section 8 of each `agents/NN-*.md`.

| # | Character | Team | Main source (Fandom EN) | Cross-checks / supplementary sources | Review status in this package |
|---|---|---|---|---|---|
| 01 | Twilight Sparkle | T1 | https://mlp.fandom.com/wiki/Twilight_Sparkle | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Ponyville · https://mlp.fandom.com/wiki/Canterlot | **Overall Lead candidate: priority re-check** |
| 02 | Rainbow Dash | T1 | https://mlp.fandom.com/wiki/Rainbow_Dash | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Wonderbolt_Academy · https://mlp.fandom.com/wiki/Sonic_Rainboom | v1 corpus inherited + rebuilt in this package |
| 03 | Fluttershy | T1 | https://mlp.fandom.com/wiki/Fluttershy | https://mlp.fandom.com/wiki/Fluttershy%27s_Cottage · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Fluttershy_Leans_In | v1 corpus inherited + rebuilt in this package |
| 04 | Pinkie Pie | T1 | https://mlp.fandom.com/wiki/Pinkie_Pie | https://mlp.fandom.com/wiki/Pie_family · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/The_Last_Laugh | v1 corpus inherited + rebuilt in this package |
| 05 | Applejack | T1 | https://mlp.fandom.com/wiki/Applejack | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://en.wikipedia.org/wiki/Applejack_(My_Little_Pony) · https://mlp.fandom.com/wiki/Applebuck_Season | v1 corpus inherited + rebuilt in this package |
| 06 | Rarity | T1 | https://mlp.fandom.com/wiki/Rarity | https://mlp.fandom.com/wiki/Carousel_Boutique · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Rarity_Takes_Manehattan | v1 corpus inherited + rebuilt in this package |
| 07 | Princess Celestia / Daybreaker | T0 | https://mlp.fandom.com/wiki/Princess_Celestia | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Canterlot · https://mlp.fandom.com/wiki/The_Last_Problem | **Overall Lead candidate: priority re-check** |
| 08 | Princess Luna / Nightmare Moon | T0 | https://mlp.fandom.com/wiki/Princess_Luna | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://en.wikiquote.org/wiki/My_Little_Pony:_Friendship_is_Magic_(season_1) · https://mlp.fandom.com/wiki/Luna_Eclipsed | **Overall Lead candidate: priority re-check** |
| 09 | Princess Cadance | T0 | https://mlp.fandom.com/wiki/Princess_Cadance | https://mlp.fandom.com/wiki/The_Crystalling_-_Part_1 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/A_Canterlot_Wedding_-_Part_1 | **Overall Lead candidate: priority re-check** |
| 10 | Shining Armor | T0 | https://mlp.fandom.com/wiki/Shining_Armor | https://mlp.fandom.com/wiki/A_Canterlot_Wedding_-_Part_1 · https://mlp.fandom.com/wiki/The_Crystal_Empire_-_Part_2 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | v1 corpus inherited + rebuilt in this package |
| 11 | Flash Sentry | T0 | https://mlp.fandom.com/wiki/Flash_Sentry | https://mlp.fandom.com/wiki/Flash_Sentry_(EG) · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestriagirls.fandom.com/wiki/Flash_Sentry | v1 corpus inherited + rebuilt in this package |
| 12 | Queen Chrysalis | T3 | https://mlp.fandom.com/wiki/Queen_Chrysalis | https://en.wikipedia.org/wiki/List_of_My_Little_Pony_characters · https://mlp.fandom.com/wiki/Transcripts/A_Canterlot_Wedding_-_Part_2 · https://mlp.fandom.com/wiki/Changeling_Kingdom | v1 corpus inherited + rebuilt in this package |
| 13 | Lord Tirek | T3 | https://mlp.fandom.com/wiki/Lord_Tirek | https://mlp.fandom.com/wiki/Transcripts/Twilight%27s_Kingdom_-_Part_1 · https://mlp.fandom.com/wiki/Transcripts/Twilight%27s_Kingdom_-_Part_2 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | v1 corpus inherited + rebuilt in this package |
| 14 | Cozy Glow | T3 | https://mlp.fandom.com/wiki/Cozy_Glow | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/School_Raze_-_Part_2 | v1 corpus inherited + rebuilt in this package |
| 15 | Sweetie Belle | T2 | https://mlp.fandom.com/wiki/Sweetie_Belle | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/The_Show_Stoppers | v1 corpus inherited + rebuilt in this package |
| 16 | Apple Bloom | T2 | https://mlp.fandom.com/wiki/Apple_Bloom | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/Call_of_the_Cutie · https://mlp.fandom.com/wiki/Transcripts/Crusaders_of_the_Lost_Mark | v1 corpus inherited + rebuilt in this package |
| 17 | Scootaloo | T2 | https://mlp.fandom.com/wiki/Scootaloo | https://en.wikipedia.org/wiki/Flight_to_the_Finish · https://mlp.fandom.com/wiki/Transcripts/Flight_to_the_Finish · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | v1 corpus inherited + rebuilt in this package |
| 18 | Derpy Hooves | T2 | https://mlp.fandom.com/wiki/Derpy_Hooves | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/Slice_of_Life · https://en.wikipedia.org/wiki/Derpy_Hooves | v1 corpus inherited + rebuilt in this package |
| 19 | Lightning Dust | T2 | https://mlp.fandom.com/wiki/Lightning_Dust | https://mlp.fandom.com/wiki/Transcripts/Wonderbolts_Academy · https://mlp.fandom.com/wiki/Transcripts/The_Washouts · https://en.wikipedia.org/wiki/The_Wonderbolts | v1 corpus inherited + rebuilt in this package |
| 20 | Trixie | T4 | https://mlp.fandom.com/wiki/Trixie | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/Boast_Busters · https://mlp.fandom.com/wiki/Transcripts/No_Second_Prances | v1 corpus inherited + rebuilt in this package |
| 21 | Starlight Glimmer | T4 | https://mlp.fandom.com/wiki/Starlight_Glimmer | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Transcripts/The_Cutie_Re-Mark_-_Part_2 · https://mlp.fandom.com/wiki/Our_Town | v1 corpus inherited + rebuilt in this package |
| 22 | Discord | T4 | https://mlp.fandom.com/wiki/Discord | https://mlp.fandom.com/wiki/Transcripts/The_Return_of_Harmony_Part_1 · https://mlp.fandom.com/wiki/Transcripts/The_Ending_of_the_End_-_Part_2 · https://en.wikipedia.org/wiki/List_of_My_Little_Pony_characters | v1 corpus inherited + rebuilt in this package |
| 23 | Vinyl Scratch / DJ Pon-3 | T4 | https://mlp.fandom.com/wiki/Vinyl_Scratch | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Slice_of_Life · https://mlp.fandom.com/wiki/The_Saddle_Row_Review | v1 corpus inherited + rebuilt in this package |
| 24 | Lyra Heartstrings | T4 | https://mlp.fandom.com/wiki/Lyra_Heartstrings | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Lyra_Heartstrings_and_Sweetie_Drops_(EG) · https://mlp.fandom.com/wiki/Slice_of_Life | v1 corpus inherited + rebuilt in this package |
| 25 | Octavia Melody | T4 | https://mlp.fandom.com/wiki/Octavia_Melody | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Octavia_Melody_(EG) · https://mlp.fandom.com/wiki/Slice_of_Life | v1 corpus inherited + rebuilt in this package |
| 26 | Bon Bon / Sweetie Drops | T4 | https://mlp.fandom.com/wiki/Bon_Bon | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Slice_of_Life · https://mlp.fandom.com/wiki/Call_of_the_Cutie | v1 corpus inherited + rebuilt in this package |
| 27 | King Sombra | T3 | https://mlp.fandom.com/wiki/King_Sombra | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestripedia.org/wiki/King_Sombra · https://mlp.fandom.com/wiki/The_Crystal_Empire | v1 corpus inherited + rebuilt in this package |
| 28 | Tempest Shadow / Fizzlepop Berrytwist | T4 | https://mlp.fandom.com/wiki/Tempest_Shadow | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestripedia.org/wiki/Tempest_Shadow · https://mlp.fandom.com/wiki/The_Storm_King | v1 corpus inherited + rebuilt in this package |
| 29 | Spitfire | T4 | https://mlp.fandom.com/wiki/Spitfire | https://mlp.fandom.com/wiki/Wonderbolts · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Wonderbolt_Academy_(location) | v1 corpus inherited + rebuilt in this package |
| 30 | Sci-Twi / Midnight Sparkle / human Twilight | T5 | https://mlp.fandom.com/wiki/Twilight_Sparkle_(Sci-Twi) | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Equestria_Girls:_Friendship_Games · https://mlp.fandom.com/wiki/Equestria_Girls:_Legend_of_Everfree | v1 corpus inherited + rebuilt in this package |
| 31 | Adagio Dazzle | T5 | https://mlp.fandom.com/wiki/Adagio_Dazzle | https://equestriagirls.fandom.com/wiki/Dazzlings · https://equestriagirls.fandom.com/wiki/Starswirled_Music_Festival · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | v1 corpus inherited + rebuilt in this package |
| 32 | Sonata Dusk | T5 | https://mlp.fandom.com/wiki/Sonata_Dusk | https://mlp.fandom.com/wiki/The_Dazzlings · https://equestriagirls.fandom.com/wiki/Starswirled_Music_Festival · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | v1 corpus inherited + rebuilt in this package |
| 33 | Aria Blaze | T5 | https://mlp.fandom.com/wiki/Aria_Blaze | https://mlp.fandom.com/wiki/The_Dazzlings · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Equestria_Girls:_Rainbow_Rocks | v1 corpus inherited + rebuilt in this package |
| 34 | Princess Flurry Heart | T0 | https://mlp.fandom.com/wiki/Princess_Flurry_Heart | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Crystal_Empire | v1 corpus inherited + rebuilt in this package |
| 35 | Spike | T1 | https://mlp.fandom.com/wiki/Spike | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation | v1 corpus inherited + rebuilt in this package |
| 36 | Sunset Shimmer | T5 | https://mlp.fandom.com/wiki/Sunset_Shimmer | https://en.wikipedia.org/wiki/My_Little_Pony:_Equestria_Girls · https://en.wikipedia.org/wiki/My_Little_Pony:_Equestria_Girls_%E2%80%93_Rainbow_Rocks | v1 corpus inherited + rebuilt in this package |
| 37 | Gloriosa Daisy | T5 | https://mlp.fandom.com/wiki/Gloriosa_Daisy | https://mlp.fandom.com/wiki/Camp_Everfree · https://en.wikiquote.org/wiki/My_Little_Pony:_Equestria_Girls_%E2%80%93_Legend_of_Everfree | v1 corpus inherited + rebuilt in this package |
| 38 | Juniper Montage | T5 | https://mlp.fandom.com/wiki/Juniper_Montage | https://equestripedia.org/wiki/Juniper_Montage · https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/MyLittlePonyEquestriaGirlsMagicalMovieNight | v1 corpus inherited + rebuilt in this package |
| 39 | Wallflower Blush | T5 | https://mlp.fandom.com/wiki/Wallflower_Blush | https://mlp.fandom.com/wiki/Forgotten_Friendship · https://en.wikipedia.org/wiki/My_Little_Pony:_Equestria_Girls | v1 corpus inherited + rebuilt in this package |
| 40 | Big Macintosh | T2 | https://mlp.fandom.com/wiki/Big_McIntosh | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Sweet_Apple_Acres | v1 corpus inherited + rebuilt in this package |
| 41 | Pear Butter | T2 | https://mlp.fandom.com/wiki/Pear_Butter | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/The_Perfect_Pear | v1 corpus inherited + rebuilt in this package |
| 42 | Soarin' | T6 | https://mlp.fandom.com/wiki/Soarin%27 | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Cloudsdale | v1 corpus inherited + rebuilt in this package |
| 43 | Zecora | T6 | https://mlp.fandom.com/wiki/Zecora | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://equestripedia.org/wiki/Zecora_(Friendship_is_Magic) | v1 corpus inherited + rebuilt in this package |
| 44 | Daring Do / A.K. Yearling | T6 | https://mlp.fandom.com/wiki/Daring_Do | https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters · https://mlp.fandom.com/wiki/Daring_Don%27t | v1 corpus inherited + rebuilt in this package |
| 45 | Misty Brightdawn | T6 | https://mlp.fandom.com/wiki/Misty | https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/List_of_My_Little_Pony:_Friendship_Is_Magic_characters | v1 corpus inherited + rebuilt in this package |
| 46 | Sunny Starscout | T6 | https://mlp.fandom.com/wiki/Sunny_Starscout | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://en.wikipedia.org/wiki/Equestria | v1 corpus inherited + rebuilt in this package |
| 47 | Izzy Moonbow | T6 | https://mlp.fandom.com/wiki/Izzy_Moonbow | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://mlp.fandom.com/wiki/Cutie_Blossom_Bash | v1 corpus inherited + rebuilt in this package |
| 48 | Hitch Trailblazer | T6 | https://mlp.fandom.com/wiki/Hitch_Trailblazer | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark | v1 corpus inherited + rebuilt in this package |
| 49 | Zipp Storm | T6 | https://mlp.fandom.com/wiki/Zipp_Storm | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://www.equestriadaily.com/2021/08/this-updated-map-from-my-little-pony.html | v1 corpus inherited + rebuilt in this package |
| 50 | Pipp Petals | T6 | https://mlp.fandom.com/wiki/Pipp_Petals | https://en.wikipedia.org/wiki/My_Little_Pony:_A_New_Generation · https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://mlp.fandom.com/wiki/Jazz_Hooves | v1 corpus inherited + rebuilt in this package |
| 51 | Opaline Arcana | T6 | https://mlp.fandom.com/wiki/Opaline | https://en.wikipedia.org/wiki/My_Little_Pony:_Make_Your_Mark · https://mlp.fandom.com/wiki/Locations · https://villains.fandom.com/wiki/Queen_Opaline | v1 corpus inherited + rebuilt in this package |

---

## 7. Limitations and Open Items (Must Be Told to the Client Honestly)

1. **This round could not reach Fandom/Wikipedia/Baidu Baike/Moegirlpedia directly** (timeouts/403s). Character facts rely on the v1 corpus fetched on 2026-10-23 (full Fandom texts + Wikipedia texts); this round only added incremental sites (EQD/Bilibili/official) and search-level corroboration.
2. **No body text was obtained from the Chinese encyclopaedias:** Baidu Baike/Moegirlpedia search records are kept only and are not used as evidence; Chinese name translations follow the v1 cards and community convention, and multiple translations are retained.
3. **Two versions of the G5 map disagree:** the EQD analysis states this explicitly; this package adopts a compromise mapping and marks everything Low. If the client needs "official precise coordinates", no such public data exists today.
4. **Distance figures are rough estimates:** from the v1 project's equidistant-projection conversion, used only to judge "distance bands"; do not cite specific km as setting fact.
5. **Voice cast/crew information** was not verified item by item (IMDb anti-scraping); it is background only in the profiles and is not evidence for a character's abilities or plot.
6. **Secondary canon (IDW/official books)** was not checked book by book; where involved it is marked "secondary / one tier lower", with no effect on the main profiles.
7. **Currency:** research is current to 2026-10-24; if new works or official setting updates appear, re-grade under P6 and update the profiles.

---

## 8. Evidence Inventory (Files)

| File/directory | Content | Size class |
|---|---|---|
| `research/raw_extra/_fetch_log.tsv` (retained in the source Chinese edition) | 24 fetch records (status / bytes / sha256 / elapsed / final URL) | Small |
| `research/raw_extra/eqd_g5_maps.*` (source edition) | EQD "G5 Maps" long-form article (G4<->G5 map comparison) | 2.0 MB |
| `research/raw_extra/bilibili_rail.*` (source edition) | Bilibili Equestria railway material | 57 KB |
| `research/raw_extra/official_mlp_home.*` (source edition) | Official Hasbro page (redirects to global support) | 67 KB |
| `research/raw_extra/imdb_*` (source edition) | IMDb anti-scraping pages (not adopted) | 2 KB x2 |
| `../mlp_agents/_sources/` | Full v1 corpus: 51 character pages + 6 geography pages + Wikipedia texts | ~2.5 MB |
| `../mlp_agents/profiles/` | v1 English canon profiles (51 files) | ~800 KB |
| `data/cards8.json` | 51 character runtime cards (with a `sources` field) | ~750 KB |
| `docs/02-geography.md` | Location master table and 65-place reference | 38 KB |

---

## 9. Review and Update Recommendations (for Future Maintainers)

1. When the network allows, re-fetch the Fandom G5 three-settlement pages and the Wikipedia G5 pages, and add them to `_sources`.
2. If an official high-resolution G5 map or art book becomes available, update the section 5 mapping and confidence under "official maps > EQD analysis".
3. Once the Chinese encyclopaedias are accessible again, redo the cross-check of Chinese name translations and character introductions, and update `name_cn` and the name-translation table.
4. Whenever a new source enters the database, update: this file, the `sources` field in `data/cards8.json`, section 8 of the relevant Agent files, and run `tools/validate.py`.
5. Do not delete failure records — they are the evidence of "what we did not verify", and the roadmap for future maintenance.

---

**Version:** v1.0 (2026-10-24) | Maintainer: Overall Team Lead + Spike (archives) | Changes must be synced to `data/` and the source sections of the Agent files.

# Arxiv Daily Deep Report - 2026-09-28

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 30
---

## 1. RePlay: Retrieval-Based Voice Playback for Multi-Turn spoken dialogue

**作者**: Sathvik Udupa, Naveen Kumar, Ryan Folmsbee
**链接**: [2609.31588](https://arxiv.org/abs/2609.31588)
**分类**: Spoken Dialogue Systems | **关键词**: spoken dialogue systems, retrieval-based response selection, low-latency interaction, full-duplex spoken language models, layer-wise probing, pre-recorded voice playback

# RePlay: Retrieval-Based Voice Playback for Multi-Turn Spoken Dialogue

## 核心痛点
- 许多语音交互应用（娱乐/游戏中的交互角色、场馆导览、客服）要求对回复的**内容与演绎方式**都有精确控制，通常使用预录台词。
- **全双工端到端语音对话模型**响应延迟低、行为可控性不断增强，但开放式生成无法保证精确内容，也无法复现某一条特定录音表演。
- **级联系统**（ASR + LLM + 回复选择）可以被约束到预定义回复集合，但引入额外延迟；基于 LLM 的选择召回更高，代价是延迟更大。
- 现有语音检索工作（SpeechRAG 等）多是"检索知识以支撑生成"，且通常在用户说完后查询一次，检索到的信息仍需再经过生成才能到达用户，无法保证精确台词与演绎。

## 方法创新
### 1) 探针分析：何时、何层能恢复"即将说出的回复"
- 以 PersonaPlex（Mimi 语音编码器 + 32 层 Transformer LLM + Depth Transformer + 文本流）为基础。文本流使用三类 token：`<WRD>`、`<EPAD>`（通常紧邻每个词之前）、`<PAD>`；用户话轮结束后的第一个 `<EPAD>` 标志系统回复开始。
- 考察两个候选帧：`<EPAD> predict`（该 token 被预测的帧）与 `<EPAD> input`（该 token 作为输入的下一帧）。
- 在每个层、两个帧上训练岭回归，把隐状态映射到 PersonaPlex 回复的 nomic-embed-text 嵌入；用 top-5 检索准确率与 k=16 k-means 聚类的平衡准确率评估（使用 200/100 条通用、无关键词的单轮问答）。
- 结论：`<EPAD> predict` 帧在所有层都接近随机水平；`<EPAD> input` 帧在 13–14 层附近急剧上升并持续提升。因此读取 **layer 15 在 `<EPAD> input` 的隐状态**，只保留前 16 层 LLM，将 LLM 计算量减半但仍保留清晰的回复信号。

### 2) RePlay 架构
- 保留 PersonaPlex 前 16 层 LLM，丢弃其余层与语音生成模块；不再生成语音，而是**选择脚本台词并播放其预录音频**。
- 输入与 PersonaPlex 基本一致，但有两处不同：
  - `<EPAD>` 只在每条回复的第一个词之前保留，作为专用的"话轮开始" token；
  - 播放的台词取代生成语音：音频走系统通道，其文字按强制对齐的时间戳插入文本流。
- 文本输出被替换为 layer 15 上的两个线性头：
  - **Head Turn**：将每帧分类为 `<PAD>` / `<EPAD>` / `<WRD>`（`<WRD>` 合并所有词 token），当 `<EPAD>` 概率最高时判定系统话轮开始；
  - **Head Embed**：在紧随其后的 `<EPAD> input` 帧，把隐状态投影到文本嵌入空间，用与冻结台词嵌入的余弦相似度给每句台词打分。
- 由于没有参数与具体台词绑定，新台词只需嵌入即可加入，**无需重新训练**。

### 3) 检索训练
- Head Embed 在每个话轮起始 `<EPAD>` 之后的帧上训练，与冻结的台词嵌入对齐（nomic-embed-text），使用单向 SigLIP loss 加一个余弦对齐项：
  - L = −(1/|B|) Σ_{i∈B} Σ_{j∈C(i)} log σ( y_ij (τ s_ij + b) ) + (λ/|B|) Σ_{i∈B} (1 − s_{ii+})
  - 其中 B 为 batch 中的系统话轮集合，s_ij 为投影 z_i 与台词 j 的余弦相似度，i+ 是目标台词；C(i) 包含 i+ 以及按嵌入相似度挖掘的困难负样本，并排除与目标近乎改写的句子；y_ij = +1（j=i+）或 −1，τ 为可学习逆温度，b 为可学习偏置，λ 权衡对齐项。
- 训练细节：两个头用 teacher forcing 联合训练；数据为合成数据，为保持对真实语音的鲁棒性，对第 0–9 层施加 LoRA（rank 256），仅全量微调第 10–15 层；Head Turn 用交叉熵，`<EPAD>` 权重为 9；τ 与 b 初始化为 10 与 −10；序列最长 90 s，8 张 A100 (40 GB)。

### 4) 数据与基线
- **D1 合成多角色对话**：用 LLM（Sonnet 5）生成 100 个角色，每个角色约 300 条去重台词、覆盖 30 个意图（共 29,225 条）；随后生成自由形式访客话轮的对话并按 line ID 选择角色回复；刻意让 1/4 访客话轮意图欠明确，使模型学会依赖对话上下文并回复澄清台词。共 52,768 段对话（1071 h），用 Chatterbox TTS 配克隆的 VCTK / LibriSpeech 音色合成，加入长用户停顿与 WHAM! 噪声。
- **D2 目标任务**：用户面试非人角色 Nobu 的职位面试场景；作者为 Nobu 撰写 300 条台词、覆盖 30 个面试意图，模拟方式同 D1。在 D1 上训练后用 2 h 模拟 D2 面试微调。泛化划分：AS（所有台词都见过）、UL（每意图 50% 台词留出）、UI（一半意图完全留出，排除问候/告别等共享意图）。
- 基线（均为级联，最后从 300 条 Nobu 台词中选择并立即播放预录音频）：A = Azure ASR final + GPT-4.1 从全台词集选择；B = Kyutai VAD≥0.6 + Gemma-4-E4B 选择；C = Kyutai + Gemma-3-1B 自由回复后按嵌入相似度映射到最近台词（用短 persona 与话题换取延迟）。
- 评测：用 GPT-4o-mini 模拟面试官（无系统意图/台词信息），Breeze-TTS-2 合成用户话轮，共 100 个最长 90 s 的脚本场景；用 GPT-4o-mini 裁判给出意图一致性 IntentAgr、R@k（裁判首选为 k=1、前三为 k=3、再加 7 个最相似台词为 k=10），以及 1–5 分的参与感/响应性评分 Q；话轮接管报告截断率 CR 与延迟 p10/p50/p90/mean。

## 实验结果
- **延迟**：RePlay 中位延迟 383 ms（p10 333 / p50 383 / p90 439 / mean 387），比同等级对话质量的级联快 3–7 倍。级联 A 中位 2612 ms（mean 2652）、级联 B 中位 1226 ms（mean 1145）、级联 C 中位 591 ms（mean 569）。
- **检索与对话质量**：RePlay R@1 0.35 / R@3 0.50 / R@10 0.60，Q 3.76，IntentAgr 0.83，CR 3.6%。级联 A 检索更强（R@1 0.52，Q 3.90，IntentAgr 0.85）但极慢；级联 B 与 RePlay 接近（R@1 0.36、Q 3.77、IntentAgr 0.77）但慢 3 倍；级联 C 快但质量差（R@1 0.17、Q 2.99、IntentAgr 0.35、CR 17.0%）。总体上 RePlay 以更低的精确台词准确率为代价，换来显著更低的延迟。
- **用户研究**：与使用小 LLM 的快速级联相比，被试在 63% 的评分中偏好 RePlay，而该级联仅 12%（p = 0.008）；与使用更强 LLM 的较慢级联相比，RePlay 偏好为 46% vs 21%，差异不显著。
- **贡献总结**：(1) 探针分析表明全双工模型在话轮开始处即可恢复即将给出的回复；(2) RePlay——一个截断的语音对话系统，用话轮接管头与检索头实现低延迟回复检索；(3) 模拟多轮评测与用户研究，中位延迟 383 ms，比同质量级联低 3–7 倍。

## 一句话评价
RePlay 把"回复选择"直接提前到话轮边界并用预录台词播放，通过层探针找到回复可恢复的最早层/帧（layer 15, `<EPAD> input`），在几乎不损失对话质量的前提下把多轮语音对话的中位延迟压到 383 ms，为需要精确内容与固定演绎的交互角色类应用提供了一条实用的低延迟路线。

---

## 2. Assessing a Mathematical Model of Syllable Production via CTW Alignment with EMA Data

**作者**: Frédéric Berthommier
**链接**: [2609.31508](https://arxiv.org/abs/2609.31508)
**分类**: Articulatory Modeling / Speech Production | **关键词**: Articulatory Modeling, Syllable Production, Coarticulation, EMA, Maeda Parameters, CTW Alignment, Model Validation, Articulatory Model Transparency

# 论文总结：Assessing a Mathematical Model of Syllable Production via CTW Alignment with EMA Data

## 核心痛点
- 神经语音合成中，发音建模（articulatory modeling）的可解释性与透明性不足，需要区分不同层级的透明性。
- Level 1 端到端神经发音表示（EMA、X-ray、实时 MRI、WavLM 类自监督编码器、HiFi-GAN 声码器）虽合成质量高，但学习到的参数 largely data-driven，缺少发音控制变量基础。
- Level 2 将显式发音合成器嵌入神经网络（如 Tensor2Tract + VocalTractLab），具有物理可解释性，但语言透明性仍有限。
- 需要验证一个由语言内容（音素与音节结构）驱动的确定性音节规划模型，能否在共享 Maeda 发音参数空间中与真实 EMA 发音数据形成结构对应。
- 近期实验（Kasper et al.）观察到规则音节序列中发音预判（anticipation）至少提前 200 ms，模型需具备前瞻性规划能力。

## 方法创新
- 提出四层发音模型透明性框架：Level 1 端到端神经发音表示；Level 2 神经框架结合显式发音合成器；Level 3 手势与语言内容显式关联（本文所属）；Level 4 生理透明性。
- 使用数学定义的音节规划架构，集成 Maeda 发音参数；这些参数不仅是几何描述，也近似具有生物力学意义的控制变量。
- EMA 到 Maeda 参数的简单线性映射：将 14 个 EMA 坐标中的 13 个投影到 6 个功能一致的发音自由度：Jaw、Body、Drsm、Tip、LipP、LipH。
- 预处理：500 Hz 降采样至 100 Hz，每个文件 1000 帧（约 200 静音帧），8 Hz 零相位低通滤波，z-normalize；再用模型输出的均值和标准差对经验数据重归一化。
- 模型生成：用有向图 G=(V,E) 表示音节规划，节点为元音或辅音目标，弧表示过渡；节点在复平面中具有 (ρ,θ) 位置，并符合发音特征。音素库存为 /e, a, i, u/ 与 /d, g/，与数据库中的 /s, t, k/ 被视为音素一致。辅音 /g/ 有前化与后缩两个同位异音。规划在静音期也持续。时间由参数 T=16 帧控制，停顿时长 Tp=16。声母弧与韵母弧同时规划并叠加，产生无权重协同发音。引入 anticipatory vowels Vo，通过 “.” 连接音节图。示例 Model12 首词为 “déa.gu.da.da”，来自 File12 的 C’est /akuta/ ça ?。每个 CV 环持续 2T，一个词约 5×2T=10T 加一个停顿 Tp；一个文件含 6 个词，共 6×11×16=1056 帧，每帧 10 ms。
- 对齐与验证：采用非对称 Canonical Time Warping (CTW)，将模型生成的 Maeda 轨迹对齐到 EMA 时间网格（1000 样本），不改变 EMA 时间轴。对 CTW 映射到每个 EMA 索引的模型帧取平均，再作 8 Hz 零相位低通。使用 permutation test 统计验证，比较音素一致条件与音素不一致替代条件。条件 A 与 B 均允许音节一致性，但只有 A 具有音素一致性。
- 评估指标：对齐质量、Maeda 参数相关系数、合成 formant 轨迹 F1–F3 相关系数。

## 实验结果
- 对 63 个文件（9 次重复 × 7 个短语）进行 CTW 对齐；活跃语音区域对应前 800 帧（索引 0–800）。
- 条件 A 的 warping path 在尺度校正后接近直线，说明对齐质量较好；条件 B 偏差更大，反映音素不一致。
- 同一 CTW warping path 同时作用于六个发音参数，从而保持它们协调的时间结构。
- 统计分析显示：音素一致配对的 alignment quality 显著优于音素不一致的 surrogate 条件；Maeda 参数和 formant 轨迹相关性在条件 A 下更好。
- 结论：模型与发音数据之间存在强结构对应，为模型的 representational validity 提供了实验支持。摘要指出 phonetically congruent pairings 的对齐显著更好。

## 一句话评价
该研究通过 EMA→Maeda 线性映射、CTW 非对称对齐与置换检验，为确定性音节规划模型的语言透明性提供实验支持，表明其生成轨迹与真实发音数据具有显著结构对应，但感知合成质量并非其优化目标。

---

## 3. SAID: Semantic Acoustic Imaging Detector for Sound Event Localization and Detection

**作者**: Runbang Wang, Zining Liang, Yin Cao, Qiuqiang Kong
**链接**: [2609.31492](https://arxiv.org/abs/2609.31492)
**分类**: Sound Event Localization and Detection (SELD) | **关键词**: Sound Event Localization and Detection, Semantic Acoustic Imaging, Sound Source Localization, Panoramic Feature Learning, Mask Transformer, Spatial Audio

## 论文信息

- **标题**: SAID: Semantic Acoustic Imaging Detector for Sound Event Localization and Detection
- **会议**: DCASE 2026（2026年10月28–29日，美国波士顿）
- **作者**: Runbang Wang, Zining Liang, Yin Cao, Qiuqiang Kong
- **单位**: 南京大学、香港中文大学、中国科学院声学研究所、香港中文大学先进工程研究所（SHIAE）
- **代码**: https://github.com/IN03X/SAID
- **arXiv**: 2609.31492

## 核心痛点

语义声学成像（Semantic Acoustic Imaging）要求从音频中预测每个活动声源对应的带类别标签的声学图：一张水平360°、垂直180°的矩形图像，其中声源所占据的方向区域以“区域”形式标出，区域内的数值表示声音能量，并配以类别标签。该任务可服务于机器人环境感知与AR声学可视化。

现有方法存在三个关键问题：

1. **传统SELD只预测类别与点方向**：以SELDnet及后续注意力模型为代表的方法只能给出每个声源的类别和单一方向，无法描述声源占据的区域范围及区域内能量分布。
2. **邻近多源与时变区域难以处理**：模型需要为邻近方向上的不同声源分别预测带标签的声学图，而活动声源数量、位置与区域大小随时间动态变化。
3. **音频缺乏声学图式的方向化特征**：图像分割网络（如Mask2Former）可以处理可变数量区域，但音频录制本身并不直接提供按方向排布、与声学图格点对齐的特征表示。

## 方法创新

作者提出 **SAID（Semantic Acoustic Imaging Detector）**，整体由编码器 **Audio2Sph** 与解码器 **Sph2Imaging** 构成，借鉴MaskFormer/Mask2Former的“query + mask”范式，把声源当作可学习槽位（slot）来预测独立的带标签声学图。

### 1. Audio2Sph 编码器
- 输入48 kHz四通道音频，STFT（2048点Hann窗、2048点FFT、480点帧移）得到100 fps的幅度与相位；将多通道对数幅度与相位正余弦拼接后送入4个ConvNeXt阶段。
- 后三个阶段输出多尺度时频特征 X1、X2、X3。
- **球面交叉注意力（Spherical Cross-Attention）**：为 H=45（仰角）× W=90（方位角）× D=16 的方向网格设置可学习查询，通过注意力在频率维上聚合特征，把时频特征映射到方向网格上，得到 Yi ∈ R^{T0×H×W×D}；三者相加得到 Y0，再经时间对齐（自适应平均池化与最大池化取平均）得到10 fps的**全景特征 Y ∈ R^{T×H×W×D}**。

### 2. 类别无关预训练
- 预训练阶段，Y0 先送入全景解码器（Panoramic Decoder），通过三层卷积与两次2倍双线性上采样，输出每帧180×360的**类别无关声学图**（所有活动声源总能量图），该监督不依赖类别标签，用于教会编码器定位声音能量；预训练后该分支被移除。

### 3. Sph2Imaging 解码器
- 将全景特征投影到 S=256 通道，通过两次步长2卷积构建多尺度网格；采用**多尺度可变形注意力（Multi-Scale Deformable Attention）**预测采样位置与权重。
- 经Up Block恢复出Small/Medium/Large三层特征，最终1×1卷积得到 **Map Features M ∈ R^{T×H×W×S}**。
- 引入**冻结的PaSST**（AudioSet预训练PaSST-S，并在DCASE数据上进一步训练后冻结）提取类别特征 T×768，投影并与 Cl=13 个可学习类别嵌入相加，得到类别键值。
- 每帧初始化 **N=16个可学习Slot Queries**，每个slot代表一个候选声源而非固定方向或类别。
- **Map Head**（3层MLP）将查询映射后与Map Features做点积+sigmoid，得到45×90的连续 **Slot Map Mask**（MaskFormer式）。
- **9层Mask Decoder**（Mask2Former式）逐帧独立更新查询：KV Block循环选取Large/Medium/Small特征；用上一层mask的sigmoid阈值0.5定义二值注意力区域做**Masked Cross-Attention**，再与PaSST类别特征做交叉注意力，随后进行跨slot自注意力与FFN。
- **Active Head**预测 Cl+1 个分数（含no-object），**Class Head**通过ConvNeXt X2/X3与交叉注意力+2层MLP输出 Cl 类概率。
- **Refine Block**将Map Features与最终slot查询上采样/投影后点积，生成180×360高分辨率掩码用于训练监督与推理；每个掩码赋予最高类别概率的类别，置信度为活动分与类别分的乘积。

### 4. 数据生成与训练流程
- 开发了生成模拟录音的pipeline用于预训练，并支持在DCASE真实录音上微调。

## 实验结果

在 **DCASE2026 Task 3 Track A 官方评测集**上，提交系统**排名第一**，取得 **Macro mAP = 0.1080**、**Macro Pearson r = 0.3962** 的成绩。论文提供了演示与代码。

## 一句话评价

SAID将语义声学成像重新定义为“每个声源一张带标签全景图”的query-based掩码预测问题，通过方向化编码器Audio2Sph、类别无关预训练与Mask2Former式多槽解码器Sph2Imaging，有效解决了传统SELD无法输出区域与能量、且难以处理时变多源的问题，并在DCASE2026 Task 3 Track A上取得第一名的成绩。

---

## 4. Why Alzheimer's Speech Screening Fails to Generalize: Bridging the Deployment Gap via Cross-Corpus Evidence Anchoring

**作者**: Zijian Lu, Sizhe Liu, Yin Zhang, Jixuan Deng, Xinrong Lin, Xinchen Yuan, Chicheng Jin, Yiping Zuo, Yuanchao Li
**链接**: [2609.31293](https://arxiv.org/abs/2609.31293)
**分类**: Alzheimer's Disease Speech Screening | **关键词**: Alzheimer's disease detection, Cross-domain evaluation, Cross-corpus generalization, Explainable speech processing, Leave-one-corpus-out, XLM-R, GroupDRO, Evidence anchoring

# 论文总结：Why Alzheimer's Speech Screening Fails to Generalize

## 核心痛点
- 基于语音的阿尔茨海默病（AD）及相关认知风险筛查是非侵入、可远程、可纵向追踪的潜在方案，但模型通常在单一语料/域内训练和随机划分评估，部署到新语言、任务、麦克风、分割策略、ASR错误分布时泛化性差。
- 在4个异质语料上做 Leave-One-Corpus-Out（LOCO）评估，发现70个可解释语音/语言特征中有59个在健康对照（HC）与认知风险组之间的效应方向跨语料冲突；停顿、静音、语速等常被视为通用损伤代理，但对任务设计和录音协议高度敏感，单标记规则在域偏移下不安全。
- 深度表示也有风险：XLM-R 文本基线平均性能强，但在最弱留出域 AUC 仅 0.520，说明强平均性能可掩盖特定未见语料的严重失败。
- 因此论文主张将最差域鲁棒性作为主要评估标准，而不是只看分布内平均分。

## 方法创新
- 评估框架：采用 LOCO 跨验证，每次留出一个完整语料作为外部测试集，其余三个作为源域训练；所有特征选择、缩放、模型拟合、阈值校准仅在训练语料上完成，避免目标域泄漏。
- 数据集：NCMMSC（中文，混合任务）、Pitt Cookie（英文，图片描述）、TAUKADIAL Mandarin（中文，连接性临床语音）、Mandarin Chou（中文，图片描述）；共1561样本、663说话人，HC 673、风险 888。统一为 HC vs 认知风险二分类。
- 特征与模型：70个可解释高层语音/语言特征，覆盖时间不流畅、停顿动态、语速、声学强度、词汇多样性、POS分布、词汇集中度、重复标记、信息结构、语篇连贯性；24个经典特征构成传统基线。深度基线使用冻结的 XLM-R 文本嵌入（768维）和 wav2vec 2.0 第12/24层表示（1024维），下游为加权 L2 正则逻辑回归；并对比 GroupDRO 域泛化基线。
- 证据锚点融合：三阶段部署导向框架：1）审计跨语料标记可靠性；2）从源数据选择紧凑的鲁棒证据锚点；3）将锚点分数与 XLM-R 文本基线分数融合。提出平衡融合与锚点重融合两种配置，分别优化平均性能和最差域性能。
- 控制实验：标签打乱、元数据/长度控制、语料偏差控制、语料身份探针，用于确认模型捕获的是真实可迁移临床信号而非数据伪影。
- 指标：以说话人级 AUC 为主，报告宏平均 mean speaker AUC 和最差域 worst-case speaker AUC；AUC 无阈值，决策阈值仅用训练说话人校准。

## 实验结果
- 特征审计：70个标记中59个跨语料方向冲突；词汇和POS标记相对稳定，而静音、语速、停顿时长等高度协议敏感。
- XLM-R 文本基线：平均表现强，但最弱留出域 AUC 降至 0.520。
- GroupDRO 基线：平均说话人 AUC 0.766，最差域 AUC 0.504。
- 所提融合：平衡融合达到 0.785 平均说话人 AUC；锚点重融合将最差说话人 AUC 提升到 0.615，说明证据锚点可显著改善最弱域鲁棒性。
- 结论：跨语料部署时，单一可解释标记和纯深度表示都不够可靠；需要审计特征可迁移性，并显式报告最差域泛化性能。

## 一句话评价
论文系统揭示了阿尔茨海默病语音筛查从基准到部署的泛化鸿沟，并通过跨语料证据锚点与 XLM-R 融合，在保持平均性能的同时显著提升最差域鲁棒性，为该领域提供了以最差域为中心的评估与建模范式。

---

## 5. Room Impulse Response Embeddings for Speech Enhancement in Noisy and Reverberant Environments

**作者**: Adrian Meise, Reinhold Haeb-Umbach
**链接**: [2609.31041](https://arxiv.org/abs/2609.31041)
**分类**: Speech Enhancement / Dereverberation | **关键词**: Room Impulse Response (RIR), Speech Enhancement, Dereverberation, Self-Supervised Learning, Contrastive Learning, Teacher-Student Learning, Embeddings, Deep Filtering

## 核心痛点
- 实际远场录音同时受混响和加性噪声影响，RIR/空间传播信息有助于去混响和语音增强，但传统方法依赖监督估计RIR、T60、DRR，或假设这些信息已知。
- 自监督学习在频谱表征上很成功，但空间/RIR自监督表征研究较少；已有RIR嵌入主要用于声学参数估计、房间分类、RIR估计/生成，较少系统用于语音增强。
- 噪声会破坏RIR嵌入的表示空间：噪声导致表征偏移与弥散；而先降噪再提取嵌入会依赖降噪系统并引入伪影，且可能假设混响对降噪透明，这通常不成立。

## 方法创新
提出三阶段课程学习/自监督RIR表示学习框架：
1. **混响数据对比学习**：沿用[12]的Conformer RIR编码器。正样本为同一RIR卷积不同语音，负样本为不同RIR卷积同一语音，迫使嵌入忽略源信号、只编码RIR；损失为InfoNCE与负样本余弦相似度的加权和。
2. **噪声-混响数据对比学习**：在上一阶段模型上继续训练。正样本中同一RIR配不同噪声，负样本中不同RIR以更高概率配相同噪声，促使模型忽略噪声、聚焦RIR差异。
3. **教师-学生训练**：冻结阶段1教师，对混响输入产生目标嵌入；阶段2学生接收带噪混响输入，用MSE回归教师嵌入，同时保持正负样本设置，使噪声鲁棒的学生嵌入空间对齐干净混响嵌入空间。

## 实验与结果
- 数据：EARS 100h干净语音、EARS-Reverb、EARS-WHAM v2；训练噪声来自WHAM!、CHiME-3、SINS、SMS-WSJ；测试使用未见噪声DEMAND和未见RIR BUT-ReverbDB。
- 编码器：Conformer 10层、256隐藏单元、4注意力头、两层MLP输出256维ℓ2归一化嵌入。
- 声学参数估计：用514参数线性层从嵌入估计T60和DRR，对比0.27M参数1D-CNN直接从波形估计。
  - 混响测试：Stage1/2/3的T60 MAE约0.17–0.21s、ρ约0.73–0.76，DRR MAE约2.51–2.74dB；远优于CNN波形估计（T60 MAE 0.30s，DRR 7.36dB）。
  - 噪声-混响测试：Stage2/3显著优于Stage1和Denoised+Stage1；Stage3学生取得T60 MAE 0.23s/ρ0.68、DRR MAE 2.56dB/ρ0.51，说明教师-学生训练有效恢复噪声鲁棒性。
- 摘要指出：将嵌入条件化到判别式深度滤波语音增强模型，在混响和噪声-混响条件下所有评价指标（含下游WER）均取得一致提升。论文片段在表1后截断，第5节语音增强细节未展示。

## 一句话评价
该工作用“混响对比学习→噪声混响对比学习→教师-学生蒸馏”的三阶段自监督方案，在不依赖RIR标签的情况下学习噪声鲁棒的RIR嵌入，并通过轻量探针验证了嵌入确实编码T60/DRR，进而为判别式语音增强提供有效空间条件信息。

---

## 6. A Comprehensive Study of Content Representations for Speech Synthesis

**作者**: Diego Torres, Axel Roebel, Nicolas Obin
**链接**: [2609.30975](https://arxiv.org/abs/2609.30975)
**分类**: Speech Synthesis | **关键词**: content representations, speech synthesis, voice conversion, speaker disentanglement, speech tokenizer, self-supervised learning, neural audio codec

### 论文信息
- **标题**: A Comprehensive Study of Content Representations for Speech Synthesis
- **作者**: Diego Torres, Axel Roebel, Nicolas Obin
- **机构**: STMS Lab, IRCAM, CNRS, Sorbonne Université

### 核心痛点
- 语音内容表示（content representations，也称 semantic tokens）广泛用于语音转换、语音到语音翻译、多模态语言模型和 TTS，但不同表示通常按产生方式分组评估，很少在同一生成式框架下直接比较「每个表示到底包含什么信息」。
- 已有基准将声学 tokenizer 与内容 tokenizer 放在同一排名中，但二者目标不同，且未直接评估解耦；已有 SSL 探测多局限于 k-means/RVQ 和少数 HuBERT 层。
- 不同应用对表示需求相反：传统 VC 更关注音色，口音转换更关注韵律；因此关键问题不是「是否解耦」，而是「捕获了语音的哪些方面、程度如何」。

### 方法创新
- **统一生成式评估框架**：仅以每种表示为条件训练生成模型，不提供说话人 ID 或参考音频，避免生成模型依赖额外身份通道造成混淆。生成模型学习 `p(x|r)`，由于 `r=f(x)`，生成可视为从 `X(r)={x:f(x)=r}` 中采样；集合内不变属性被保留，变化属性被重采样。
- **覆盖广泛的表示**：SSL 特征（HuBERT-base、WavLM-base 第 6 层）、k-means 量化、VQ-VAE、VQ-ASR、PPG 后验图及其 argmax、Soft units、SpeechTokenizer、ContentVec，全部统一到 50 Hz 帧率。
- **多维评估指标**：内容用 dWER；说话人身份用 VoicePrivacy 协议的 EER（50% 表示无说话人信息）、性别探针准确率；韵律用 F0 轮廓 MSE 分解为寄存器误差、范围误差和相关性；另用 UTMOS 检查音频质量。
- **声学模型**：将表示上采样到 100 Hz，用 flow-matching 生成 100 Hz mel 频谱（100 mel、1024 FFT、hop 240 @24 kHz），ConvNeXt+attention，约 67M 参数，单卡 RTX 4070 训练 800k 迭代，使用 classifier-free guidance 和中点 ODE 求解，波形由 Vocos 声码器生成。

### 实验结果
- 数据：LibriTTS，train.clean.100/360 训练，dev.clean 选 checkpoint，test.clean 评估；24 kHz 合成，SSL 编码器涉及处重采样到 16 kHz。
- **两种明显 regime**：
  1. **近乎重建原始音频的表示**：连续 SSL 特征（HuBERT dWER 0.5%、EER 1.3%、Gender 98.7%、Sim 0.61；WavLM EER 2.0%）、VQ-VAE（EER 12.8–20.3%）、Soft units（EER 2.2%）等，内容/说话人/韵律保真度高，但说话人身份泄露明显。
  2. **有效解耦说话人身份的表示**：k-means 量化 HuBERT（EER 32–36%）、VQ-ASR（EER 46–48%）、PPG（EER 40%）、PPG argmax（EER 43%）等，说话人身份被大幅削弱，但内容与韵律指标变差（dWER 升高、pitch corr 降低）。
- ContentVec EER 16.3%、SpeechTokenizer EER 28.8%；连续 VQ-ASR EER 8.6%，量化后 EER 显著升高，说明监督+量化瓶颈共同影响解耦。
- 表 2：VQ-ASR 码本维度降到 8 时，256 codes 版本 dWER 3.2%、EER 46.8%、Gender 55.9%、Pitch Corr 0.29；连续版本 dWER 2.4%、EER 39.7%、Gender 71.9%、Pitch Corr 0.35，相对 256-d VQ 有显著变化。
- **核心发现**：解耦不只取决于是否有监督，而取决于训练目标与表示信息容量的相互作用；受监督的表示只有在容量被充分约束时才会解耦说话人身份。

### 一句话评价
本文用统一的「仅以表示为条件」生成式评估框架系统比较 SSL、监督 token、后验图和神经音频编解码器，实证揭示语音内容表示在「高保真重建」与「说话人解耦」之间存在权衡，且解耦由训练目标与信息容量共同决定，为 VC/S2ST/TTS 的表示选择提供了清晰依据。

---

## 7. Coupled Meta-Adaptive Filtering for Active Noise Control Under Time-Varying Acoustic Paths

**作者**: Boxiang Wang, Zhengding Luo, Ziyi Yang, Dongyuan Shi, Xuexian Liu, Woon-Seng Gan
**链接**: [2609.30945](https://arxiv.org/abs/2609.30945)
**分类**: Active Noise Control | **关键词**: Active Noise Control, Meta-Adaptive Filtering, Meta-Learning, Time-Varying Acoustic Paths, Online Secondary Path Modeling, Delayless Dual-Rate Implementation

## 论文信息
- **标题**：Coupled Meta-Adaptive Filtering for Active Noise Control Under Time-Varying Acoustic Paths
- **作者**：Boxiang Wang, Zhengding Luo, Ziyi Yang, Dongyuan Shi, Xuexian Liu, Woon-Seng Gan
- **机构**：南洋理工大学、西北工业大学、浙江大学
- **代码**：https://github.com/Wang-Boxiang/CoMeta-AF-ANC

## 核心痛点
- 传统 ANC 多采用 FxLMS 等手工设计更新规则，存在收敛慢、可能发散、快速变化声学条件下跟踪能力有限、需要经验调参等问题。
- Meta-AF 将自适应滤波器更新建模为元学习问题，通过 DNN 直接从信号特征预测滤波器增量，但用于 ANC 时仍面临时变声路径挑战。
- 关键问题在于：Meta-AF 的物理信息优化器特征依赖次级路径估计；当物理次级路径变化而估计保持不变时，特征失配会导致控制滤波器更新不准确、降噪性能下降。
- 现有在线次级路径建模（OSPM）方案也有局限：辅助噪声法会引入额外残余噪声；无辅助噪声法依赖控制信号频谱丰富度；传感器条件神经网络方法需要摄像头等额外设备，增加复杂度并有隐私顾虑。

## 方法创新
- 提出 **CoMeta-AF-ANC**（Coupled Meta-Adaptive Filtering Active Noise Control），将控制滤波器自适应与声学路径在线跟踪统一到一个闭环元学习框架中。
- 提出 **Meta-Gated Joint Path Identifier (MG-JPI)**：仅利用可获得的 ANC 信号，无辅助噪声地联合跟踪主路径和次级路径；更新后的次级路径估计会反馈用于重构 Meta-AF 控制器特征。
- 控制器和路径辨识器相互耦合：控制器输出为路径辨识提供激励，路径估计更新又服务于后续控制器自适应；两个优化器通过同一闭环递归联合训练。
- 实现 **无延迟双速率（delayless dual-rate）** 结构：控制信号在时域逐样本生成，保持因果前馈控制；学习到的自适应在帧率下执行，从而避免块处理延迟。
- 主要贡献包括：时变声路径下学习优化器联合控制滤波器与主/次级路径更新的耦合框架；无辅助噪声联合路径辨识器 MG-JPI；无延迟双速率实现；基于实测声路径与多样噪声的实验验证。

## 实验结果
- 使用实测头枕声路径进行评估，CoMeta-AF-ANC 在跟踪时变声路径方面优于代表性 ANC 算法。
- 在未见头部运动场景中保持更高稳定性。
- 对训练中未遇到的真实噪声也表现出良好泛化能力。
- 实验使用实测声路径和多种噪声信号，验证了方法在时变声学条件下的有效性与泛化能力。

## 一句话评价
该论文将控制滤波器自适应与主/次级路径在线跟踪统一到闭环元学习框架中，并通过无延迟双速率实现兼顾因果控制与学习自适应，是 Meta-AF 在时变 ANC 场景下的一项重要推进。

---

## 8. Music Source Separation via Stem Discovery

**作者**: V. Valtteri Kallinen, Eloi Moliner, Lauri Juvela, Vesa Välimäki
**链接**: [2609.30912](https://arxiv.org/abs/2609.30912)
**分类**: Music Source Separation | **关键词**: Music Source Separation, Blind Source Separation, Query-based Source Separation, Stem Discovery, Conditional Flow Matching, Audio Embedding

# Music Source Separation via Stem Discovery (MuS3D)

## 核心痛点
- 传统 MSS 研究多聚焦固定目标（如 VDBO：vocals, drums, bass, other），难以扩展到任意乐器，且简单扩充输出词表会导致严重目标稀疏。
- 近期 query-based 方法（文本、音频、区域、多模态查询）虽可分离任意 stem，但依赖合适的手动查询，即便知道 ground truth 也难提供，限制大规模自动化 MSS。
- 盲源分离（blind）在语音/通用声场景已有探索，但音乐中源之间存在强时序与谐波相关性，此前无工作专门解决音乐盲分离。

## 方法创新
- 提出 MuS3D：一个 query-based 音乐源分离框架，可迭代发现混合中的活跃源。核心是 Stem Embedding Generator (SEG)，递归生成各 stem 的 query embedding，再送入 separator 提取目标源。
- SEG 基于条件流匹配（CFM）训练的 Transformer/DiT，生成一对 z0=[q_k, r_k]：下一源查询 q_k 与描述剩余源的 residual embedding r_k。通过求解 flow ODE，从 t=1 到 t=0 生成。
- 生成 residual 使递归自终止：无源剩余时 residual 槽输出固定 stop symbol s；当 ⟨r_k/||r_k||, s⟩ > τ_stop 时停止，并设最大迭代 16 作为回退。
- 训练：打乱 stems 顺序，均匀采样递归深度 k，单次前向监督任意阶段，无需展开整个递归，训练成本与 K 无关；残差目标为 ψ(m - Σ x_k) 或 stop symbol。
- 查询表示：PaSST（OpenMIC-2018 预训练）提取 embedding，PCA 降到 128 维（解释方差 0.96）。SEG 条件包括混合的 PaSST 表征与 DAC-VAE latents、已生成 queries；flow time、step counter、层级标志 h 通过 adaptive layer norm 注入。
- 分离器：DiT-Sep（基于 SAM-Audio large，约 2.2B 参数，CFM 训练，微调 300k iter，batch 16，EMA 0.9999）；BS-Locoformer（medium，band-split TF-Locoformer，通过 SwiGLU bias modulation 做 query conditioning，约 200k iter，batch 4）。

## 实验结果
- 数据：MoisesDB（11 broad groups / 38 fine instruments），补充 MedleyDB 125 首与 AlbumDB 10 首，279 训练 / 48 测试 / 26 验证。测试集 48 首歌切 10s 非重叠片段，共 1062 段；平均 4.5 个活跃 groups（1-8）或 7.0 个 instruments（1-15）。
- Stem discovery 评估：将 SEG 生成的连续 embedding 视为对 MoisesDB 分类体系的多标签分类任务，训练 hierarchical stem classifier 给 query 打标签；包含 Oracle 分类器上界。基线：从混合直接预测标签的多标签分类器，以及 MusicFlamingo 音乐理解语言模型。
- 摘要结论：在正确检测到的源上，MuS3D 匹配手动查询基线，并超越 state-of-the-art 文本模型。主观评价表明，当前生成式分离的瓶颈是编码伪影（encoding artifacts）。
- 作者认为 audio-based query representations 为源分离提供了有效且可自动化的接口。

## 一句话评价
MuS3D 首次系统性地将递归流匹配与 stem embedding 生成结合，为音乐盲源分离提供了无需外部信息或手动查询的自动化新范式，在正确检测源上达到手动查询基线水平，但生成式分离的编码伪影仍是实际音质上限。

---

## 9. Adapting Personalized Speech Enhancement for Low-Latency Audio-Visual Target-Speaker Extraction

**作者**: Rayhan Rashed, Senja Filipi, Ross Cutler
**链接**: [2609.30631](https://arxiv.org/abs/2609.30631)
**分类**: Audio-Visual Target-Speaker Extraction | **关键词**: Target-Speaker Extraction, Audio-Visual Speech Enhancement, Personalized Speech Enhancement, Low-Latency, Target Confusion, AV-HuBERT

## 核心痛点
- 在线音视频目标说话人提取（TSE）需要在去除竞争语音的同时保持语音质量并限制前瞻量。现有提取器大多基于合成混合音频构建和评估，其听音质量与真实会议场景中的行为未经验证。
- 个性化语音增强模型 PVQE 能以高质量重建目标语音，但在双说话人合成混合音频上，即使有干净注册语音，仍有 46% 的样本混淆目标（目标混淆，target confusion）。
- 与在线自回归音视频提取器 AVASE 相比，PVQE 输出的 DNSMOS 评分更高，但该评分器仅接收输出音频、无注册信息，无法判断恢复的是谁。

## 方法创新
- 提出 AV-PVQE（Audio-Visual Personalized Voice Quality Enhancement），从 PVQE 出发，在其说话人条件输入上加入嘴部特征，并与注册嵌入结合。
- 视觉前端采用 AV-HuBERT 卷积编码器提取嘴部特征（512 维投影到 176 维），按 AVASE 方式重复到音频帧率。
- 设计门控注册残差融合视觉与注册信息：g_t = sigmoid(W_g[b̄_t; e] + a_g)，r(e) = W2 ReLU(W1 e + a1) + a2，c_t = b_t + g_t ⊙ r(e)。其中 W2、a2 初始化为零，使融合初始等价于仅使用视觉特征。
- 训练策略：先训练视觉条件，再加入注册残差在 LRS3 和 VoxCeleb2 双说话人混合音频上继续微调；在线化处理使用运行均值替换整段聚合、重映射时间解码器滤波器到当前和过去输入、过去抽头初始化为零；最终阶段联合更新视觉路径、融合层和声学网络。
- 模型总参数量 12.79M，其中新增仅 0.40M。使用 16kHz 音频、20ms STFT 窗、10ms 帧移、88×88 灰度嘴部裁剪（25fps）。算法与缓冲延迟 20ms，满足 ICASSP 2023 DNS 低延迟限制，且无需未来音频或视频帧（因果流式已验证）。

## 实验结果
- 数据集：合成双说话人混合音频 LRS3、VoxCeleb2；真实会议语料 AMI、MCoRec、MTM（无需再微调）。测试集包含 3,000 对未见说话人。
- 目标恢复：
  - LRS3：AV-PVQE SI-SNRi 9.03 dB、Picked 98.38%，优于 AVASE（8.72 dB、96.83%）和 PVQE（-2.31 dB、54.17%）。
  - VoxCeleb2：AV-PVQE 5.65 dB、92.57%，优于 AVASE（3.81 dB、85.52%）和 PVQE（-2.97 dB、54.12%）。
  - AMI：AV-PVQE 6.99 dB、83.18%，显著优于 AVASE（2.56 dB、71.96%）和 PVQE（0.40 dB、57.01%）。
  - MTM：AV-PVQE 9.64 dB、90.34%，优于 AVASE（3.06 dB、76.99%）和 PVQE（-0.08 dB、51.99%）。
- 说话人数量鲁棒性（MTM）：在 2/3/4 说话人混合中 AV-PVQE 的 SI-SNRi 分别为 12.16/7.13/4.91 dB，Picked 分别为 93.33/91.15/75.00%，全面优于 AVASE（4.27/1.92/0.65 dB，84.10/72.57/56.82%）。
- 主观听音：个性化 P.835 测试中，相对 AVASE 整体质量 MOS 分别提升 0.57 和 0.63，与起始模型 PVQE 的平均评分相近。
- 保持与拒绝测试：无竞争语音时保持目标完整，目标缺失时抑制竞争语音。

## 一句话评价
AV-PVQE 通过将嘴部视觉线索以门控残差方式注入预训练个性化语音增强模型的说话人条件输入，并进行低延迟联合微调，在不牺牲听音质量的前提下将双说话人混合中的目标混淆率从 46% 降至 1.6%，并在合成与真实会议基准上同时超越自回归音视频提取器 AVASE 和原始 PVQE。

---

## 10. Seeing Speech: Learning Visible Articulatory Dynamics for Speech-Driven 3D Facial Animation

**作者**: Hyung Kyu Kim, Byungchan Hwang, Hak Gu Kim
**链接**: [2609.30517](https://arxiv.org/abs/2609.30517)
**分类**: Speech-Driven 3D Facial Animation | **关键词**: Speech-driven 3D facial animation, Visible articulation, Directional articulatory motion, Memory network, Topology-aware composition, Articulatory modeling

# Seeing Speech: Learning Visible Articulatory Dynamics for Speech-Driven 3D Facial Animation

**作者**: Hyung Kyu Kim, Byungchan Hwang, Hak Gu Kim (Chung-Ang University, Seoul, South Korea)  
**会议**: 40th Conference on Neural Information Processing Systems (NeurIPS 2026)  
**arXiv**: 2609.30517v1 [eess.AS] 24 Sep 2026

## 核心痛点
语音驱动的 3D 面部动画在顶点级重建质量上已取得进展，但生成语音一致的可见发音仍然困难。原因在于语音产生遵循结构化、受约束的发音器官协调，且声学到运动的映射本质上一对多：由于发音耦合和补偿机制，多种发音器配置可以产生相同的声学实现。现有方法（时序 CNN、Transformer 自回归预测、扩散去噪框架等）主要将任务视为整体面部运动回归，追求顶点或网格级重建质量，未显式建模语音产生背后的结构化发音运动，导致可解释性有限、物理基础薄弱。

## 方法创新
论文提出一种以可见发音结构为基础的 articulation-aware 框架。首先，基于五个可见网格表面锚点（上唇 UL、下唇 LL、左嘴角 LMC、右嘴角 RMC、下巴 Jaw），将可见发音定义为三个方向性发音运动：水平展开/圆唇（Spreading–Rounding, S）、垂直开合（Opening–Closing, O）、深度突出/后缩（Protrusion–Retraction, P）。跨代表性音素观察表明，可见发音不是任意的，而是遵循一致的方向主导运动模式。

框架包含两个核心组件：

1. **Speech–Articulatory Memory (SAM)**：通过键值记忆结构，在音素上下文下捕获语音与方向性发音运动之间的对应关系。SAM 使用声学桥接记忆 M_key 关联语音声学与发音模式，将 mel-spectrogram 编码为声学查询 q_t（带上下文查询头，聚合 2Ω+1 时间窗）；通过余弦相似度和缩放 softmax（τ_SAM=16.0）计算寻址向量 A_t。随后从三个可学习值记忆 M_val,δ（对应 S/O/P）检索方向性运动特征序列，每个记忆槽存储长度 2Ω+1 的特征序列以编码短期时间连续性。检索到的特征再经内容引导运动细化：使用自监督语音模型提取内容特征 f_cont，以内容特征为 query、检索序列为 key/value，通过各方向 Transformer 解码器进行时间交叉注意力，输出方向性发音运动序列。位置编码采用周期编码以捕捉时间周期性。

2. **Topology-aware Articulatory Composition (TAC)**：在面部网格拓扑下，将预测的方向性发音运动组合成表面一致的 3D 面部运动。TAC 确保可见发音在面部表面一致地实现，将方向性运动转化为顶点级 3D 运动。

## 实验结果
在 VOCASET 和 TFHP 数据集上进行实验。方法在标准重建指标上达到 state-of-the-art 性能，并改善了唇部发音的可见发音距离和速度误差。用户研究也确认，所提方法在唇同步和真实感方面获得明显偏好。论文声称其方法在性能和可解释性上均优于现有 SOTA 语音驱动 3D 面部动画模型。

## 一句话评价
该论文首次将语音驱动 3D 面部动画建立在结构化可见发音之上，通过方向性发音运动分解、记忆检索和拓扑感知组合，为生成物理一致、可解释的语音同步面部运动提供了新思路。

---

## 11. Asymmetric Classifier-Free Guidance for Target-Speaker ASR

**作者**: Yiwen Guan, Jacob Whitehill
**链接**: [2609.30476](https://arxiv.org/abs/2609.30476)
**分类**: Speech Recognition (Target-Speaker ASR) | **关键词**: Target-Speaker ASR, Classifier-Free Guidance, Whisper, Domain Adaptation, Inference-Time Calibration

## 核心痛点
- 目标说话人语音识别（TS-ASR）需要在重叠语音与噪声条件变化下识别并转写目标说话人；训练时学到的说话人条件在测试域发生偏移时可能不再最优。
- 现有 Whisper-based TS-ASR 多依赖 prompt 或条件模块，推理时条件强度固定，缺乏推理时校准机制。

## 方法创新
- 提出非对称无分类器引导（asymmetric CFG）用于 Whisper-based TS-ASR。
- 条件分支：输入混合语音与目标说话人注册语音，预测目标说话人转写；无条件分支：去掉注册语音，预测所有说话人的序列化转写（SOT，含 <sc> 说话人切换 token）。两分支共享全部模型参数。
- 训练目标：条件分支使用 hybrid CTC/attention loss；无条件分支以概率 p_u=0.1 丢弃注册语音，使用 SOT 与排列不变训练（PIT）选择较优说话人顺序。总损失为 L_asym = E[(1-b)L_TS + b L_SOT]。
- 模型结构：在 Whisper-small 编码器第 3、6、9 层后插入零初始化 cross-attention adapter，混合表示作 query，注册语音表示作 key/value；编码器末端附加线性 CTC head 提供帧级对齐监督。
- 推理解码：每个自回归解码步组合 logits，p_w = softmax(l_u + w(l_c - l_u))。w=0 为多说话人无条件解码，w=1 恢复标准目标说话人解码，w>1 放大目标条件差异。
- 域适应：冻结 ASR 模型，在目标域开发集上按网格 0.2~3.0、步长 0.2 搜索全局引导尺度 w_g，最小化语料 WER；再训练轻量预测器进行句级调整，动作集 A={w_g-δ, w_g, w_g+δ}，预测 WER 变化与收益概率，仅当置信度和预测 WER 降低超过阈值 (τ,m) 时调整尺度，详见 Algorithm 1。

## 实验结果
- 数据：Libri2Mix clean，训练使用 LibriSpeech train-clean-100；LSM-controlled 开发/测试集分别为 5,406 与 5,240 条，重叠比例 30%/50%/70%；在 OV50 下加入 WHAM! 噪声，SNR 为 10 dB 与 0 dB。注册语音为随机裁剪的 3 秒 LibriSpeech 录音。
- 指标：TS-ASR 报告目标说话人 WER，多说话人 ASR 报告 cpWER，均为语料级。
- 设置：Whisper-small 骨干，60 epochs，AdamW，batch size 8，预训练参数学习率 1e-5，新增参数学习率 1e-4，p_u=0.1，α=0.5。
- 主要结果：在域偏移下，完整系统相对 condition-only baseline 最高取得 21.8% 的相对 WER 降低，相对同一 CFG 训练模型的标准条件解码降低 5.6%。最佳 TS-WER 为 15.66%。Oracle 分析表明句级尺度选择仍有更大提升空间，且有益调整随域偏移而变化。

## 一句话评价
首次将非对称 CFG 用于 TS-ASR 推理时校准，方法简洁且有效，在受控域偏移下显著降低 WER；但目前验证限于 Whisper-small 与 Libri2Mix 受控设置，真实复杂场景下的泛化仍需进一步验证。

---

## 12. TinyAudio: Compact and Efficient Text-to-Audio Generation for Low-Resource Deployment

**作者**: Junxi Liu, Xiquan Li, Wenhao Guan, Yifan Duan, Zhikang Niu, Yanru Huo, Ziyang Ma, Xie Chen
**链接**: [2609.31525](https://arxiv.org/abs/2609.31525)
**分类**: Text-to-Audio Generation | **关键词**: Text-to-Audio Generation, Flow Matching, Compact Generative Models, Low-Resource Deployment, MeanFlow, Audio-Text Contrastive Learning

# TinyAudio: Compact and Efficient Text-to-Audio Generation for Low-Resource Deployment

## 核心痛点
- 文本到音频（TTA）生成在质量和指令遵循上进步显著，但代表性系统通常需要约十亿参数，内存和推理延迟高，难以部署到资源受限设备。
- 仅减少采样步数（如 TangoFlux、MeanAudio）不能减小模型大小；构建紧凑 TTA 模型还需高效设计文本条件、潜变量生成和波形重建。

## 方法创新
1. **整体架构**：TinyAudio 总计 87M 推理参数，比十亿级 pipeline 减少 90% 以上，峰值 GPU 显存仅 0.48 GB。包含：32M TA-CLAP 文本编码器、35M TA-DiT 生成器、20M TA-VAE 解码器。
2. **TA-VAE**：紧凑音频潜变量表示。DAC 风格卷积编码器 + 轻量 anti-aliased multi-periodicity (AMP) 解码器；对 44.1 kHz 波形采用 1024× 时间压缩，得到 64 通道、43 Hz 潜序列。训练用 7M 编码器产生归一化潜目标，推理仅保留约 20M 解码器重建波形。
3. **TA-CLAP**：轻量音频对齐文本编码器。文本编码器由 Ettin-encoder-32m 初始化，与预训练 HTSAT 音频编码器组成双编码器，通过 SigLIP pairwise sigmoid loss 做音频-文本对比学习；对比适配后丢弃音频分支，仅保留文本分支。
4. **TA-DiT**：轻量单流音频生成 Transformer。将投影后的文本 token 与噪声音频潜变量拼接为 H=[A;Y] 进行联合自注意力，跨模态共享注意力参数；对音频和文本 token 分别应用独立索引的 RoPE，并使用 QK-Norm 提升训练稳定性。进一步在所有 Transformer 块间共享条件调制网络 M_ss 和 M_g，仅用块特定嵌入 e^l_ss、e^l_g 保留深度行为；注意力和前馈参数仍层特定。最终仅保留音频 token 输出，投影为潜速度预测，采用 flow-matching 目标。
5. **质量感知 SFT**：按 AudioBox Aesthetics 筛选样本（PQ≥5.5、CE≥3.5、CU≥4.5），按 HTSAT 预测分为音乐/语音/一般声音，比例约 1:1:3；每类取 LAION-CLAP 相似度最高样本，保留 2–30 秒录音并按路径去重，得到约 417K 高质量对。
6. **TinyAudio-MF**：基于 Improved Mean Flows 的一步加速模型。从预训练 500K 步的 TinyAudio checkpoint 初始化，在质量感知 SFT 子集上继续训练，将 25 步 Euler 采样减少为 1 次函数评估，可在四核 CPU 配额下实现实时生成。

## 实验结果
- **数据与评估**：基础训练语料约 3.7M 音频-文本对，来自 AudioCaps、AudioSet、Clotho、VGGSound、WavCaps、MusicCaps、AudioStock2；SFT 子集约 417K 对。AudioCaps 验证/测试音频被排除。评估在 AudioCaps 测试集（10 秒生成）和 TTA-Bench Accuracy 子集（1,500 prompts）上进行。
- **训练细节**：TA-CLAP 训练 10 epochs，batch 1024；TA-VAE 训练 500K steps，batch 64；TA-DiT 使用 18 个 Transformer 块、hidden 384、8 个注意力头。生成器预训练 500K steps，质量感知 SFT 再 200K steps，batch 均为 1024；局部/全局文本条件以 0.1 概率联合丢弃以学习 CFG 的无条件场。
- **主要结果（表 1）**：
  - TinyAudio：生成器 35M，部署总参数 87M，峰值显存 0.48 GB，NFE 25×2，RTF 0.078；AudioCaps FAD 2.65、KL 1.32、IS 10.44；TTA-Bench CE 3.343、CU 5.262、PC 2.983、PQ 5.996、CLAP 0.429。
  - TinyAudio-MF：1 NFE，RTF 0.010；AudioCaps FAD 2.83、KL 1.49、IS 8.47；TTA-Bench CE 3.350、CU 5.257、PC 3.043、PQ 5.994、CLAP 0.403。
  - 对比 AudioLDM-L-Full、AudioLDM2-Large、Tango-Full、Tango-2-Full、MeanAudio-L-Full、EzAudio-XL、GenAU-L-Full、TangoFlux、Resonate 等，TinyAudio 参数量和显存大幅降低，质量具有竞争力。
- **主观评估（表 2）**：TinyAudio 的 OVL 为 3.560±0.985，REL 为 3.520±0.940；TangoFlux 为 3.505±0.989 / 3.600±0.992；EzAudio 为 3.155±1.169 / 3.190±1.169；AudioLDM 为 3.015±1.004 / 2.730±0.962。
- **组件消融（表 3）**：Base FAD 2.494、KL 1.399、IS 10.695；Per-block AdaLN FAD 2.658；Dual-stream MMDiT FAD 3.168；w/o CLAP adaptation FAD 4.051、KL 1.593、IS 8.466，表明音频对齐文本条件与单流/共享调制设计重要。
- **SFT 与数据选择消融（表 4）**：Pretraining only FAD 2.471、KL 1.362、IS 10.231；Random SFT FAD 3.412、KL 1.401、IS 9.891；Quality-Aware SFT FAD 2.651、KL 1.322、IS 10.442，质量感知选择优于随机，KL 与 IS 更优。
- **效率**：TinyAudio-MF 在四核 CPU 配额下达到稳态 RTF 0.715，实现实时生成。

## 一句话评价
TinyAudio 通过单流 TA-DiT、层共享条件调制、音频对齐文本编码器、紧凑 VAE 与质量感知 SFT，把 TTA 模型压缩到 87M 参数和 0.48 GB 显存，并以 MeanFlow 实现一步实时生成，在低资源 TTA 部署中取得有竞争力的质量-占用权衡。

---

## 13. Acoustic-to-Text KV Compression for Full-Duplex Speech Models

**作者**: Yejin Lee, Seungbeom Kim, Yongha Lee, Kyuhong Shim
**链接**: [2609.31224](https://arxiv.org/abs/2609.31224)
**分类**: Full-Duplex Speech Language Models | **关键词**: full-duplex speech model, KV cache compression, acoustic-to-text compression, listening-time slack, knowledge distillation, LoRA, long-context speech understanding

## 核心痛点
- **长时全双工语音交互的内存瓶颈**：全双工语音语言模型在持续对话中不断累积声学 key–value (KV) 状态，语音表示占用的序列位置远多于文本（约 **17 个位置/秒** vs 转录文本约 **3 个位置/秒**），长时运行交互显存开销极大。
- **峰值显存无法靠事后压缩解决**：仅在输入处理完成后才做压缩，无法降低输入处理期间已经产生的峰值显存；流式交互要求全程控制峰值 KV cache 用量。
- **保行为与加能力的矛盾**：为记忆而引入的转录能力若只做 ASR 监督训练，会破坏模型原生的 listening / speaking 行为（何时停顿、抢话、被打断）。

## 方法创新
1. **Acoustic-to-Text KV Compression（声学到文本的 KV 压缩）**：利用 **listening-time slack**——模型处理完一个音频单元、下一个单元尚未到达之间的空档（本文设置约 **900 ms**）——引入 **transcription side channel**，把到来的语音增量地转成紧凑的文本记忆。每个转录段由新引入的 `<|asr start|>` / `<|asr end|>` 特殊 token 界定，转录 token 保留在语言模型上下文中，但被排除在语音解码器输入与口头输出之外。
2. **流式驱逐策略**：当常驻 KV cache 超过目标预算时，驱逐较老的声学状态，保留转录 token 与一个**近期声学窗口**（用于容忍转录延迟）。保留的转录承载早期语音的语言内容，近期声学上下文继续支撑即时交互；侧通道复用原语言模型 backbone，推理时**不需要独立的 ASR 模型**。
3. **训练策略（LoRA + 行为蒸馏）**：
   - 用词级强制对齐构造转录目标：对词 w_i 及其声学端点 e_i，按 k_i = ⌈(e_i+δ)/Δ⌉ 分配到单元，每个词仅出现在一个目标段中。
   - 以冻结的原始模型为教师（处理同一音频但无转录段），在**原生预测位置**做 token 级知识蒸馏，师生按“预测事件”而非序列下标对齐（插入段会错位下标）。
   - 总损失 L = L_ASR + L_native + L_dec + L_turn：L_ASR 为转录 token 及其分隔符的掩码交叉熵；L_native 为温度 T=1 下逐位置前向 KL（T²D_KL(P_T^T‖P_S^T)）；L_dec / L_turn 为**组平衡辅助损失**（分别按 listen/speak/other 与 turn-end/turn-continuation 分组，先组内平均再跨组平均），避免低频决策与轮次边界被平均掉。
   - 仅需短转录语句训练，无需长语音或全双工交互数据采集。

## 实验结果
- **内存/缓存**：10 分钟 LongSpeech 会话（每任务 100 段）上，相比同一 adapted 模型不驱逐，峰值流式 KV cache 降低 **64.6%**；Listening 常驻位置 **12.3K → 4.0K**，Query 期间 **10.4K → 1.8K**。
- **长语音理解全面提升**（对比原生流式）：WER **96.9 → 12.9**；Temporal QA 准确率 **30.0 → 42.0**；Summarization BLEU **2.7 → 11.0**、R-1 **27.3 → 49.0**。与外部 ASR 级联相比（Whisper-tiny 15.9 / FastConformer 流式 10.3 / Whisper-large-v3 9.35，参数量 39M / 115M / 1.55B），本方法仅用 **43.7M** 可训练参数即达到接近或更优的综合表现（WER 12.9，R-1 49.0）。
- **效率**：4K KV 预算下，含转录与缓存驱逐的处理平均 **461 ms/秒音频**（H100，batch size 1），10,039 个测量单元**无 deadline miss**。
- **全双工交互**：Full-Duplex-Bench v1.0 上 pause-handling、turn-taking、interruption 与基线相当（TOR 0.218 vs 0.000，pause latency 1.965 s vs 1.944 s，turn-taking score 4.54 vs 4.65，interruption TOR 0.940 / latency 1.820 s）。**消融**：去掉蒸馏、仅用转录交叉熵时行为崩溃（backchannel TOR 0.982、pause latency 0.000、turn-taking score 0.19），说明原生预测位置蒸馏是保住全双工行为的关键。

## 一句话评价
用“在听力空档做增量 ASR、以文本记忆替换被驱逐的声学 KV”这一简洁而有效的思路，在几乎不损害全双工听说行为的前提下把流式峰值 KV cache 压缩约 2/3，并同时提升长语音理解质量，是面向长时语音交互的实用型记忆压缩方案。

---

## 14. Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs

**作者**: Jihoo Jung, Youngjoon Jang, Joon Son Chung
**链接**: [2609.31193](https://arxiv.org/abs/2609.31193)
**分类**: Audio-Visual Large Language Models (AVLLMs) | **关键词**: Audio-Visual LLMs, Trimodal Binding, Symbolic Binding IDs, Active Speaker Detection, Visual Prompting, Multi-speaker Video Understanding, Mechanistic Interpretability

# 论文总结：Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs

## 核心痛点
- 当前 Audio-Visual LLMs (AVLLMs) 在多说话人对话视频中难以稳定完成“谁说了什么”的推理。
- 该任务要求文本-音频-视觉三模态绑定：把说话人的视觉身份、屏幕空间位置、语音内容与说话时间顺序关联到同一实体。
- 已有工作主要研究 LLM 的实体-属性绑定和 VLM 的图文绑定，AVLLM 中更复杂的三模态绑定机制仍未被系统解释。
- 关键诊断问题是：失败究竟来自文本到音频/视觉的 grounding，还是直接来自音频-视觉对齐。

## 方法创新
- 系统分析四类 AVLLMs：video-SALMONN2+ (7B)、Qwen2.5-Omni (3B, 7B)、MiniCPM-o-4.5 (9B)。
- 构建单镜头多说话人 toy dataset：四个动物角色随机出现在四个象限，按随机顺序说不同国家名；每个语音事件由 (v_i, p_i, a_i, t_i) 表示。
- 定义 trimodal binding tasks：(1) Acoustically-Anchored Visual Retrieval (AAVR)：给定语音 anchor 预测说话人视觉属性；(2) Visually-Anchored Audio Retrieval (VAAR)：给定视觉 anchor 预测对应语音内容。
- 发现 AVLLMs 使用模态特定 symbolic IDs：听觉属性对应 temporal IDs（何时说），视觉属性对应 spatial IDs（何处/谁在说）。
- 提出三阶段符号绑定机制：(i) anchor ID retrieval：文本 anchor 映射到其 symbolic ID；(ii) target ID selection：将该 ID 映射到互补模态 target 的 symbolic ID；(iii) feature retrieval：按 target ID 提取语义特征。
- 失败分析表明，三模态绑定错误主要发生在 target ID selection 阶段，反映当前 AVLLMs 音频-视觉对齐存在根本不足。
- 方法创新：利用 off-the-shelf Active Speaker Detection (ASD) 模型，在活跃说话人上叠加 bounding box 作为视觉提示；该 audio-visual prompting 无需训练即可提升性能，并可结合少于 300 步的轻量微调。

## 实验结果
- Training-free ASD prompting 在四个以对话为中心的 benchmark 上取得即时性能提升（Qwen2.5-Omni 和 MiniCPM-o-4.5）。
- 在 ASD-prompted videos 上轻量微调少于 300 步后，conversation-centric 数据集准确率提升：video-SALMONN2+ 7.9%，Qwen2.5-Omni 9.7%，MiniCPM-o-4.5 3.5%。
- 方法可泛化到三个额外通用 AV benchmark，说明不仅适用于对话场景。
- 机制分析结合表征相似性分析 (RSA) 和因果中介分析：anchor token 在中间到后层出现 anchor ID 表征；last token 在后层出现 target ID 选择，最深层出现语义特征提取。

## 一句话评价
- 本文首次系统揭示 AVLLMs 的符号三模态绑定机制，将“谁说了什么”的失败精确定位到音频-视觉 target ID 选择瓶颈，并用简单 ASD 视觉提示在无需训练和轻量微调两种设定下有效缓解。

---

## 15. BAT-CLIP: Trimodal Alignment of Brain, Audio and Text

**作者**: Suhyun Kim, Jinmo Han, Danny Dongyeop Han, Ahhyun Lucy Lee, Jewoon Lee, Yonghyeon Gwon, Zach Paris, Chun Kee Chung, Saewoong Bahk, Nam Soo Kim, Seong Jae Hwang, Jiook Cha
**链接**: [2609.31180](https://arxiv.org/abs/2609.31180)
**分类**: Brain-Speech Alignment / iEEG Decoding | **关键词**: iEEG/ECoG, Brain-Speech Alignment, Trimodal Contrastive Learning, AudioCLIP, DIVER-1, Speech Representation Learning

# BAT-CLIP: Trimodal Alignment of Brain, Audio and Text

## 核心痛点
- 现有 CLIP 风格脑-语音对齐通常只锚定单一模态：音频或文本。
- 音频锚定保留时序与声学结构，但语言可分性较弱；文本锚定语义强，但丢失声学细节。
- 大脑语音理解本身是多模态整合过程，单锚定会带来表征权衡。
- iEEG 配对数据有限，训练容易过拟合，且已有方法未充分利用自监督脑基础模型先验。

## 方法创新
- 提出 `BAT-CLIP`，首个面向 iEEG 的 CLIP 风格三模态对齐框架，将神经表征同时对齐到冻结的音频与文本锚点，共享 AudioCLIP 的音频-文本流形。
- 脑编码器 `fθ` 从 iEEG 自监督基础模型 `DIVER-1` 初始化，作为对齐先验，缓解低数据过拟合；后接两层 MLP 投影到 1024 维共享空间并做 ℓ2 归一化。
- 音频/文本锚编码器 `gφ*`、`hψ*` 来自预训练 `AudioCLIP` 并保持冻结，避免低数据场景下锚空间共适应。
- 三模态对比目标：分别计算 Brain-Audio 与 Brain-Text 双向交叉熵损失，并求和：
  - `L_BA = 1/2 [CE(S_BA, y) + CE(S_BA^T, y)]`
  - `L_BT = 1/2 [CE(S_BT, y) + CE(S_BT^T, y)]`
  - `L_Total = 1/2 (L_BA + L_BT)`
  - 相似度 logit `S = α Z Z^T`，缩放因子 `α = 14.3`，用于锐化 logit 分布并稳定优化。
- 数据处理：iEEG 降采样以匹配 DIVER-1；音频重采样至 44.1 kHz 供 AudioCLIP；文本用 AudioCLIP tokenizer。iEEG 窗口为 1.0 s，按 50 采样点（0.1 s）非重叠 patch 输入 transformer。

## 实验与结果
- 数据与基准：使用 `Podcast` 颅内电生理数据集，受试者自然被动听故事，含词级时间对齐转录与语言/声学特征；采用 `Podcast Benchmark` 评估套件。
- 基线/变体：
  - 全微调监督 CNN 基线；
  - 脑基础模型 `BrainBERT`、`PopT`、`DIVER-1`；
  - 对齐变体：`BA-CLIP`（Brain-Audio）、`BT-CLIP`（Brain-Text）、`BAT-CLIP`（三模态），均基于 DIVER-1 初始化。
- 评估任务（6 个探针）：Content、Onset、POS、GPT Surprisal、Word Embedding、Whisper latent decoding；指标为 AUC / AvgAUC / Acc。
- 主要结果（9 名受试者平均）：
  - 未对齐 `DIVER-1` 是 strongest foundation-model baseline，线性探针下优于 CNN 等。
  - CLIP 对齐通常优于 DIVER-1；`BAT-CLIP` 在 POS、GPT Surprisal、Word Emb、Whisper 上优于 `BA-CLIP` 和 `BT-CLIP`，在 6 个探针中的 5 个取得最佳对齐变体结果。
  - Content 探针上 `BA-CLIP` 略优于 `BAT-CLIP`；Onset 任务上 CNN 和未对齐 DIVER-1 仍最强，CLIP 对齐反而下降。
  - 相较监督 CNN 基线，`BAT-CLIP` 在 Content +5.96%、POS +1.50%、GPT Surprisal +4.21%、Word Emb +5.01%、Whisper +8.09%；Onset -12.18%。
- 预训练消融：比较 Scratch 与 DIVER-1 初始化，显示自监督预训练脑基础模型对可靠三模态对齐至关重要；Scratch 版本性能明显更差（例如 BAT-CLIP Scratch 在 Whisper 上 -2.36%，而 DIVER-1 初始化 +8.09%）。

## 一句话评价
BAT-CLIP 将 iEEG 神经表征同时锚定到冻结的音频-文本共享流形，以三模态对比学习缓解单锚定权衡；在 Podcast Benchmark 上，三模态对齐整体优于双模态 CLIP 变体，并强调了 SSL 脑基础模型初始化在低数据对齐中的关键作用。

---

## 16. BreathGRU: A Novel Semi-Supervised Bidirectional Gated Recurrent Unit Framework for Speech and Breath Segmentation for Respiratory Audio

**作者**: Sania Fatima Sayed, John W. Holloway, Reyer Zwiggelaar, Faisal I. Rezwan
**链接**: [2609.31165](https://arxiv.org/abs/2609.31165)
**分类**: Respiratory Audio Segmentation | **关键词**: BreathGRU, BiGRU, Speech-Breath Segmentation, Respiratory Audio, Semi-Supervised Learning, VAD

# BreathGRU 论文总结

## 核心痛点
- 呼吸音频分析中，语音-呼吸分割是基础预处理步骤，直接影响呼吸声学生物标志物提取、肺功能预测和疾病监测。
- 现有方法包括阈值法、傅里叶变换方法、无监督学习和预训练 VAD 模型（如 Silero、PyAnnote），主要关注语音检测，常将吸气、呼气等呼吸事件归类为非语音或静音，限制精确呼吸检测。
- 现有方法较少建模呼吸信号的生理特性，如时间连续性、预期呼吸时长和语音-呼吸边界定位。

## 方法创新
- 提出 BreathGRU：一种半监督双向门控循环单元（BiGRU）框架，专门用于语音和呼吸分割。
- 框架包含五个组件：声学特征提取、双向循环建模、帧级分类、半监督训练、时长约束的分段 Viterbi 解码。
- 声学特征：音频重采样到 16kHz；25ms 分析窗、10ms 帧移；每帧 59 维特征，包括 13 维 MFCC、13 维一阶差分、13 维二阶差分和 20 维 Mel 频谱带；使用 Z-score 标准化。
- 网络结构：两层 BiGRU，每个方向 96 个隐藏单元；前向 GRU 捕获历史上下文，后向 GRU 捕获未来上下文，拼接后用于帧级分类。
- 分类头：Layer Normalisation、全连接层、ReLU、dropout（p=0.3）和 Softmax，输出语音与呼吸两类概率。
- 半监督策略：利用已标注和未标注录音，结合伪标签精炼与时长约束的 Segmental Viterbi 解码，生成最终分割。

## 实验与结果
- 数据集：453 段语音录音，来自 44 名临床诊断哮喘患者，均在支气管高反应性测试后采集；27 名患者 354 段录音来自澳大利亚 Newcastle 大学，17 名患者 99 段录音来自英国 Southampton 大学；受试者阅读 Rainbow Text 或 A Winter Book 段落约一分钟。手工标注语音和呼吸片段作为 ground truth。
- 外部泛化评估：Coswara 数据集 5 段不同患者慢速/快速计数片段，以及 5 段不同 TED 演讲的 60 秒片段。
- 评价指标：基于事件、时间、重叠、时长和边界的多种分割指标。
- 主要结果：BreathGRU 获得最高呼吸事件召回率 0.83、最低起始定位误差 0.14s、最高 Mean Match IoU 0.81；整体分割性能与 Silero 等大型预训练 VAD 模型具有竞争力。
- 定性评估：BreathGRU 与人工标注高度一致，呼吸检测优于 Silero；在 Coswara 和公开录音上表现一致，能适应不同录音条件和说话人口音。
- 结论：显式建模呼吸事件优于通用 VAD，BreathGRU 可作为呼吸音频分析和肺部健康应用的有效语音-呼吸分割框架。

## 一句话评价
BreathGRU 通过 BiGRU、半监督伪标签精炼和时长约束 Viterbi 解码，将呼吸事件从语音/静音中显式分离，在呼吸事件召回和边界定位上优于传统方法与通用 VAD，但其临床泛化能力仍需更大规模、多中心数据进一步验证。

---

## 17. Synth-JEPA: Joint Embedding Prediction for Renderer-Free Synthesizer Parameter Search

**作者**: Ben Hayes, Haokun Tian, Stefan Lattner
**链接**: [2609.31024](https://arxiv.org/abs/2609.31024)
**分类**: Audio Synthesis / Sound Matching (Synthesizer Inversion) | **关键词**: sound matching, synthesizer inversion, joint embedding predictive architecture, renderer-free search, synthesizer parameter search, audio representation learning, SIGReg

# Synth-JEPA 论文总结

## 核心痛点
- 声音匹配（sound matching）可形式化为在音频域目标下优化合成器参数，但来自通用音频表示（如 log-Mel、EfficientAT、CLAP）的目标往往难以优化，且与合成器参数-声音之间的对应关系无关。
- 直接搜索需要为每个候选参数调用合成器渲染音频，计算成本高；学习代理目标虽能减少渲染，但搜索质量同时受代理精度和音频表示选择影响。
- 合成器逆映射通常病态：不同参数配置可能产生相似甚至等价的声音信号。

## 方法创新
- 提出 Synth-JEPA：一种联合音频-参数预测模型，用作无渲染器（renderer-free）合成器参数搜索目标。模型学习相互预测的音频表示和参数表示，使音频嵌入空间的几何由参数-音频对应关系塑造，而非通用音频相似度。
- 训练：音频编码器 E_a 将音频 y 映射为 z_a，参数编码器 E_p 将参数 x 映射为 z_p；跨域预测器 f_{a→p} 与 f_{p→a} 进行双向预测；损失为 L_pred = MSE(ẑ_p, sg(z_p)) + MSE(ẑ_a, sg(z_a))，其中 sg 为 stop-gradient。
- 防坍缩：主方法使用 SIGReg（来自 LeJEPA）将编码器输出分布正则化到各向同性高斯，并分别作用于音频和参数分支；另训练 EMA teacher 变体（SLAP 风格）进行对比。
- 推理：目标音频只编码一次 z*_a = E_a(y*)，候选参数通过 D_JEPA(y*, x) = MSE(z*_a, f_{p→a}(E_p(x))) 打分，无需调用合成器。
- 优化：采用两阶段混合搜索。第一阶段用 JADE 进化 32 个候选，连续参数进行变异与交叉，离散参数复制或重采样；第二阶段对 D_JEPA 评分最好的 8 个候选，用 Adam（初始学习率 0.1，余弦衰减到 0）对其连续参数进行梯度精修，期间三次均匀剪枝，每次丢弃表现较差的一半，最终返回唯一候选。
- 模型结构：音频编码器为 Transformer，输入 stereo log-Mel（128 bands，25 ms window，10 ms hop），经 1D 卷积投影为 150 tokens，拼接 learned summary token，输出 z_a ∈ R^512；参数编码器对每个参数使用线性投影加参数特定 bias，经 Perceiver bottleneck（32 个 learned latents）交叉注意力，接 8 个 self-attention blocks，平均输出 z_p ∈ R^512；预测器为 3-block residual MLP，hidden width 1024。总参数 53M。
- 数据与训练：使用 Surge XT，采用 139 个活跃参数，禁用音频效果及已知引入非确定性的调制器（如 Sample & Hold）。训练时在线渲染 44.1 kHz stereo、3.0 秒音频。用 Welford 在线算法估计前 8k 训练频谱的通道均值和方差并冻结。训练 1M steps，batch size 64，AdamW，学习率 3e-4，warmup-stable-decay，weight decay 0.05。

## 实验结果
- 数据集：域内 Surge XT held-out presets；域外 NSynth 和 FSD50K（各 1024 个目标，裁剪到前 3s，重采样到 44.1 kHz，上混到 stereo）。
- 指标：MSS↓、wMFCC↓、CLAP↑。搜索类方法预算为 2048 次目标评估，flow matching 使用 20 ODE steps；墙钟时间在 RTX 3090 上按目标测量。
- 主要结果：Synth-JEPA（SIGReg）在域内所有指标上取得最优；在域外 NSynth 和 FSD50K 上保持竞争力，多数指标最优或次优，仅 wMFCC 上 log-Mel 基目标领先。SIGReg 变体在所有数据集和指标上均优于 EMA teacher 变体，说明防坍缩机制对优化几何有实质影响。
- 与摊销基线比较：优于 AST Regression 和 Flow Matching。Flow Matching 随 ODE solver steps 增加快速提升，但在约 16 步后基本饱和；Synth-JEPA 虽需更多时间达到同等性能，但随搜索预算增加持续改进，表明额外测试时计算通过目标特定搜索比通过更精确的摊销推理更有效。
- 与 renderer search 比较：学习到的 E_a 表示在 renderer-in-the-loop 设置中取得最强 MSS 结果，表明参数诱导的嵌入几何本身有益于搜索。Synth-JEPA 在域内和 NSynth 上广泛优于两个 proxy 基线，但在 Freesound 更宽的音频分布上表现更混合。
- 推理时缩放：可通过可选 best-of-k 渲染候选并选择 log-Mel L1 距离最小者进一步缩放测试时计算（此时并非严格 renderer-free）。
- 听感测试：在成对听感测试中，听众总体在 85% 的试验中偏好 Synth-JEPA。

## 一句话评价
Synth-JEPA 通过联合音频-参数预测学习由参数对应关系塑造的嵌入空间，实现了无需渲染候选音频的可微参数搜索，在域内声音匹配上显著优于摊销模型、直接搜索和学习代理基线，并支持用测试时计算换取匹配质量。

---

## 18. Tracing and Relearning Detection Evidence in Text-to-Speech Systems

**作者**: Eunji Shin, Kyudan Jung, Jihwan Kim, Minwoo Lee, Jaegul Choo
**链接**: [2609.30983](https://arxiv.org/abs/2609.30983)
**分类**: Audio Deepfake Detection | **关键词**: audio deepfake detection, text-to-speech, controlled resynthesis, detector adaptation, F5-TTS, BigVGAN, acoustic model fine-tuning, equal error rate

## 核心痛点

现有音频深度伪造检测器在标准基准上能达到较低等错误率（EER），但尚不清楚TTS系统的哪个阶段提供了检测证据。基准测试变化了欺骗系统的声学模型和波形生成、源语料和信道条件，低EER只能说明检测器在某个协议下分开了合成与真实语音，却不能说明它利用了哪个因素。检测器可能利用与合成无关的静音时长线索，而声码器对真实梅尔谱的重建本身就可能与源话语可分。在TTS输出中，声码器接收的是声学模型生成的梅尔谱，而非从语音中提取的，因此基准EER无法将分离归因于任一阶段。

## 方法创新

本文在F5-TTS–BigVGAN流水线中通过受控重合成和检测器自适应来追踪检测证据。

1. **受控重合成与条件定义**：对同一源话语和目标文本定义五种条件：R（重采样源至24kHz）、V（从源提取真实梅尔并用BigVGAN重建）、T（基础F5-TTS DiT生成梅尔+同一BigVGAN）、FT（微调后的DiT替换基础DiT）、TG（对T输出施加标量增益以匹配FT的RMS幅度）。R–V差异归因于BigVGAN重建，V–T保持同一声码器但用DiT生成的梅尔替换源梅尔，覆盖韵律和声学实现差异以及生成证据，T–TG隔离电平单独可产生的部分。

2. **声学模型微调**：微调全部3.371亿DiT参数，冻结BigVGAN但保持其可微，使波形上的判别器损失能回传到DiT。联合训练的判别器从随机初始化开始，结合5个多周期判别器（周期2,3,5,7,11）和3个多分辨率判别器（傅里叶尺寸2048,1024,512）。真实目标为真实梅尔的BigVGAN重建，假输入为DiT生成梅尔的BigVGAN输出。采用HiFi-GAN的最小二乘对抗和特征匹配公式，损失权重分别为1和2，无梅尔重建损失，评估检测器不在目标中。

3. **检测器自适应**：从XLS-R SLS检查点开始，用FT标记为合成继续训练，在自适应集中每个FT样本与其提示和转录的真实话语配对，内容和说话人不能作为标签线索。自适应运行不包含T样本，因此到基础F5-TTS的迁移是被测量的而非训练的。

## 实验结果

- **分离主要出现在BigVGAN下声学生成之后**：R在两种语料上接近随机水平；V降低SLS和Mamba的EER；从V到T的进一步下降在LibriSpeech上约为R–V步骤的3倍，在VCTK上为8–9倍。AASIST-L通过不同前端读取波形，其全部下降出现在T。对于SLS，Vocos重建的分离远强于BigVGAN（表2），说明V的分离大小依赖声码器。

- **微调在RMS增益匹配之外提高EER**：FT在所有六个检测器–语料对中相对T提高EER，超过生成种子间的波动，范围从SLS在VCTK上的0.64个百分点到AASIST-L在LibriSpeech上的18.92个百分点。TG隔离电平影响：在LibriSpeech上，RMS增益匹配解释了SLS的T–FT差距的52%、Mamba的30%；在VCTK上TG几乎不变。AASIST-L对电平更敏感，在LibriSpeech上TG解释了64%的差距。所有六对中仍存在高于TG的残差。

- **质量与内容度量保持可比**：UTMOS、说话人相似度和WER在三个语料上的变化很小，最大退化在或接近生成种子波动范围内，说明EER增加并非来自输出退化。

- **检测器自适应学习微调输出并迁移**：LibriSpeech自适应将LibriSpeech上的FT EER从19.42%降至1.71%，VCTK上从4.09%降至0.20%；VCTK自适应将LibriSpeech上降至7.46%，VCTK上降至0.10%。T在两次运行中也降至可比EER，尽管自适应仅将FT标记为合成。两种语料都能教检测器分离FT，遗留EER在不同自适应语料间存在差异。

## 一句话评价

本文通过受控重合成和检测器自适应，将TTS深度伪造检测证据主要归因于声学生成阶段，并证明对抗微调可在不降低质量的情况下削弱固定检测器的证据，而检测器自适应又能恢复对更新输出的检测，为深度伪造检测的归因和鲁棒性评估提供了重要视角。

---

## 19. Training-Free Pronunciation Transcription via Text-Constrained Acoustic Rescoring

**作者**: Hikaru Asano, Yotaro Kubo, So Kuroki
**链接**: [2609.30924](https://arxiv.org/abs/2609.30924)
**分类**: Pronunciation Transcription (Speech-and-Text-to-Pronunciation, TTS Data Preparation) | **关键词**: pronunciation transcription, training-free inference, CTC rescoring, grapheme-to-phoneme conversion, speech-to-pronunciation, greedy search, text-constrained acoustic rescoring, TTS data preparation

## 论文信息
- **标题**: Training-Free Pronunciation Transcription via Text-Constrained Acoustic Rescoring
- **作者**: Hikaru Asano (The University of Tokyo / Sakana AI), Yotaro Kubo (Sakana AI), So Kuroki (Sakana AI)
- **任务**: 发音转写（Pronunciation Transcription），即以语音 x 与其转写文本 w 为输入，估计语音中**实际说出**的发音序列 y，而非其规范读音。

## 核心痛点
1. **数据规模需求**：发音转写是 TTS 训练数据准备的关键环节，需要在**低成本**下保持**低错误率**以支撑大规模数据生产。
2. **现有范式各有缺陷**：
   - **G2P**（grapheme-to-pronunciation）：只用文本，忽略声学信息，无法消解同形异读（如日语「明日」可读 asu / ashita / myōnichi）。
   - **S2P**（speech-to-pronunciation）：只用语音，忽略文本所允许的合法读音范围。
   - **ST2P**（speech-and-text-to-pronunciation，(x,w)→y）：联合二者，但**需要昂贵的发音标注数据**（(x,w,y) 三元组）进行训练，可扩展性受限。

## 方法创新
提出**免训练（training-free）的 ST2P 流水线**，仅在推理阶段融合词汇约束与声学证据：

1. **候选生成（文本侧）**：将转写 w 按形态学分析切分为 N 个 span；对每个 span n，由词典 / G2P / 规则产生有限候选读音集合 R_n，并定义纯文本预测的**默认读音** r⁰_n。一次完整赋值 r=(r₁,...,r_N) 对应完整发音 y(r)=r₁r₂···r_N。
2. **声学打分（语音侧）**：使用**冻结**的预训练 S2P 模型，将 y(r) 渲染为模型词表 token z(y)，以整序列负对数似然（NLL）打分：S(y,x) = −log p(z(y)|x)。目标函数为 J(r,x) = S(y(r),x) + P(r)，其中 P 为可选的候选可靠性惩罚项（日语中 P=0.03·m·n_ctc，m 为从默认切换的 span 数，n_ctc 为 token 长度）。
3. **从左到右贪心搜索**：由于 |R| 随 N 指数增长，采用逐 span 单次访问、就地 commit 的贪心策略，每次把候选作为**完整序列**（前序已定、后续保持默认）打分，复杂度由指数降为 Σ|R_n|。
4. **双模型级联 + 融合分数**：S = L₁ + λL₂，L₁ 来自 320M wav2vec2.0 kana CTC，L₂ 来自 810M 自回归 kana-whisper（对同一发音最多 16 种拼写取教师强制似然之和，并缓存 cross-attention）。先用 L₁ 跑一遍贪心；若默认读音被改动且 λ>0，再用融合分数从 r⁰ 重跑，否则保留首轮结果。
5. **Margin check（边际校验）**：以长度归一化阈值 τ≥0 校验被改动 span，仅当相对默认读音的分数增益满足 S(y(r̃[j←r⁰_j]),x) − S(y(r̃),x) ≥ τ·ℓ_j（ℓ_j 为归一化发音符号数）时才保留改动，否则回退默认；τ=0 时关闭。

**关键特点**：整条流水线无需任何 (x,w,y) 三元组标注、无需任何模型训练，只在推理时同时利用词典/G2P（transcript 所允许的）与冻结 S2P（语音所支持的）两路证据。

## 实验结果
**日语（JVS-dev / JSUT BASIC5000 / JVS-par，每语料 512 条公共语句）**：
- 在**参考文本**条件下，CER 由纯文本基线的 0.60–1.40% 降至 **0.04–0.17%**；级联配置为 dev 0.15 / JSUT 0.17 / par 0.04。
- 在 **Whisper large-v3 ASR 文本**条件下，CER 为 **0.64–1.58%**（级联：0.64 / 0.65 / 1.58）。
- 超越所有基线：包括训练好的 ST2P 标注器 Furigana Whisper + 词典约束（0.21 / – / 0.15）、同模型文本条件化方法（kana-whisper+prompt、CTC+词典约束）、音频单独解码（Kana CTC greedy、kana-whisper）、纯文本 G2P（Open JTalk 等），以及商用多模态模型（Gemini 2.5/3/3.5/3.6 Flash）与开源 MLLM（Qwen3-Omni、Qwen2.5-Omni、Gemma-3n-E4B、Phi-4-multimodal，CER 普遍高出一个数量级）。
- **效率**：贪心搜索在相近 CER 下比 beam search 快 **3–3.5×**；级联比直接解码快 **2×**；Fig. 1 显示在单张 H100 上达到最低 CER 与低实时率（RTF）的帕累托前沿。
- **多语言**：在西班牙语、法语与初步英语上同样优于四个开源多模态 LLM 以及各语言最佳传统方法。
- **超参**：λ=1（选自 {0.5,1,2}），τ=0.6，用 JSUT 与 JVS-par 各 1000 条语句标定并迁移到 JVS-dev。

## 一句话评价
本文以「文本约束候选生成 + 冻结 S2P 的整序列 NLL 重打分 + 从左到右贪心搜索（含级联与 margin check）」的纯推理方案，在不训练任何模型、不使用发音标注的前提下，把日语发音转写 CER 压低到 0.04–0.17%（参考文本）并在多语言上超越训练型 ST2P 与商用多模态大模型，同时保持 3–3.5× 于 beam search 的推理速度，为大规摸 TTS 数据准备提供了一条高性价比、易迁移的实用路径。

---

## 20. I-Parakeet: Integer-Only Conformer ASR on Mobile NPU

**作者**: Taichi Nishimura
**链接**: [2609.30846](https://arxiv.org/abs/2609.30846)
**分类**: Speech Recognition | **关键词**: integer-only quantization, Conformer, automatic speech recognition, mobile NPU, Swish approximation, relative-positional self-attention, Parakeet-CTC

# I-Parakeet: Integer-Only Conformer ASR on Mobile NPU 论文总结

## 核心痛点
- 现代 Conformer ASR 模型规模大，如 NVIDIA Parakeet-CTC 0.6B 参数，单精度权重超过 2.4GB，边缘设备内存、延迟和功耗压力大。
- 量化到 INT8 可将权重降至 600MB，但多数量化 ASR 并非 integer-only：LayerNorm、Softmax、非线性激活等仍反量化为 FP16/FP32，无法完全利用移动 NPU 的整数加速器，甚至无法部署到无 FPU 的 ARM Cortex-M。
- 已有 integer-only 研究（I-BERT 及其 ASR 扩展）硬件验证局限于 GPU，尚未探索整数-only Conformer 能否在手机 NPU 上实际运行。

## 方法创新
1. **整数相对位置自注意力**：Parakeet 的相对位置 MHSA 中，内容分支 Ac 与位置分支 Ap 量化尺度 Sc != Sp，不能直接相加；论文将两分支转换、相加和 1/sqrt(dk) 缩放融合为单一重量化：qs = floor(2^-n (mc qc + mp Φ(qp)))，mc、mp 离线预计算。相对位置投影 P 仅依赖序列长度，离线量化为 INT8 常量；相对移位 Φ 仅移动和补零，可直接作用于整数张量，实现为静态索引映射。
2. **Minimax 优化的整数 Swish**：Swish 依赖 sigmoid，无整数核。论文用二阶多项式近似 tanh，但不采用 I-BERT 对 tanh 的最小二乘拟合，而是直接最小化 Swish 输出的最大误差（L∞），以解决误差被 x 放大且拟合目标不匹配的问题，数值求解得 a*=-0.1240、c*=2.4632。
3. **逐层激活范围分析**：默认 INT8 + min-max 在两处失败。BatchNorm 输出跨通道的 γ/sqrt(σ²+ε) 最大值/中位数超过 10^3-10^4，少数极端通道占满网格，因此 BatchNorm 输出改用 INT16 网格；pre-encoder 激活的 max/p99.9 达 11-21 倍，min-max 将大量 INT8 级用于 0.1% 尾部，因此 pre-encoder 用 99.9 百分位校准，encoder 内保持 min-max（2-3 倍），其余张量维持 INT8。整体实现无浮点算子、无 CPU 回退。

## 实验结果
- 设备：Nothing Phone (3a)，Snapdragon 7s Gen 3（SM7635），QNN SDK QAIRT 2.47。
- 数据集：LibriSpeech test-other。
- I-Parakeet：WER 4.97%，RTF 0.048，峰值内存 612 MiB。
- 基线：parakeet.cpp CPU FP16/FP32 为 WER 3.76、RTF 0.36、1517 MiB；parakeet.cpp CPU INT8/FP32 为 WER 3.76、RTF 0.42、1045 MiB；Stock FP16 NPU 与 Stock INT8 PTQ NPU 均 WER 100.0，无法正常工作。
- I-Parakeet 比 CPU 基线快 7.5 倍，峰值内存约减半，是唯一能在手机 NPU 上实际运行的 integer-only 实现。

## 一句话评价
I-Parakeet 通过整数相对位置注意力、minimax Swish 近似和逐层量化范围矫正，首次在消费级手机 NPU 上实现无浮点、无 CPU 回退的 Conformer ASR，验证了 integer-only ASR 在移动整数加速器上的可行性。

---

## 21. Subject-Invariant Cross-Modal Decoding of Perceived Speech from Brain Recordings

**作者**: Aoke Zhang, Jing Chen
**链接**: [2609.30832](https://arxiv.org/abs/2609.30832)
**分类**: Neural Speech Decoding / Brain-Computer Interface | **关键词**: MEG, fMRI, cross-modal decoding, cross-subject decoding, subject consistency, perceived speech decoding, brain-computer interface

## 核心痛点
- 非侵入式脑机接口（BCI）感知语音解码面临两大挑战：从神经信号中提取具有丰富时空信息的表征，以及实现跨受试者泛化。
- MEG 空间分辨率低，难以预测语义等高层语音特征；fMRI 时间分辨率通常为秒级，难以捕捉动态特征，导致合成文本词错误率高。
- 现有跨模态方法（如 fMMF）主要面向受试者内解码，受试者间差异使模型对新目标受试者泛化差；现有跨受试者方法（如 CPSD）多仅依赖 MEG/EEG，缺乏丰富时空细节。
- 因此，亟需统一方法同时解决跨模态融合与跨受试者一致性问题。

## 方法创新
- 提出 SICMD（Subject-Invariant Cross-Modal Perceived Speech Decoding），统一 fMRI 与 MEG 的跨模态、跨受试者感知语音解码。
- MEG 编码器包含：PESA（基于位置编码的空间注意力）模块，将不同受试者 MEG 信号重映射到标准化参考空间，显式提取受试者一致信息；1x1 CNN 层；subject layer；以及基于 ConvConcatNet 的 brain encoder。
- fMRI 编码器为简单 MLP：三个编码模块（线性层 + BatchNorm + ReLU + Dropout=0.3）后接线性层，首层输入维度匹配 fMRI 数据维度，后续层维度为 1024。
- 训练流程采用留一受试者法（leave-one-subject-out）。源模型预训练输入 MEG 片段、传感器位置和受试者 ID；PESA 利用传感器位置进行重映射，再经 1x1 卷积和 subject layer，送入 MEG brain encoder，输出对齐 wav2vec2 表示。
- 个人特化：使用 CorrCA 算法从源受试者 subject layers 中提取一致分量并平均，初始化目标受试者的 subject layer；随后微调，使神经表征与语音表征重新对齐。
- 模态融合：采用 fMMF 的异步数据融合方法，利用不同语音层级信息变化率差异，以及 fMRI 和 MEG 对不同层级语音信息的预测能力。

## 实验设置
- 数据集：公开多模态神经影像数据集，包含 12 名受试者聆听相同连续中文语音的 fMRI 和 MEG 记录，共 60 trials；fMRI 重复时间 TR=0.71s；MEG 使用 306 通道系统，采样率 1000Hz；预处理沿用已有方法。
- 数据划分：按 trial 索引划分为 70% 训练集、10% 验证集、20% 测试集，确保不同 trial 数据无重叠。
- 训练细节：CLIP loss；batch size=128；测试样本量=128；Adam 优化器，学习率 3e-4；早停 patience=10；单张 NVIDIA RTX 3090 GPU。
- 评价指标：Top-1 准确率、Top-10 准确率、Rankacc。

## 实验结果
- 跨受试者感知语音解码：SICMD 达到 Top-1 43.5±13.7%、Top-10 82.7±12.7%、Rankacc 93.4±5.0%。
- 相比基线方法，Top-1、Top-10、Rankacc 分别提升超过 10.6%、10.1%、1.7%，所有提升经配对 t 检验统计显著（p<0.001）。
- 效率：与多受试者和受试者内解码设置相比，训练成本分别降低 88.8% 和 60.5%；多受试者、受试者内、个人特化阶段平均训练步数分别为 5595.5、1593.4、629.3。
- 消融研究：融合方法中 SICMD 所用方法最优；融合位置在 brain encoder 输出处最优；随机打乱传感器位置顺序会使 Top-10 下降 19.0%（p<0.001）；fMRI Encoder 层数消融验证了超参数有效性。
- PESA 可视化显示，双侧颞叶附近通道权重更高，表明模型自动关注与语音处理相关的脑区。

## 一句话评价
SICMD 将跨模态 fMRI-MEG 融合与跨受试者一致性建模统一到感知语音解码框架中，在显著提升解码性能的同时大幅降低训练成本，为非侵入式语音神经假体提供了有前景的跨受试者解决方案。

---

## 22. Symbiotic Architecture for Post-Hoc Audio Extension of Frozen Language Models

**作者**: Yotaro Kubo, Qi Sun, Yujin Tang
**链接**: [2609.30784](https://arxiv.org/abs/2609.30784)
**分类**: Audio Language Models | **关键词**: Audio Language Model, KV Cache Injection, Catastrophic Forgetting, Prefilling Scalability, Frozen LLM, Context Optimization

## Core Pain Points
- **Limited prefilling scalability**: In conventional monolithic ALMs, audio embeddings are prefilled by the backbone LLM to produce KV cache, making computational cost proportional to backbone size. With ever-larger LLMs, this cost becomes prohibitive.
- **Catastrophic forgetting**: Fine-tuning the LLM on audio and instruction data often degrades its original text-only capabilities. Mitigation via dataset mixing is complex and expensive.

## Method Innovation
- **Symbiotic architecture**: Introduces an **injector** module that directly writes audio-conditioned vectors into the LLM's KV cache, enabling the frozen LLM to act as an audio language model (ALM) without weight updates.
- **Injector design**: A stacked CNN based on **LConv** modules (from Conformer) with RMSNorm, chosen over Transformer for local context modeling. The adapter block subsamples via max pooling (stride 8) and maps to key/value spaces with affine transformations and RMSNorm.
- **KV scale matching**: Aligns the distribution of injected KV vectors with the backbone LLM's internal KV cache (e.g., Qwen3) by initializing RMSNorm scale parameters and adding head-wise rescaling, ensuring stable optimization.
- **Noisy RoPE training**: Randomizes RoPE position offsets and time-scale factors during training to improve robustness to unseen sequence lengths, since the backbone is not fine-tuned.
- **Decoupled prefilling**: The injector is narrower than the backbone, so prefilling cost scales with injector width rather than backbone width, improving scalability. The LLM remains completely frozen, preserving original capabilities.

## Experimental Results
- Evaluated on audio-understanding tasks: **automatic speech recognition (ASR)**, **audio question answering (AQA)**, and **acoustic scene classification (ASC)**, as well as text-only tasks.
- The proposed method **outperforms the conventional frozen-LLM approach** and **approaches the performance of a fine-tuned ALM** while activating fewer parameters during audio prefilling.
- By construction, it **preserves the backbone LLM's original text-only task performance** without degradation.

## One-Sentence Evaluation
A novel symbiotic architecture that efficiently extends frozen LLMs to audio understanding via KV cache injection, simultaneously addressing prefilling scalability and catastrophic forgetting while maintaining text-only performance.

---

## 23. Dialogue-Based Streaming Audio-Visual Target Speaker Extraction with Predictive Dialogue Information

**作者**: Shuhan Zhang, Wenxuan Wu, Haizhou Li
**链接**: [2609.30774](https://arxiv.org/abs/2609.30774)
**分类**: Audio-Visual Target Speaker Extraction (AV-TSE) | **关键词**: Audio-Visual Target Speaker Extraction, Speech LLM, Voice Activity Projection, Streaming Inference, Dialogue Context, Target Speaker Extraction

# 论文总结：Dialogue-Based Streaming Audio-Visual Target Speaker Extraction with Predictive Dialogue Information

## 核心痛点
- 真实面对面实时通信中，目标说话人提取需处理自然停顿、话轮转换、反馈信号和背景串扰。
- 现有 TSE 多基于模拟混合，覆盖完全重叠或稀疏重叠，忽略真实对话的话轮结构；在线 AV-TSE 缺乏基准。
- 流式模型看不到未来帧，在话轮边界和相似重叠语音下提取最困难。
- 传统 VAP 只在干净单说话人通道训练，不能从重叠混合预测；且主要依赖声学线索，未利用语言和对话知识。

## 方法创新
1. **首个在线 AV-TSE 基准**：基于 IEMOCAP 和 RealTalk 构建真实二元对话加独立第三方干扰，保留自然话轮、停顿和重叠。
2. **LLM-based TS-VAP**：将 Mini-Omni2（Qwen2-0.5B）适配为目标说话人条件语音活动投影。Whisper 和 CLIP 编码混合音频与目标视频，Qwen 产生视觉条件音频表示并与 CLIP 特征融合，轻量因果头输出 25 Hz、256 维预测表示；预测未来 2 秒目标–伙伴联合活动，编码为 2^8=256 状态。训练含联合状态分类、当前活动和未来 bin 辅助监督；微调后冻结，为分离器提供预测上下文。
3. **三类对话上下文融合**：
   - 历史上下文：过去分离器潜变量经 GRU 汇总，受 MeMo 启发。
   - 同步上下文：ASD 嵌入与视觉特征，受 ActiveExtract 启发。
   - 预测上下文：过去 TS-VAP 特征经 0.2 秒间隔池化得到最多 10 个 token，加相对位置嵌入；当前音频特征通过 MHA 查询该上下文。
4. **两遍训练**：第一遍无预测记忆处理前缀并构建记忆；第二遍用固定记忆重新处理前缀加额外 2 秒。
5. **pVAD 头与掩码推理**：显式监督目标缺失区域，推理时用目标活动概率阈值化构造衰减掩码。

## 实验结果
- **数据**：Vox2Mix 预训练；IEMOCAP-Dialog3Mix（23,522/8,120/3,000 训练/验证/测试）；RealTalk-Dialog3Mix（1,000 混合，跨语料泛化）。
- **主干对比**：Dolphin、AV-TFGridNet、TDSE、USEV、AV-SepFormer。
- **主要结果**：
  - TS-VAP 跨主干一致提升：TDSE 7.44→7.78 dB（+4.6%），AV-SepFormer 9.07→9.59 dB（+5.7%），USEV 9.04→9.56 dB（+5.8%）。
  - LLM-VAP 优于 Acoustic VAP：USEV 上 LLM-VAP +5.8% vs Acoustic VAP +4.1%。
  - USEV 上组合历史、同步、预测上下文达 10.03 dB，相对无上下文 9.04 dB 提升 +10.9%，约 1 dB 增益。
  - 按重叠比例报告 SI-SNR，组合上下文在 0% 重叠达 17.19 dB，在 (80,100]% 重叠达 7.09 dB。
- **结论**：历史、同步、预测三类上下文互补，预测性对话信息尤其在真实 AV 对话中带来显著增益。

## 一句话评价
该论文首次构建真实二元对话下在线 AV-TSE 基准，并利用语音 LLM 的对话级话轮预测能力，将历史、同步与预测上下文系统融合，显著提升流式音视频目标说话人提取性能。

---

## 24. Learning Natural Conversational Behavior in Tandem Speech-to-Speech Models with Randomized Guidance

**作者**: Manato Yaguchi, Yotaro Kubo, Hikaru Asano, So Kuroki
**链接**: [2609.30773](https://arxiv.org/abs/2609.30773)
**分类**: Speech-to-Speech Dialogue | **关键词**: speech-to-speech dialogue, full-duplex dialogue, randomized guidance, tandem speech-to-speech, real conversations, KAME, Moshi

### 核心痛点
实时语音对话需要同时具备高质量回复和自然交互能力。Moshi 等全双工 S2S 模型延迟低、轮次切换灵活，但知识与推理能力有限；级联 ASR–LLM–TTS 系统可借助强大文本 LLM，却会引入影响对话流畅性的延迟。KAME 等 tandem 架构用响应式语音前端搭配异步文本 LLM 后端，在用户说话期间由后端持续提供候选回复作为 guidance。

训练这类 tandem S2S 模型时，监督微调不仅需要普通对话对，还需要后端在用户说话过程中提供的中间 guidance。但普通对话录音只有用户话语和最终回复，缺少后端 LLM 的 intermediate guidance。KAME 使用 simulator LLM 逐样本模拟 guidance，成为将 tandem 训练扩展到大规模真实对话语料的数据准备瓶颈；而仅用合成数据又难以直接学到自发对话的时机与语音表达。

### 方法创新
论文提出 randomized intermediate guidance，直接用对话语料构造训练时的 guidance stream，而不再逐样本模拟后端 LLM 行为。具体做法是：目标回复 transcript y 作为 informative guidance，放在最后一个 designated target-response update；其余更新位置从训练语料其他对话中随机采样 response texts，作为 potentially irrelevant guidance。采样池按 token 序列去重，排除当前对话中的 response texts，并保留 token 数在 y 的 0.5 到 2 倍之间的候选，然后对每个 segment 均匀无放回采样。

该方法的核心假设是：KAME 微调最关键的能力，是让前端模型学会区分 informative guidance 与由过早 LLM 调用产生的 irrelevant guidance。通过混合目标回复和随机无关回复，模型被鼓励选择性利用有用的后端信息，同时忽略无关更新。这样所有训练数据都可以直接由带转写的对话数据构造，无需逐样本 LLM simulation。

在真实对话应用上，作者先做 VAD、说话人日志、语音增强、质量过滤和转写对齐：用 Silero VAD 检测 PodcastIndex 录音中的语音区域，用 pyannote speaker-diarization-3.1 做说话人日志，投影到 VAD 段并丢弃多说话人或重叠语音段；用 Sidon 增强，再用 DNSMOS P.835 过滤 OVRL≥3.0；用 batched faster-whisper large-v3-turbo 转写并获得 token 级时间戳；用 Whisper language probability≥0.85 和平均 log probability≥−0.4 过滤转写。之后由同一录音、同一声道、恰好两个说话人身份的 segment group 构造对话样本，按原时间戳排序并首尾拼接，保留相对时序但丢弃原始段间间隔。

### 实验结果
在相同英文合成对话上比较四种 guidance 构造策略：LLM-generated、Similarity-based、Target-only、Randomized。评估使用 spoken MT-Bench 的 30 个问题子集，GPT-4.1 作为推理时 backend，Whisper large-v3 转写，GPT-4 judge 按 1–10 打分。结果：Randomized 6.09±0.05，Similarity-based 6.14±0.05，LLM-generated 5.54±0.03，Target-only 5.12±0.03。Randomized 与最佳基线竞争力相当，并高于 Target-only；作者推测 LLM-generated 的模拟 guidance 遵循启发式轨迹，未必充分反映推理时 backend 更新的多样性。

在真实对话上，作者用 3.8k 小时双人对话语料训练 KAME。结果显示：KAME（real data, ours）MT-Bench 5.04±0.21，smooth turn-taking 50.88%，interruption 17.77%，pause 81.08%，audio-judge naturalness 4.79±0.32；相比 KAME（synthetic data）MT-Bench 5.54±0.03、smooth 40.62%、interruption 19.28%、pause 80.20%、naturalness 4.05±0.14，真实数据模型轮次切换更平滑、音频自然度更高；相比 Moshi 的 MT-Bench 1.96±0.01、smooth 36.75%、interruption 23.93%、pause 74.62%、naturalness 5.29±0.22，真实数据 KAME 在回复质量上保持显著优势。

### 一句话评价
用“目标回复 + 随机无关回复”替代昂贵的逐样本 LLM guidance 模拟，方法简单实用，使 tandem S2S 模型能直接利用大规模真实对话语料学习自然交互行为，同时保留 tandem 架构的回复质量优势。

---

## 25. Training-Free Contextual ASR via SpeechLLM-Based Error-Aware Selective Retrieval

**作者**: Natsuo Yamashita, Ai Nemoto, Ryosuke Koichi, Masaaki Yamamoto
**链接**: [2609.30694](https://arxiv.org/abs/2609.30694)
**分类**: Speech Recognition (Contextual ASR / SpeechLLM-based Terminology Retrieval) | **关键词**: Training-Free Contextual ASR, Speech Large Language Model, Domain-Term Error Localization, Selective Retrieval, Acoustic Neighbor Embeddings, In-Context Learning

# 论文总结：Training-Free Contextual ASR via SpeechLLM-Based Error-Aware Selective Retrieval

## 核心痛点
- 领域特定与低频术语识别仍是 ASR 的难点，通用 ASR 容易将其误识为常见词或音近词。
- 上下文偏置可提升这类术语识别，但直接提供大规模术语词典会引入大量无关候选，增加计算成本并可能导致过度偏置。
- 基于检索的上下文偏置虽能筛选候选，但若对大量识别词进行查询，需要多次词典查找，且候选定位可能不够精准。
- 现有术语选择或检索方法多依赖单独训练的检索、排序或对齐模块，并且选择标准未显式针对“可能对应领域术语且包含识别错误”的区域。
- 因此需要一种无需任务特定训练、能判断何时需要术语检索以及哪些区域应触发检索的方法。

## 方法创新
- 提出无需训练的上下文 ASR 框架：预训练 SpeechLLM 在一次推理中联合生成第一遍 ASR 假设，并定位可能包含领域术语的识别错误片段。
- 将定位到的错误片段作为硬门控用于术语检索：只有预测可能包含领域术语错误的区域才触发外部术语词典查询，而不是对全部识别词查询。
- 使用 Acoustic Neighbor Embeddings (ANE) 对定位片段进行音素/声学近邻检索，从外部术语词典中召回音近术语；相似度定义为 r(q,v)=1/(1+||g(q)-g(v)||^2)，对多个查询片段按每个词典词取最大相似度聚合排序，取 Top-K 候选。
- 同一 SpeechLLM 基于第一遍假设与检索到的术语进行第二遍上下文重识别，无需参数更新。
- 利用音频-文本上下文学习（ICL）示例，覆盖四种识别情形：无错误、领域术语替换、领域术语被误识为常见词序列、音近替换；输出格式为先完整生成第一遍转录，再输出错误片段，使片段定位条件依赖于模型自身生成的假设。
- 若未定位到任何片段（M=0），则跳过检索与第二遍重识别，直接保留第一遍结果，从而减少不必要的词典查询。
- 整个框架不需要任务特定模型训练或参数更新，使用 Qwen3-Omni-30B-A3B-Instruct 作为 SpeechLLM。

## 实验设置
- 数据集：医学 United-MedSyn (MedSyn)、空管 ATCOSIM、金融 Contextual Earnings-22 (Earnings)。
- MedSyn 随机采样 7,906 条，对应 10% 数据。ATCOSIM 为 1,901 条、22,642 参考词、167 领域术语、领域占比 9.00%；Earnings 为 772 条、26,750 参考词、652 领域术语、5.04%；MedSyn 为 7,906 条、106,566 参考词、7,198 领域术语、11.65%。
- 术语词典从参考转录中构建，保留在 LibriSpeech、Common Voice、GigaSpeech 中每百万词出现不超过一次的目标领域 unigram；排除数字词、少于 3 字符的词和非字母 token；词典固定，不利用话语级参考信息。
- 模型：Qwen3-Omni-30B-A3B-Instruct，无参数更新。Joint ICL 使用 4 个音频-文本 ICL 示例；其他定位方法不使用示例。Joint zero-shot 使用相同定位指令但无示例。

## 实验结果
- 摘要与实验部分表明：在医学、空管、金融三类语音上，所提方法显著减少词典查询，同时提升相关术语候选的召回与排序以及第二遍 ASR 性能。
- MedSyn 上的领域术语错误定位结果（Table 4）：
  - All ASR 1-grams：Spans/Utt. 13.37，Error Precision 8.1，Error Recall 92.8，General Recall 83.6，Domain Recall 99.1。
  - Random span：0.99，11.5，10.6，11.0，10.3。
  - NE extraction：1.72，29.5，63.6，37.0，81.7。
  - Confidence span：1.15，49.4，50.6，28.9，65.3。
  - ASR only：0.67，65.0，54.4，36.6，66.4。
  - Audio only：0.94，27.4，18.6，12.3，22.8。
  - Audio + ASR：1.07，49.9，67.0，41.4，84.4。
  - Joint zero-shot：1.09，46.7，75.6，49.7，85.9。
  - Ours (Joint ICL)：0.99，51.9，76.1，47.6，86.0。
- 定位性能上，Ours 在 Error Precision、Error Recall、Domain Recall 上与 Joint zero-shot 接近或略优，且 Spans/Utt. 仅为 0.99，远低于 All ASR 1-grams 的 13.37，说明以很少的片段触发检索即可获得较高领域术语召回，从而减少词典查询。

## 一句话评价
- 该工作用预训练 SpeechLLM 自身的错误定位作为选择性术语检索门控，以完全免训练的方式在多个领域上实现了更少词典查询和更好的上下文 ASR 效果，思路简洁有效；但其性能仍较依赖 SpeechLLM 能力、ICL 示例质量以及音近检索词典覆盖。

---

## 26. MuseTimbre: Zero-Shot Timbre Transfer by Controlling a Frozen Music Generator

**作者**: Yuan-Chiao Cheng, Zhiyao Duan
**链接**: [2609.30548](https://arxiv.org/abs/2609.30548)
**分类**: Music Generation (Timbre Transfer) | **关键词**: Timbre Transfer, Music Generation, Diffusion Transformer, Disentangled Representation, Cross-Attention, CLAP, Zero-Shot

## 核心痛点
- 乐器音色迁移需要保留源演奏的音符内容，同时换成参考乐器的音色。
- 文本提示只能给出乐器名，难以指定同种乐器内部的音色细节，例如电吉他的 clean jazz 与 heavy distortion、小提琴的明亮独奏与温暖乐队音色。
- 音频参考能更精确指定音色，但现有音频参考方法通常训练专用模型，任务窄、乐器集固定；或给预训练音乐生成器加控制时，参考片段中的音色与 genre/melody 纠缠，系统仍退回文本命名音色。
- 还需解决源录音中的音高-音色解耦，以及目标音色的精确指定与迁移。

## 方法创新
- 提出 MuseTimbre，据称是首个通过条件化预训练音乐生成器，将音频参考音色迁移到复调源音频的系统。
- 基于 Stable Audio 3 Medium（预训练 rectified-flow diffusion transformer / DiT）构建，冻结其音频自编码器、DiT 主干和原始文本控制路径，只添加两个可训练插件式条件模块。
- 音高条件路径：用 Basic Pitch 从源音频显式估计音高，生成 88 note + 88 onset 的二进制 piano roll；经 1-D CNN 编码为逐帧特征；通过带 RoPE 的 decoupled cross-attention 注入 DiT 每一层，并使用零初始化门控。piano roll 也可直接接受 MIDI 乐谱输入。
- 音色条件路径：使用 LAION-CLAP 音频分支提取 512 维、时间不变的参考音色嵌入；通过 linear projection 映射为每层 AdaLN 的 scale 和 shift，以 AdaLN-Zero 风格注入，同样使用零初始化门控。与已有冻结编码器的工作不同，MuseTimbre 端到端微调 CLAP 编码器。
- 训练目标为 rectified-flow 目标：给定目标 latent z0 和高斯噪声 epsilon，构造 x_t = (1-t) z0 + t epsilon，回归速度 epsilon - z0；条件为 c_pitch 和 c_timbre。每个训练片段中，c_pitch 为真值音高或 Basic Pitch 估计音高，c_timbre 从同一片段的不同区段提取。
- 训练数据为 50/50 合成与真实音频：合成部分用 Slakh MIDI stems 与 7 种 General MIDI soundfonts 渲染，约 110 万条至少 10 秒的 stem 录音，覆盖 13 个乐器类；真实部分含 MoisesDB 和 URMP 的 18,869 个片段、1,208 个单乐器 stem，去掉鼓、打击乐、人声和未标注 stem。每个训练片段 5 秒、44.1 kHz。
- 优化：AdamW 训练 250k 步，2 张 GPU，weight decay 0.01，1000 步 warmup 后 cosine decay，有效 batch size 16，多条件 classifier-free guidance dropout。音色编码器学习率 1e-5，控制模块学习率 1e-4。
- 推理：从噪声开始，25 步 Euler，单张 RTX 5090 上生成 5 秒音频约 1 秒；CFG 为 λpitch = λtimbre = 2。冻结主干保留文本控制，并可用 MIDI 乐谱钢琴卷合成参考音色。

## 实验结果
- 零样本跨乐器迁移实验：在 4 个训练未见数据集上共 304 对样本上评估，数据集为 PHENICX-Anechoic、MAESTRO v3 test split、GOAT、Bach10，共 13 种乐器。
- 每对源和参考来自不同乐器、不同数据集，且不共享乐器身份或录音条件。取每个片段最响的 5 秒。
- 与四类文本条件基线和三类音频参考基线比较，包括 DDIM-inv、DDPM-inv 等；图中还比较了 TokenSynth-A、SS-VQ-VAE、TokenSynth-T、MuseControlLite、CTD 等。
- 结果显示：MuseTimbre 在四个真实复调录音数据集上，音高对齐（pitch alignment）与基线相当或具有竞争力，同时音色匹配（timbre match）显著更接近参考音色。
- 微调后的 CLAP 音色提取器对音高变化鲁棒；在控制网格上的音色识别检索任务中，微调 CLAP 在所有 pool size 上优于冻结 CLAP、AST、MERT、M2L 等基线，可用于音色相似度度量。
- 论文发布代码、模型权重和音频示例。

## 一句话评价
MuseTimbre 通过冻结预训练音乐生成器并注入音高与音色双条件模块，在零样本复调音色迁移中兼顾音高保持与音色匹配，并用微调 CLAP 提升了音色表征的鲁棒性，是该方向一个兼具系统性与实用性的新方案。

---

## 27. Don't CLAP: Are Music-Text Models Bag-of-Words?

**作者**: Yuan-Chiao Cheng, Alexander Lerch
**链接**: [2609.30540](https://arxiv.org/abs/2609.30540)
**分类**: Music-Text / Audio-Language Model Evaluation | **关键词**: CLAP score, music-text models, bag-of-words, attribute binding, prompt faithfulness, benchmark

## 论文信息
**标题**: Don't CLAP: Are Music-Text Models Bag-of-Words?
**作者**: Yuan-Chiao Cheng, Alexander Lerch（Georgia Tech, Music Informatics Group）

## 核心痛点
文本到音乐（text-to-music）系统的评估主要关注音频质量和提示忠实度（prompt faithfulness）。其中 **CLAP score**（对比式音乐-文本模型的音频嵌入与文本嵌入之间的余弦相似度）已成为衡量忠实度的标准客观指标。然而，该指标是否真正反映文本中的细粒度语义关系尚不清楚：当一个属性被绑定到某个乐器上时（如 "distorted guitar"），文本嵌入是否捕捉到了这种**属性绑定（attribute binding）**？

## 方法创新
1. **属性交换扰动（Attribute Swap Perturbation）**：不改动音频，仅把两个乐器之间**恰好一个属性**互换，生成扰动 caption c−，其余词完全不变。涵盖三个属性维度：
   - 音色（timbre）
   - 主奏 vs 伴奏（lead vs accompaniment）
   - 首次出现顺序（order of first appearance）
2. **Music Attribute-Swap Benchmark (MASB)**：400 个带注释的录音（140 timbre / 123 lead-vs-acc / 137 onset-order），共 800 个 caption 对（模板式 + 自然改写两种格式）。数据来自 Song Describer Dataset 与 MTG-Jamendo 的 10 秒 CC 音频片段。
3. **MASB-Order**：来自 MoisesDB stems 的 300 组对称音频对（a+ 与 a− 只在哪个乐器先进入上不同），构造上消除文本先验，检验无先验下的真实辨别能力。
4. **评测模型**：四个对比式音乐-文本模型（LAION-CLAP music ckpt、MS-CLAP 2023、MuQ-MuLan、CLaMP 3）+ 一个大音频语言模型（Qwen2-Audio-7B-Instruct，分别在有/无音频下测试）。
5. **先验与音频证据的分离**：用 Cohen's κ 衡量带音频选择与纯文本选择的一致性；按文本先验是否正确切分数据，并用先验平衡准确率（prior-balanced accuracy）消除先验优势。

## 四个实验与结果
**Exp.1（属性交换下的 CLAP score）**：四个对比模型无一致偏好，平均准确率仅 0.431–0.519，接近 0.5 随机水平；仅 MuQ-MuLan（0.642）和 MS-CLAP（0.630）在 lead role 上显著高于随机，但 CLaMP 3 在同一属性上低至 0.337、MuQ-MuLan 在 onset order 上仅 0.383（显著低于随机）。Qwen2-Audio 平均 0.681（timbre 0.639 / lead 0.720 / onset 0.690），表现更好。

**Exp.2（文本先验 vs 音频证据）**：Qwen2-Audio 无音频时已达 0.682（timbre）、0.679（lead role），高于所有对比模型；onset order 仅 0.573。加入音频后整体仅从 0.644 升至 0.681，timbre 甚至从 0.682 降至 0.639。带音频与纯文本选择的一致性在 lead 上 κ=0.46、onset 上 κ=0.57、timbre 上 κ=0.03，说明其优势主要来自语言先验。四个对比模型 κ 从未超过 0.24。

**Exp.3（文本嵌入距离）**：c+ 与交换后 caption 的余弦距离、与改写 caption（paraphrase）的距离进行比较，验证原始与扰动 caption 的嵌入几乎无法区分。

**Exp.4（对称音频对，先验被抵消）**：MASB-Order 上所有模型准确率均接近随机——LAION-CLAP 0.508、MS-CLAP 0.538、MuQ-MuLan 0.497、CLaMP 3 0.527、Qwen2-Audio 0.537，LALM 的优势在无先验条件下消失。

## 结论与一句话评价
论文有力证明 CLAP score 及相关指标**无法捕捉细粒度音乐语义和属性绑定**，其文本表示更接近 **bag-of-words**，对改变语义的 caption 扰动不敏感；LALM 表面上的优势主要来自与音频无关的语言先验而非真正的音频理解。该工作为音乐-文本对齐评估敲响警钟，并提供了可复用的 MASB 基准（代码与注释已公开）。

---

## 28. AcoustiClaim: A Numeric Claim Benchmark with Instrument Ground Truth

**作者**: Sheng-Tse Lin, Siyuan Zhai, Chien-Liang Kuo, Massa Baali, Bhiksha Raj
**链接**: [2609.30483](https://arxiv.org/abs/2609.30483)
**分类**: Audio Language Models Evaluation / Acoustic Measurement Benchmark | **关键词**: Audio Language Models, Numeric Claim Benchmark, Acoustic Measurement, Selective Prediction, Speech Quality Assessment

## 核心痛点
音频语言模型在描述录音时经常会输出具体声学数值，例如 SNR、jitter、shimmer、HNR、F0、语速、停顿数等。但现有评测大多只把这些数值与人类主观评分或 judge model 对齐，而不是检查该数值是否真的对应信号本身可被仪器测得的量。因此，模型可能给出看似专业、实际不可验证或错误的数值声明。论文提出 AcoustiClaim，用仪器 ground truth 直接检验自由文本中的数值声明。

## 方法创新
1. 基准构建：从自由文本中抽取数值声明，对照定义该声学量的仪器读数评分；按参考量是否存在于模型输入中分成不同 tier：Exact、Measurable、Stem-only、Masked。
2. 数据：Libri2Mix 两说话人混合（加录制的房间响应做混响，并以独立 SNR 加噪）和 AMI 远场会议。每个 mixture 贡献自身与 clean twin，测试集为 6000 条；AMI 行是零样本。
3. 参考系统：冻结 WavLM encoder 第 7 层 + 卷积压缩器 + adapter + Qwen3-8B decoder，LoRA rank 16，每 160 ms 一个 prefix token。一个线性 confidence head 对每个 quantity 输出 value 与 log-variance，用 heteroscedastic Gaussian NLL 训练。每个数值都是 prefix token 的精确求和项；方法区分 sum/rate 与 quotient 两类误差结构，并给出 clip error 的界。
4. 选择性预测：按 per-quantity threshold 校准到 0.75 coverage，低置信度时在 prose 中拒绝回答，而不是强行给数。
5. 指标：coverage、selective risk、normalized MAE、Spearman correlation；并设 n≥25 clips、至少 5 个不同值、ρ>0.3 三条外部 bar。

## 实验结果
- 四个 open-weight 系统和 1 个 closed model，对 10 个量用 5 种 elicitation 方式、2 个语料，共 207 个 cell。49 个 cell 输出少于 5 个不同值；158 个可排名 cell 中仅 8 个超过 ρ=0.3，其中 5 个来自 closed model 读 pitch，3 个其置信区间明确高于 bar，若排除区间包含 bar 的则仅 1 个。
- 除 3 个 ranked cell 外，所有 cell 误差都等于或高于 constant-predictor floor。各系统失败模式不同。
- Table 1：AcoustiClaim 参考系统在 Libri2Mix 上对 SRMR ρ=+0.918、SNR ρ=+0.972、speaking rate +0.497、pause count +0.504、pause rate +0.409、F0 mean +0.434、F0 s.d. +0.165、jitter +0.809、shimmer +0.481、HNR +0.795；Ridge baseline 在 speaking rate 等项上有时更高，nMAE 有高有低；F0 s.d. 和 shimmer 仍高于 constant floor。
- Table 2：外部 panel 大多接近 0；Libri2Mix 上 Audio-Flamingo-3 SNR +0.304、Gemini-3.8-Flash F0 mean +0.311；AMI 上 Gemini F0 mean +0.629、F0 s.d. +0.347。AcoustiClaim 在多数量上显著更高，但 AMI speaking rate 出现 -0.438。
- 参考 decoder 在没有任何 withheld 的情况下，对 95% mixture 用 prose 拒绝 5 个 voice quantities（F0、jitter、shimmer、HNR 等），在 clean twins 上全部陈述，说明它从音频中学到了目标规则。
- 校准阈值后，withholding 约 26.9%±2.8 的 slot；mixture 上 10 个 quantity 平均误差下降，8 个在 every split 上下降；随机 selector 同样 coverage 下误差最多只变 0.6%。
- 线性 baseline 在排序误差上至少与该方法一样好；F0 s.d. 和 shimmer 仍高于 constant floor。

## 一句话评价
AcoustiClaim 将音频语言模型的数值声明从“像不像人类意见”推进到“是否与仪器 ground truth 一致”，并给出了带选择性预测、可解释误差分解和严格 tiering 的基准；其结果显示当前音频语言模型在声学数值测量上普遍接近常数预测器，仅少数 closed model 的 pitch 等维度略超最低相关性门槛。

---

## 29. Inference-Time Target Speaker Unlearning in LLM-Based Automatic Speech Recognition

**作者**: Bo Su, Yueru Yan, Thai Le
**链接**: [2609.30439](https://arxiv.org/abs/2609.30439)
**分类**: Speech Recognition | **关键词**: Target-Speaker Unlearning, Inference-Time Unlearning, LLM-Based ASR, Speaker Diarization, Enrollment-Conditioned Gating, Privacy-Preserving Transcription

# 论文总结：Inference-Time Target Speaker Unlearning in LLM-Based ASR

## 核心痛点
在线会议AI转写系统通常会自动把所有人的语音转成文字，但部分参会者可能不愿被转写（opt-out）。现有方案存在明显缺陷：
- **事后处理**（如按说话人过滤音频段）：属于after-the-fact，且当语音重叠时会误删其他说话人的内容；
- **重新训练模型**：计算代价高昂、不切实际，尤其对基于复杂LLM架构的现代转写系统，且opt-out请求可能动态出现在推理阶段。

作者将此问题形式化为 **Target-Speaker Unlearning for ASR (TSU-ASR)**：给定一段多方会议录音与一组opt-out说话人的短语音样本，系统需转写除opt-out用户之外的所有说话人，同时仍需保留**说话人日志（diarization）**——即仍报告"谁在何时说话"，只是不显示其内容（如标记Speaker A在10–15秒说话但不显示文字）。这与以往"只转写某一位目标说话人"的target-speaker ASR不同，是一类新任务。

## 方法创新
1. **Enrollment-Conditioned Gating (ECG) 模块**：一个轻量、可即插即用的门控模块，附加在**冻结的双流语音LLM**（base model为TagSpeech）上，可在推理时动态支持新的opt-out说话人——即使是ECG训练阶段未见过的人。
2. **双流架构适配**：基座模型使用两个Zipformer编码器——语义编码器（内容）与语音编码器（说话人信息），各接projector送入Qwen2.5-7B LLM，输出XML格式的文本、说话人标签与时间戳。
3. **帧级匹配与内容抑制**：ECG先用同一语音编码器计算帧级语音特征 v_t 与enrollment embedding e_k，再用两层MLP结合 [v_t; e_k; cos(v_t, e_k)] 得到匹配分数 g_{t,e_k}∈[0,1]；多目标时取最大分数；随后对语义流做 s_t ← s_t · max{g}，从而在其说话时"打乱/抑制"内容路径，而语音路径保持不变以维持diarization。使用连续分数（而非二值）便于反向传播。
4. **仅训练ECG**：基座参数全部冻结；训练时以0.5概率随机选择录音中的说话人作为目标并删除其文本、保留标签与时间；同时加入未出现在录音中的说话人作为负样本。损失函数 L = α·CE(ŷ, y⁻) + β·BCE(g, m)，兼顾输出引导与说话人匹配能力。更换opt-out说话人只需更换语音样本，无需再训练。

## 实验结果
- **数据集**：AMI（英语，单远场麦克风）与AliMeeting（普通话，第一远场通道）；AMI 2,607段、AliMeeting 4,373段；测试集按约10%时长划分，AMI 16位、AliMeeting 60位说话人，训练/测试说话人无重叠以验证泛化性。
- **主要指标**：CLR（Content Leakage Rate，含CLR-all与CLR-rare，越低越好）、cpWER-R/gWER-R（AMI）与cpCER-R/gCER-R（AliMeeting，仅针对retained说话人）。
- **关键结果**：opt-out说话人的转写准确率显著下降——AMI从72.3%降至48.2%，AliMeeting从73.6%降至27.3%；而保留说话人的转写错误率基本维持不变（如AMI Retain-only cpWER 36.7→37.0）。实验还区分Retain-only、Forget-only、Mixed-overlap、Mixed-nonoverlap四类片段，并指出重叠语音是条件(1)与条件(2)相互竞争的难点。

## 一句话评价
本文首次提出推理时目标说话人"遗忘"的TSU-ASR任务，用轻量即插即用的ECG门控模块在冻结LLM-ASR上动态抑制指定说话人的内容而保留其说话人日志，为视频会议提供了实用的隐私保护转写方案，但重叠语音场景下遗忘与保留的平衡仍是明显挑战。

---

## 30. CLEAR: Online Speech Content Leakage Estimation through Cross-ASR Disagreement

**作者**: Bhawana Chhaglani, Tanvi Kandepuneni, Jeremy Gummeson, Prashant Shenoy
**链接**: [2609.30415](https://arxiv.org/abs/2609.30415)
**分类**: Speech Privacy / Privacy-Preserving Speech Processing | **关键词**: cross-ASR disagreement, speech content leakage, reference-free runtime privacy estimation, adaptive privacy, ASR ensemble

# CLEAR: Online Speech Content Leakage Estimation through Cross-ASR Disagreement

## 核心痛点
- 信号级语音隐私机制（如 Kirigami、低通滤波、下采样、选择性采样等）在抑制语言内容的同时，需要保留下游音频感知任务所需的声学信息。
- 这些机制的隐私参数通常离线在数据集上选定，部署后保持固定；但语音内容泄漏高度依赖输入，在不同话语、不同说话人之间差异显著。例如 Kirigami 固定阈值 τ=0.5 时，对抗 PER 在 0.45–1.0 之间变化；说话人 S1（加拿大英语男性）平均 PER 为 0.61±0.30，而 S2（德语口音非母语男性）平均 PER 为 0.94±0.17。
- 现有泄漏评估依赖 WER/CER/PER 等指标，需要真实转写文本作为参考；但在隐私保护部署场景中，原始转写不可用也不应保留，因此无法在线计算，导致系统无法实时判断隐私暴露、向用户报告风险，或动态调节保护强度。
- 因此，需要一种 reference-free 的运行时语音内容泄漏估计信号。

## 方法创新
- 提出 CLEAR（Content Leakage Estimation through ASR disagreement）：利用异构 ASR 系统之间的分歧作为无需参考的语音内容泄漏度量。
- 核心直觉：若隐私变换后语言内容仍可恢复，独立训练的异构 ASR 会倾向于输出相似假设；若语音被遮蔽，ASR 假设会越来越不一致。
- 给定隐私变换后音频 x'=T(x)，使用 N 个异构 ASR A={A1,...,AN}，得到假设 hi=Ai(x')；对假设进行小写化、去标点、空白归一化后，计算两两序列相似度 sij=SeqSim(hi,hj)，并定义成对分歧 dij=1-sij。
- CLEAR 分数 c 为所有 ASR 对的平均分歧：c 越高表示 ASR 分歧越大、估计可恢复性越低（隐私越好）；c 越低表示多个 ASR 恢复出相似内容，潜在泄漏越高。
- 特殊处理空假设：若恰好一个 ASR 输出为空，则 dij=1；若两个都为空，也设 dij=1（表示零泄漏），同时单独跟踪空假设比例 e，以捕捉 ASR 恢复失败。
- 潜在泄漏词识别：若一个词被至少两个异构 ASR 恢复，则视为可能泄漏；通过 MatchingWords 取所有 ASR 对的并集 L，可向用户报告“哪些内容可能泄漏”，而不仅是抽象隐私分数。
- 隐私控制反馈：当 CLEAR 低于目标隐私水平时，系统可提高隐私变换强度并重新计算 CLEAR；当泄漏足够低时，可放宽变换以保留更多声学信息，实现运行时自适应隐私。

## 实验结果
- 数据集：从 Mozilla Common Voice 中选取 100 条约 2 秒的语音，覆盖不同性别、年龄和口音；真实转写仅用于离线评估 ground-truth 泄漏，运行时不会提供给 CLEAR。
- 隐私变换：主要使用 Kirigami，扫描 13 个阈值/操作点（τ=0.3 到 0.9），并额外评估对其他隐私变换的泛化性。
- 与 held-out 强 ASR 对抗者得到的 transcript-grounded 泄漏相比，CLEAR 在 utterance-configuration 对上达到 Spearman ρ=0.80，在操作点平均上达到 ρ=0.98。
- 潜在暴露词识别正确率为 61.3%，可提供可解释的运行时隐私反馈。
- CLEAR 优于使用单个 ASR 置信度分数，并可跨不同隐私变换工作。
- 找到最优异构 ASR 子集/集成，可在低延迟下估计语音泄漏，RTF=0.15。

## 一句话评价
CLEAR 将异构 ASR 分歧转化为无需真实转写的运行时语音内容泄漏估计，使隐私从固定离线配置变为可监控、可通信、可自适应调节的运行时属性，在隐私-效用权衡中具有实用价值；但其效果依赖 ASR 集成的多样性与质量，泄漏词识别精度仍有提升空间。

---


# Arxiv Daily Deep Report - 2026-11-26

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 7
---

## 1. UMAI: UM Aware Inference with a Frozen Qwen3-ASR

**作者**: Gyeongmin Kim
**链接**: [2611.34256](https://arxiv.org/abs/2611.34256)
**分类**: Speech Recognition | **关键词**: filled pauses, disfluency detection, Qwen3-ASR, linear discriminant analysis, probing, verbatim transcription

# UMAI 论文总结

## 核心痛点
语音识别器常把 uh、um 等填充停顿（filled pauses）从转写中删除，导致转写不逐字。对逐字转写进行微调虽能恢复填充词，但会改变词选择、标点和数字格式等其余输出。本文在更严格约束下研究该问题：识别器只运行一次，已识别词必须原样保留，仅在词间插入 [uh]/[um] 标签；删除标签即可还原 Qwen3-ASR 原文。

## 方法创新
提出 UMAI（UM Aware Inference），以冻结的 Qwen3-ASR-1.7B 为基座，在单次贪心解码中记录内部状态，并在解码后做读出，不使用梯度下降训练参数。

- **Gap 建模**：在每个输出词前以及 EOS 结束处定义 gap，记录 28 层解码器在步骤 g 与 g+1 的状态。
- **音频证据**：混合 448 个解码器注意力头，用 EM 拟合对齐头；由注意力构造 gap 音频窗口，并在 5 类（静音、词、填充词、截断词、重复）帧后验上池化，得到 20 维音频特征；还构造下一词窗口特征以处理词首拉长类似填充词的情况。
- **两阶段 LDA 检测**：Stage 1 对每层、每步骤拟合 5 类 LDA，协方差用 OAS 收缩，保留 224 个相对 O 类的对数后验比；Stage 2 在 245 维输入上再拟合 5 类 LDA，输入含 Stage 1 分数、音频特征和 Qwen3-ASR 已写填充词指示；结束 gap 使用单独模型。
- **校准与插入**：用 isotonic regression 将分数校准为概率，超过阈值 τ（默认 0.75）即插入标签；两阶段线性结构可在推理时折叠为单一矩阵。
- **uh/um 形式选择**：结合 Qwen3-ASR 最后一层对 uh/um 单 token 拼写的语言模型偏好分数，以及投影帧上的音频 um-vs-uh 对数似然比，经二类 LDA 与 isotonic 校准得到 um 概率，Rk>0.5 写 [um]，否则 [uh]。
- **无需梯度训练**：类均值、收缩协方差有闭式解，注意力头权重由 EM 得到，概率表由 isotonic regression 得到；产出约 5.7 MB 的独立文件。

## 实验结果
- **AMI eval**：填充词 F1 从 Qwen3-ASR 的 12.2 提升到 τ=0.75 时的 82.6，Exact F1 从 12.1 到 80.0；τ=0.50 时 F1 可达 84.7。
- **Nyra Verbatim Benchmark**：F1 从 37.2 提升到 96.5，Exact F1 从 36.6 提升到 94.9；默认阈值 τ=0.75 在 Nyra 上选择，因此该阈值下 Nyra 结果偏乐观。
- **效率**：总处理时间仅增加 14%。
- **约束保持**：UMAI 不改变任何已识别词，仅插入标签；删除标签可恢复原识别文本。

## 一句话评价
UMAI 证明了冻结 ASR 的单次解码内部状态已包含足够信息来恢复大部分被丢弃的填充停顿，以无需梯度训练、保持原文不变的轻量读出方式显著提升填充词 F1，但阈值校准与 Nyra 上的乐观性仍需在更独立设置下审视。

---

## 2. Investigation of generalization to unseen audio generation models in audio--text semantic-alignment score prediction

**作者**: Yuki Okamoto, Noriyuki Tonami, Takao Kawamura, Keisuke Imoto, Ryotaro Nagase, Riki Takizawa, Minoru Kishi, Shinnosuke Takamichi
**链接**: [2611.34626](https://arxiv.org/abs/2611.34626)
**分类**: Audio-Text Semantic Alignment Evaluation / Text-to-Audio Generation | **关键词**: text-to-audio generation, audio-text semantic alignment, alignment score prediction, domain generalization, gradient reversal layer, subjective evaluation

## 核心痛点
- 文本到音频生成（TTA）需要可靠评估生成音频与输入文本之间的语义对齐程度。
- 现有基于学习的 audio–text semantic-alignment score prediction 模型主要在与训练数据相同的 TTA 模型所生成音频上评估，对未见生成模型的泛化能力尚未被系统研究。
- 预训练音频编码器可能捕获生成模型特有的声学/伪影特征，导致对齐分数预测模型在 unseen TTA 模型上性能下降。

## 方法创新
- 首先分析生成音频是否包含可识别生成模型的特征：使用冻结的预训练音频编码器（BYOL-A、CLAP）加两层 MLP 分类器，在 XACLE Challenge 2026 数据集上识别 8 个 TTA 模型。高分类准确率说明生成音频中存在明显的模型特有特征。
- 基线模型采用 XACLE Challenge 2026 官方 baseline：BYOL-A 音频编码器、RoBERTa 文本编码器、BiLSTM 与线性层组成的分数预测器；损失为 Lscore = Lmse + λ1Lcon。
- 提出使用带梯度反转层（GRL）的生成模型分类器进行对抗训练：通过 GRL 连接生成模型分类器与中间表示，总损失为 Ltotal = Lscore + λ2Ladv。GRL 在前向传播中近似恒等，在反向传播中反转并缩放梯度，以促使音频编码器学习对语义对齐预测有用但对生成模型来源不敏感的表征。
- 实验比较两种 GRL 配置：Only audio encoder（GRL 仅作用于音频编码器）与 All（文中表述为 GRL 作用于 score predictor 一侧的配置）。

## 实验设置
- 数据集：XACLE Challenge 2026，包含真实录音与 8 个 TTA 模型生成音频、文本描述及 11 点主观对齐分数。
- 将 8 个生成模型划分为两个不相交集合：Set A 包括 AudioLDM、Tango2、AudioGen、Stable Audio；Set B 包括 AudioLDM2、Tango、Make-an-Audio 2、TangoFlux。在一个集合上训练，在另一个集合上测试。
- 每个集合包含 2,000 个训练、1,000 个验证、1,000 个测试 audio–text 对，并进行平衡采样。
- 评价指标：SRCC、KTAU、LCC、MSE；另外用冻结音频编码器表示训练 4 类生成模型分类器，以衡量表征中保留的生成模型特有信息。

## 实验结果
- 基线泛化能力有限：在 Set A 上训练时，Set A 的 SRCC 为 0.339，但 unseen Set B 仅 0.144；在 Set B 上训练时，Set B 的 SRCC 为 0.393，但 unseen Set A 降至 0.210。
- GRL 在部分设置中有效：Set A 训练时，Ours All 将 Set A 的 SRCC 从 0.339 提升到 0.413，将 unseen Set B 从 0.144 提升到 0.161；Set B 训练时，Ours All 将 unseen Set A 从 0.210 提升到 0.241。
- GRL 效果依赖应用位置和训练数据：Set B 训练时，Ours Only audio encoder 在 Set B 上取得最高 SRCC 0.412，但在 unseen Set A 上与基线相当或略低。
- 生成模型特有信息分析：Set A 训练时，Ours All 的分类准确率从 0.928 升至 0.951，未降低；Set B 训练时，Ours All 从 0.942 降至 0.835。Only audio encoder 未降低分类准确率（Set A 0.929，Set B 0.952）。说明 GRL 对生成模型特有信息的抑制并不稳定。

## 结论
- 预训练音频编码器确实能捕获生成模型特有特征；audio–text semantic-alignment score prediction 模型在 unseen TTA 模型上存在明显性能退化。
- 基于 GRL 的对抗训练在某些设置下可提升预测性能，但其抑制生成模型特有信息的效果有限，且受训练数据与应用位置影响。

## 一句话评价
- 该文首次系统揭示 audio–text semantic-alignment score prediction 在 unseen TTA 模型上的泛化缺陷，并验证 GRL 对抗训练的部分有效性，但方法仍不足以稳定消除生成模型特有信息。

---

## 3. Music Similarity Estimation from Jukebox Embeddings

**作者**: Johannes Grafinger, Gerhard Widmer, Jan Schlüter
**链接**: [2611.34346](https://arxiv.org/abs/2611.34346)
**分类**: Music Information Retrieval (Music Similarity Estimation) | **关键词**: music similarity estimation, Jukebox embeddings, generative music model, embedding repurposing, PCA, Jensen-Shannon divergence, distance space normalization, cold-start recommendation

## 论文基本信息

- **标题**：Music Similarity Estimation from Jukebox Embeddings（提出方法简称 **JukeSim**）
- **作者**：Johannes Grafinger、Gerhard Widmer、Jan Schlüter（奥地利林茨约翰开普勒大学计算感知研究所 / LIT AI Lab）
- **任务**：基于内容的音乐相似度估计（content-based music similarity estimation）

## 核心痛点（Motivation）

1. **冷启动问题**：音乐推荐系统依赖协同过滤，新曲目缺乏用户交互数据时失效；基于音频内容的相似度可以绕开这一困境。
2. **问题本身定义模糊**：相似度是多方面的，却被强行压到单一维度，且没有明确客观的“正确答案”。
3. **方法演进存在断层**：早期手工特征方法（MFCC+GMM、单高斯、Fluctuation Patterns、Seyerlehner 特征集）与近年深度度量学习/分类方法从未在**同等条件下**被比较过。
4. **生成式模型的表征潜力未被验证**：Jukebox、MusicGen 等生成式音乐模型的 embedding 已被用于 tagging、旋律转写、节拍跟踪等任务，但**尚未有人研究其用于音乐相似度估计**。

## 核心假设与方法创新

**核心假设**：生成式音乐模型既然能生成/续写音乐，其内部表征应当隐含对歌曲的强语义理解，可被“再利用”于相似度估计。

**方法流程**（embedding 提取 → 歌曲级聚合 → 距离度量）：

1. **Embedding 提取**：使用 Jukebox（大规模自回归 Transformer 生成式音乐模型，72 层，每帧 4800 维，单次最多约 24 秒 / 8192 帧 @344 fps），借助 `jukemirlib` 提取；固定取音频**中心片段**，只用**单层**（默认第 36 层，此前被用于 auto-tagging 与 music understanding），并注意不超出单次前向的上下文长度。
2. **数据压缩**：
   - 全量表征规模惊人（500 段 24s 音频 ≈ (500, 72, 8192, 4800)，32-bit 下 >5000 GB）；
   - 措施：精度降至 16-bit → 只保留一层 → 用 librosa 重采样到 100 Hz（得每曲 2378×4800 矩阵）→ 逐维标准化后做 **PCA** 投影到前 P 个主成分（P ≪ 2378，实验中取 50/100/150）。
3. **歌曲级全局模型**（两种）：
   - **均值向量**（对帧取平均，P 维）；
   - **单高斯模型**（均值 + 经验协方差矩阵）。
4. **相似度/距离度量**：
   - 均值模型：Cosine、Euclidean、Manhattan；
   - 高斯模型：Symmetric KL Divergence (SymKLD)、Fréchet Inception Distance (FID)、以及**改进版 Jensen-Shannon 散度 (AltJSD)**——用 μ_m、Σ_m 的近似（式 1、2）得到**闭式解**（式 3），避免了对两成分 GMM 精确混合分布进行采样估计，大幅降低计算量。
5. **距离空间归一化 (DSN)**：对距离矩阵每个元素减去其所在行与列的均值、除以标准差，可减少 hub / orphan 现象（Pohle 与 Seyerlehner 等曾使用）。
6. 相似度 = 距离的相反数/倒数。

**三项贡献**：① 给出用生成模型 embedding 做相似度估计的可行策略；② 与现有公开的度量学习方案对比；③ 首次在统一评测下打通“手工特征 SOTA”与“深度学习 SOTA”之间的比较链路。

## 实验设置与结果

- **评测代理指标**：Precision@k（P@k，k=1..20），因人工听测成本过高；该指标已被证明与人类判断相关（[18]）；有艺术家信息时启用 **artist filter**（检索时跳过同艺术家曲目以防混淆）。
- **数据集**：
  - **Homburg**：1886 段片段，9 种流派，含艺术家信息；
  - **Ballroom**：698 段 30 秒国标舞音乐，8 种舞种。
- **调参结论（图 1）**：
  - 基于**单高斯**的三类距离全面优于基于**均值向量**的三类距离；
  - **AltJSD 总体最佳**（例外：Homburg 在 P=150 时表现不佳）；SymKLD 在 Homburg 较好、FID 在 Ballroom 较好；
  - PCA 维度具数据集依赖性：Ballroom 上随 P 增大全面提升；Homburg 上 P=50→100 多数指标提升但 AltJSD 在 P=50 最佳，P=150 时各度量趋于接近（作者推测与 Homburg 音频片段长度上限有关）。
- **总体结论**：JukeSim 与现有基于度量学习的方法**性能相当（on par）**，且二者**均优于最好的手工设计方法**；代价是 JukeSim 所需计算量高于其他方案。

## 一句话评价

本文以“生成式模型内部表征可复用”为假设，用 Jukebox 单层 embedding + PCA + 高斯建模 + AltJSD 闭式距离构建了 JukeSim，在流派检索代理指标上与深度度量学习方法持平并超越手工特征基线，首次补齐了新旧方法学之间的可比性缺口，但其价值更偏“可行性验证（viability）”，计算开销与评测代理指标的局限仍待解决。

---

## 4. Beat This! Live - Online Beat and Downbeat Tracking by Predicting the Future

**作者**: Bánk Juhász, Gerhard Widmer, Jan Schlüter
**链接**: [2611.34277](https://arxiv.org/abs/2611.34277)
**分类**: Music Information Retrieval - Online Beat and Downbeat Tracking | **关键词**: online beat tracking, downbeat tracking, causal model, low-latency streaming, label shifting, Shifted Causal Local Max, Beat This!

## 核心痛点
- 高精度 beat/downbeat 跟踪模型大多为离线模型，依赖完整音频、双向序列建模或较大时间上下文，因此难以用于实时音频流。
- 仅实现因果性还不够：实时场景要求低延迟；人耳通常可感知约 50 ms 的音频延迟，部分人更敏感。
- 原始 Beat This! 的后处理通过局部极大值和 downbeat snap 进行，需要“窥视未来”，因此违反因果性。
- 流式推理若使用因果全自注意力，计算复杂度会随历史帧数线性增长，最终难以跟上输入帧率。

## 方法创新
- 以离线 Beat This! 为基础：输入 T×128 频谱图，使用 rotary transformer 和 beat/downbeat 双任务头，输出 T×2 概率；多数实验变体采用较小的 128 维 transformer。
- 系统性因果化改造：
  - 将 stem/frontend 中的 2D 卷积替换为因果卷积，并通过 padding/cropping 保证因果性。
  - 训练时的 batch normalization 在推理阶段替换为固定的逐帧线性变换，以满足因果性。
  - 频率方向 partial transformer 因不违反因果性而保留；时间方向 partial transformer 和六个 transformer block 的双向注意力替换为因果自注意力。
- 流式推理改造：采用 causal sliding-window attention，只让固定局部窗口内的前序 token 参与注意力，使计算复杂度不随历史增长，同时保留短程依赖。
- 延迟处理与“预测未来”：
  - 输入使用 centered STFT（1024 样本窗，22.05 kHz），带来约 23 ms 的隐式 lookahead。
  - 训练时将真实 beat/downbeat 标签向后移动若干帧，使模型提前预测未来事件，从而为推理计算留出时间，并支持零延迟甚至负延迟预测。
- 后处理创新：提出 Shifted Causal Local Max（SCLM）。对于标签偏移模型，不在当前帧立即决策，而是在包含未来少量预测的对称窗口内选择局部极大值，从而在保持因果性的同时实现更有效的峰值检测；downbeat 由 beat 门控，并可用 cooldown 抑制误触发。

## 实验结果
- 在 GTZAN 数据集上，相比当前在线 beat tracking 的 state of the art 方法 BeatNet+：
  - beat F1 从 80.6 提升到 86.7；
  - downbeat F1 从 56.5 提升到 74.1。
- 论文强调该模型是竞争性的 online 模型，但尚不是完整的 real-time 实现。
- 主要贡献包括：将 Beat This! 系统性改造为因果在线变体；分析因果结构修改与后处理策略对精度和延迟的影响；提出 SCLM 后处理方法。

## 一句话评价
该工作系统地把离线 Beat This! 改造为低延迟因果在线模型，通过标签前移与 SCLM 后处理显著提升在线 beat/downbeat 跟踪性能，是面向实时 MIR 应用的实用化强基线。

---

## 5. InstructTTS-OPD: On-Policy Distillation for Multi-Objective Instruction-Following TTS

**作者**: Haitao Li, Tian Tan, Yuguang Yang, Guanrou Yang, Wenhao Guan, Chenglin Li, Shan Yang, Xie Chen
**链接**: [2611.33937](https://arxiv.org/abs/2611.33937)
**分类**: Instruction-Following Text-to-Speech (Instruct-TTS) | **关键词**: Instruct-TTS, On-Policy Distillation, GRPO, Multi-Objective Optimization, Flow Matching, Conflict-Aware Velocity Fusion

# InstructTTS-OPD 论文总结

## 核心痛点
Instruct-TTS 要求模型在自由文本指令下朗读目标文本，并同时满足三个目标：**指令遵循（IF）**、**可懂度（WER/CER）**、**自然度/音质（MOS）**。现有做法通常用 GRPO 等强化学习，将多目标压缩为单一标量奖励；但标量化会丢失方向信息：当不同目标对输出修改方向不一致时，梯度贡献相互抵消，优化会偏向最容易提升的目标，造成三目标之间的“跷跷板”式此消彼长。重新调整奖励权重只能移动平衡点，不能消除目标冲突。

## 方法创新
1. **将 on-policy distillation（OPD）引入 Instruct-TTS**：不再只用单一标量奖励，而是在学生模型自身 on-policy rollout 上匹配多个单目标教师的 velocity field，提供稠密、逐步的监督信号。
2. **三轴奖励设计**：
   - IF：蒸馏 Qwen-Omni 作为低成本代理，逼近昂贵的 Gemini 判断；
   - WER：使用去方言数据训练 WER 教师，避免模型通过“不说目标方言”来降低 WER，从而拖累 IF；
   - MOS：采用 DNSMOS 替代存在中英文偏置的 UTMOS，避免把中文读成外语口音。
3. **三教师 GRPO 训练与领域路由**：分别用 GRPO 训练 IF、WER、MOS 三个单目标教师；在 OPD 中按数据域将每个 rollout 路由到 IF 或 WER 教师，同时让所有 rollout 跟随 MOS 教师。IF 与 WER 路由到不相交话语，使二者可同时提升而不产生明显 trade-off。
4. **冲突感知 velocity fusion**：由于音质目标与指令遵循存在冲突，直接加性融合会重新引入跷跷板。作者提出在融合前将 quality target 投影到与主目标相反方向的正交补空间，即移除与主目标冲突的分量；这是一种逐帧几何操作，标量奖励 RL 难以表达。
5. **DiTAR + Flow Matching 实现**：基于约 0.7B 的 DiTAR 架构（0.5B Qwen 语言模型、193M local decoder、48M aggregation encoder，vocoder 冻结），将部分 ODE 采样转为 SDE 以支持 on-policy rollout，并记录状态、条件、采样输出与转移 log-prob；GRPO 使用组内标准化优势并加 KL 正则，蒸馏与策略梯度共享均值 µθ 优化目标。

## 实验结果
论文摘要与引言声称：融合模型在 **IF、WER、MOS 三个目标上同时优于 scalar-reward GRPO**；IF 与可懂度可以共同提升而无 trade-off；冲突感知 velocity fusion 显著降低 IF/quality 的权衡。由于提供的论文片段在 3.3 节后被截断，未包含具体实验表格、数值、消融与人类评估细节，因此无法在本总结中给出精确指标。

## 一句话评价
该工作把图像生成中的 OPD 多教师融合迁移到 Instruct-TTS，并针对语音奖励偏差和目标冲突设计领域路由与冲突感知 velocity fusion，为多目标 TTS 后训练提供了避免标量奖励跷跷板的新范式；其完整有效性仍需结合全文实验数据与消融进一步验证。

---

## 6. Evaluating Cine and Tagged MRI-to-Speech Synthesis with Complementary Metrics and MRI-Free Controls

**作者**: Karlo Vrancic, Fangxu Xing, Jiachen Zhuo, Maureen Stone, Jerry L. Prince, Jonghye Woo
**链接**: [2611.33786](https://arxiv.org/abs/2611.33786)
**分类**: Articulatory-to-Acoustic Speech Synthesis (MRI-to-Speech) / 医学影像驱动的语音合成与评估 | **关键词**: Cine MRI, Tagged MRI, Speech Synthesis, Log-mel Spectrogram, Evaluation Framework, Corr2D, MRI-Free Control, Glossectomy, ESTOI

## 核心痛点

- **临床动机**：舌切除术后，患者的舌部运动与语音生成之间的关系尚不清楚。如果能利用动态 MRI 定量描述内部舌运动与决定可懂度的声学特征之间的联系，就能为手术规划和康复提供量化依据。
- **现有做法的隐患**：已有研究把 cine MRI 或 tagged MRI 翻译成 2D log-mel 频谱图，并用预测频谱与真实频谱之间的二维 Pearson 相关（Corr2D）来衡量“成像模态携带了多少声学信息”，报告值在 0.665–0.820 之间。但 Corr2D 从未与“不含 MRI 的预测器”做过校准。
- **为什么随机基线不够**：本领域使用的语料只有一两句按节拍器说出的短句，因此不含 MRI 的声学模板仅凭复现句子的共有结构就能拿到高分；同时，Corr2D 是对展平频谱图做的一次整体相关，会忽略预测的缩放和偏移，而 log-mel 本身带有所有被试、所有帧共有的强静态频谱倾斜。因此，分数里有一部分来自“表征本身”，而不是模型或成像的贡献。

## 方法创新

1. **固定主干、只变输入**：构建一个图像到频谱图的网络，并让所有条件共享同一个 backbone，使输入配置和对照组成为唯一变量。网络结构包括：逐帧 Vision Transformer（2 层、4 头，8×8 patch，d=128，采用 graph-Laplacian 位置编码——由像素网格图拉普拉斯的前 8 个非平凡特征向量经符号不变网络生成）；逐帧池化 patch token；沿时间线性重采样到目标 mel 长度；再接膨胀一维卷积解码器，输出 64 通道 mel；训练损失为 log-mel 上的 MSE；用 Griffin–Lim 重建波形。
2. **四种输入配置**：cine MRI（1 通道）、单方向 tagged MRI（1 通道）、双方向 tagged MRI（2 通道）、cine + 双方向 tagged 融合（3 通道）。融合为早期融合，把对齐后的帧堆叠成通道；另有 late-fusion 变体（每个输入一个编码器、逐帧平均特征）。
3. **两个无需 MRI 的对照（核心贡献）**：
   - **静态均值谱基线 A_h**：对训练集频谱逐帧时间平均，再广播到目标时长——包含整体频谱平衡，但不含任何时序信息。
   - **队列模板 B_h**：把训练说话人的同一句频谱沿时间重采样对齐后平均，再拉伸到留出被试的时长——代表“平均说话人”，唯一知道的被试信息是录音时长（受训模型也同样获得该时长）。
   - 两者都参与完全相同的留一被试交叉验证（leave-one-subject-out）评估，且不读取任何图像。
4. **多指标评估**：Corr2D、log-mel 倒谱距离（LMCD，对 64 通道 log-mel 的 DCT 第 1–13 系数使用 mel-cepstral distortion 公式）、ESTOI（对预测与真值 mel 都做 Griffin–Lim 重建以固定声码器）；辅助分析用 sharpness（Laplacian 方差）和 SSIM。
5. **稳健性验证**：三种位置编码、编码器时序注意力模块、与指标不变性相匹配的训练目标（相关性型损失）下重复；并做被试内模态配对比较与患者与健康人的对比分析。

## 数据与实验设置

- Siemens 3.0T TIM Trio 或 PRISMA，分段梯度回波序列，采集配对的 cine MRI、双方向 tagged MRI 与音频。
- 44 名被试（26 名健康人、18 名舌切除术后患者），说“a souk”或“a geese”，36 人完成两项任务；因此两个语句不是独立重复，故分别报告、不合并。
- 图像使用原生 128×128 分辨率，名义上每句 26 帧；音频转为 22.05 kHz、64 通道 log-mel（1024 点 FFT、256 跳），得到 55–123 帧（0.6–1.4 s）。
- 每句排除一条记录（“a souk”的 Sub 1、“a geese”的 Sub 2，因为只有 17.2 s、8.1 s 的未裁剪扫描录音），最终 n=37 与 n=41；该排除对结论无影响（模板 Corr2D 仅移动约 0.003，24 项模板-配置检验的显著性无一改变）。
- 每折使用相同随机种子重新训练 40 个 epoch；少数 subject-task 在某些配置下不足 26 帧（多方向 tagged 只保留共享的 DICOM 实例号）；仅取 26 帧齐全的被试子集分析时，cine 优于双方向 tagged 的结果仍显著（p<0.001）。

## 主要结果

- **队列模板（完全不用 MRI）** 的 Corr2D 达 **0.745（a souk）/ 0.664（a geese）**；**静态均值谱基线（完全无时序）** 达到模板分数的 **87%–89%**（0.663 / 0.574）。
- **没有任何训练配置在 Corr2D、LMCD 或 ESTOI 上超过模板**；8 项主要对比中有 7 项在 Corr2D 上显著落后。12 次训练运行的 Corr2D 区间为 0.692–0.740（a souk）和 0.566–0.645（a geese），均值全部低于模板；最接近的两个（a souk 的 cine，在两种目标函数下）与模板统计上持平（p=0.36）。
- 该结论在三种位置编码、编码器时序注意力、与指标不变性匹配的训练目标下均成立；late-fusion 变体同样显著落后（0.720 / 0.604，p≤0.002）。
- **模板自身的分数依赖目标渲染方式**（同一批录音在不同渲染下为 0.35–0.75 与 0.34–0.67），因此不能跨研究直接比较绝对 Corr2D。
- **cine 与 tagged MRI 在被试内存在一致的差异**，但差异方向取决于所用指标。

## 一句话评价

这是一篇“评估方法论”而非“新网络”的论文：它用一个固定主干和两个零成本的、无需 MRI 的对照，证明该领域广泛使用的绝对 Corr2D 分数无法证明模型真的从 MRI 中恢复了声学信息——因为一个不含图像、只含“平均说话人 + 时长”的模板就能追平甚至超过所有 MRI 驱动的模型。其提出的对照可由任何研究用自己的训练录音复现，“模型相对对照的余量”才是成像真正贡献的度量。这为 articulatory-to-acoustic 映射类研究提供了必要且可复用的评测规范。

---

## 7. Psychophysics of Duration Perception in Multimodal Large Language Models

**作者**: Auss Abbood, Zihao Fu, Nigel Collier
**链接**: [2611.33176](https://arxiv.org/abs/2611.33176)
**分类**: Multimodal Large Language Models (Audio Perception) | **关键词**: 时长感知, 多模态大语言模型, 旋律识别, 心理物理学, 时序分组, 上下文学习, 音频感知

## 核心痛点
现有关于语言模型时间感知的研究主要集中于文本场景：一类工作考察语篇层面的时长/紧迫感主观判断，另一类工作考察智能体对任务耗时的估计与校准。然而，多模态大语言模型（MLLMs）越来越多地用于需要感知时间流逝的任务，其时间感知边界以及与人类基线的差异仍缺乏系统理解。论文指出，现有音频/音乐基准要么测试物理属性的粗粒度判断，要么测试固定刺激集上的音乐分组分类，并未通过改变音符时值来估计“依赖时值的时序分组”何时崩溃。

## 方法创新
论文借鉴心理物理学与格式塔心理学，将“时长感知”操作化为旋律识别任务：熟悉的旋律应能在不同速度和音高下保持可识别，而当音符时值被拉长到一定程度，音符之间的时序绑定/格式塔分组瓦解，旋律不再被识别。该边界被用来定义时长感知极限。

实验基于 Warren et al. (1991) 的人类研究设计，包含训练、筛选和时长缩放三个阶段：
- 使用 8 首著名旋律（如 Twinkle Twinkle Little Star、Happy Birthday 等），并额外用 11 首扩展旋律验证。
- 旋律以等时音符呈现，音符时值集合为 D = {round(40(√2)^k) ms : k ∈ {0,...,12}} ∪ {3600 ms}。
- 通过从第 3 或第 4 个音符进入并循环移位，避免模型仅凭开头音符识别。
- 训练阶段测试零样本多项选择与带标签上下文示例两种变体；筛选阶段采用静态单次循环呈现，并将人类 6/8 的准入标准缩放为 12/16 试验。
- 输入格式包括 text+audio 与 audio-only；后者用 TTS 将指令转为音频并与旋律合并为单一音频文件。
- 时长缩放阶段对每个时值独立测试，每个旋律在 14 个时值上各 2 次试验，共 28 次试验。

## 实验结果
- 测试了 21 个音频/全模态模型；大多数模型在无带标签上下文示例时，无法仅凭参数知识可靠识别正常速度的著名旋律。
- 提供上下文示例后，有 7 个模型能够可靠识别旋律，且多数模型的识别峰值落在人类识别中位数区间内。
- 泛化能力有限：
  1. 上下文示例的速度会移动识别峰值，可靠识别被限制在示例音符时值附近的狭窄范围内；
  2. 旋律标题会引入预测偏差，将标题替换为中性代码可降低偏差并提升准确率；
  3. 提供科学音高记谱示例并不能阻止多数模型在长音符时值下准确率下降。
- 作者总结：在人类中，识别窗口是感知者的属性；在当前模型中，识别窗口很大程度上是提示词的属性，因此难以识别模型内在的感知极限。

## 主要贡献
1. 提出一种心理物理学方法，用旋律识别测量 MLLMs 的时长感知极限，并与人类基线比较。
2. 证明表观时序识别极限会随上下文示例速度移动，挑战其作为稳定感知边界的解释。
3. 证明旋律标签会偏置听觉识别，中性代码可减少偏差并提高准确率。

## 一句话评价
该论文用巧妙的旋律识别心理物理范式揭示了当前 MLLMs 的“时长感知边界”高度依赖提示上下文而非稳定的内在感知能力，为多模态时间感知评估提供了可复用的实验框架。

---


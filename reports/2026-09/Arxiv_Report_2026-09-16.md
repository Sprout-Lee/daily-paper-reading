# Arxiv Daily Deep Report - 2026-09-16

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 52
---

## 1. Counting Closures in Spanish Trills: A Multi-Corpus Acoustic Study

**作者**: Mateo Cámara, Maria F. Alcala-Durand
**链接**: [2609.17424](https://arxiv.org/abs/2609.17424)
**分类**: Acoustic Phonetics / Speech Production | **关键词**: Spanish trill, rhotics, closure detection, phonotactic context, acoustic phonetics, multi-corpus, quality filter, autocorrelation period estimator

# 论文总结

**论文标题**：Counting Closures in Spanish Trills: A Multi-Corpus Acoustic Study
**作者**：Mateo Cámara, Maria F. Alcala-Durand
**机构**：Universidad Politécnica de Madrid, Spain

## 核心痛点
- 西班牙语颤音 /r/ 传统上被描述为一小段舌部闭合序列，但跨语料库的大规模声学证据稀缺。
- 自动计数方法常基于整流包络峰值，会把每个闭合及其释放分别计为事件，导致计数约翻倍；该偏差与发声频谱密度及说话人特征共变。
- 先前社会语音学研究对说话人性别、音位环境的作用结论不一致；缺乏可靠音素级切分和大规模闭合计数研究。

## 方法创新
- 提出基于闭合的检测器：锚定中频带 500–3500 Hz 能量极小值，并要求后续释放验证；候选需在 50 ms 窗口内下降至少 5 dB 且低于最大值 40%，组合包络下降至少 3 dB；释放需在 3–25 ms 后达到局部最大值的 40%。
- 当 token 至少有 3 个闭合时，周期步骤会移除相邻间隔均偏离中位数超过 2 个标准差的闭合。
- 固定、检测器无关的质量过滤器：时长 50–200 ms（因 60 ms 以下周期分未定义，实际有效下限为 60 ms），至少 80% 帧为浊音，包络周期性得分 ≥0.40（中频带包络自相关在 25–55 ms 滞后上的峰值，对应 18–40 Hz 颤音范围）。
- 独立交叉检测器：基于自相关估计 20–60 ms 的主导闭锁间隔，n = round(duration/period)，仅作内部一致性检查，不共享闭合事件逻辑。
- 统计上为避免伪重复，聚合到每说话人一个观测或每说话人×语境一个观测；使用 Mann–Whitney U、Kruskal–Wallis H、Dunn 事后比较、bootstrap 置信区间和线性混合效应模型。

## 实验设置与结果
- 数据：六个西班牙语语料库，356 名说话人，16,836 个候选 token，质量过滤后保留 3,560 个 well-formed 颤音 token（21%）。语料包括 TEDx（1,481）、Heroico（1,151）、Glissando（762）、DIMEx100（81）、ALBAYZIN（46）、PRESEEA（39）。保留率从 Heroico 的 45% 到 DIMEx100 的 1.3% 不等。
- 主要结果：闭合计数的中位数为 2；闭锁间隔中位数约 36 ms，与经典描述文献一致。
- 说话人层面：音位环境是唯一稳健且中等效应的因素；起始位置颤音（词首和 /n,l,s/ 后）比元音间 rr 有更多闭合。
- 性别：直接计数闭合时未发现稳健的性别效应。
- 分析集为浊音、周期性、良好成形的颤音，因此参考中位数描述的是 well-formed trills，而非连续语音中颤音的实际出现率。
- 贡献：方法上主张可扩展的颤音测量应直接计数闭合，而非整流包络峰值；实证上给出跨语料库参考值和可复现测量流程。

## 一句话评价
该工作通过闭合锚定检测与严格质量过滤，澄清了西班牙语颤音闭合计数的测量偏差，并在多语料库规模上证明音位环境比说话人性别更稳健地影响颤音结构。

---

## 2. Optimal transport of image sources for interpolation of room impulse responses with moving sources

**作者**: Jesper Brunnström, Filip Elvander, Isabel Haasler
**链接**: [2609.17237](https://arxiv.org/abs/2609.17237)
**分类**: Room Impulse Response Interpolation (Geometrical Acoustics / Audio Signal Processing) | **关键词**: Optimal transport, Image-source method, Room impulse response interpolation, Geometrical acoustics, Partial optimal transport

## 核心痛点

房间脉冲响应（RIR）在几何声学中可由自由空间中的一组**镜像源**（image sources）表示，其位置与接收端无关，因此便于对接收端位置做插值。然而当**物理声源移动**时，所有镜像源也随声源同步移动：

- 每个镜像源的位置依赖于物理声源位置，导致 RIR 插值变得困难；
- 镜像源的**可见性**同时取决于声源与接收端位置，因此起点与终点的两组镜像源集合大小不一定相同（I0 ≠ I1），存在“某些点在另一端不存在”的情况；
- 在未知房间几何（无法获得墙面信息）的前提下，镜像源位置只能从实测声数据估计，且顺序未知，需要在两组点之间找到对应关系并丢弃无匹配的点。

这本质上是一个带“丢弃”的指派（assignment）问题，适合用**部分最优传输（Partial Optimal Transport, POT）**求解。

## 方法创新

### 1. 问题建模
假设声源沿直线轨迹从 s0 移动到 s1（sτ = (1−τ)s0 + τs1），镜像源高阶位置可写作 T_W(s) = H_W s + b_W（H_W 为正交 Householder 矩阵乘积）。目标是**在未知房间几何的情况下**，仅由端点处带噪的镜像源估计 ν0、ν1 恢复轨迹上任意 τ 的度量 µτ。

### 2. 位移插值（Displacement Interpolation）
论文的核心几何洞察是：**物理声源移动时，每个镜像源移动的距离与物理声源相同**，即

∥r_i^(0) − r_i^(1)∥₂ = ∥H_Wi(s0−s1)∥₂ = ∥s0−s1∥₂ （利用 H_Wi 的正交性）。

因此镜像源轨迹也是线性的：r_i^(τ) = (1−τ)r_i^(0) + τ r_i^(1)。基于此提出插值格式（式 9）：由 POT 得到的传输计划 M 对“两端都存在”的点做位移插值，对仅在某一端存在的点按 (1−τ) 或 τ 的权重逐渐淡出。

### 3. 统计模型驱动的代价函数
将真实残差建模为 ρ_i = γ d_i + ε_i，其中 γ = ∥s0−s1∥₂ 为已知长度、d_i ~ U(S²) 为未知方向的单位球均匀向量、ε_i ~ N(0, σ²I) 为合并高斯噪声。边缘化方向参数后得到残差分布：

p(ρ) = 1/(2πσ²)^(3/2) · exp(−(r²+γ²)/(2σ²)) · sinhc(γr/σ²)，其中 r = ∥ρ∥₂，sinhc(x)=sinh(x)/x。

由此得到最大似然指派问题，并与平衡 OT 等价，从而导出代价：

- **c_ML(x_i, y_j) = r_ij² + γ² − 2σ² log sinhc(γ r_ij / σ²)**（统计最优，式 14）
- **c_Eu(x_i, y_j) = r_ij²**（常用欧氏代价，σ≫γ 时与 c_ML 渐近等价）
- **c_SI(x_i, y_j) = (r_ij − γ)²**（“声源先验”代价，γ≫σ 时与 c_ML 渐近等价）

### 4. 有原则的 dummy 代价 ξ 选择
POT 中仅满足 c(x_i, y_j) ≤ 2ξ 的质量会被传输。论文引入可解释参数 α = 匹配对落在接受域之外的概率，利用 r ~ σχ₃(γ/σ)（3 自由度非中心卡方分布）的已知 CDF，数值求解 Prob(c(x,y) > 2ξ) = α，从而对每种代价函数得到一致的 dummy 代价。

### 5. 与已有工作的差异
- 与 [22] 的 POT 方法不同：本文处理**移动声源**而非移动接收端，而移动声源场景下插值才是必需的；
- 与 [23] 用 OT 处理移动声源不同：本文**显式建模镜像源几何结构**，这是关键创新；
- 提供了有充分动机的代价函数与 dummy 代价。

## 实验结果

论文通过**仿真实验**验证：

- **评价指标**：（1）指派误差（assignment error，式 17，基于理想传输计划 M* 的 L1 偏差归一化）；（2）估计 RIR 的归一化均方误差（NMSE）。
- **结论**：使用所提出代价函数的 POT 相比替代方案（如欧氏代价等）表现更有效，说明统计建模导出的 c_ML/c_SI 代价及合理的 dummy 代价能显著提升插值性能。
- 图 1 展示了不同代价函数随 r 的变化曲线（归一化最小值到 0）以及接受域随 α 的划分，验证 c_ML 在 σ≫γ 与 γ≫σ 两端分别退化为 c_Eu 与 c_SI。

## 一句话评价

本文将“移动声源下镜像源等距位移”这一几何先验编码进统计模型，推导出可解释的 ML 代价与 dummy 代价，用部分最优传输同时解决镜像源指派与轨迹插值问题，是几何声学与最优传输交叉的一个理论扎实、动机清晰的创新工作。

---

## 3. Differentiable and Severity-invariant Discrete Tokens for Dysarthric Speech Recognition

**作者**: Huimeng Wang, Xurong Xie, Mengzhe Geng, Haoning Xu, Jiajun Deng, Youjun Chen, Chengxi Deng, Xunying Liu
**链接**: [2609.16855](https://arxiv.org/abs/2609.16855)
**分类**: Dysarthric Speech Recognition | **关键词**: dysarthric speech recognition, discrete tokens, differentiable K-means, severity-invariant regularization, self-supervised learning, HuBERT, Conformer

# 论文总结：面向构音障碍语音识别的可微且严重程度不变离散 Token

## 1. 核心痛点
- **构音障碍语音识别（Dysarthric ASR）仍然困难**：病理语音数据稀缺、与正常语音失配严重、说话人级差异大。
- **离散 token 的优势与代价**：离散 token 便于序列压缩、统一文本-语音建模、降低存储/传输成本并支持端侧推理；但其性能通常低于连续特征，用于构音障碍 ASR 时退化更明显。
- **退化原因**：① 离散 token 提取与 ASR 后端的训练目标不一致，造成任务相关信息损失；② 病理严重程度导致的说话人异质性，使面向正常语音的端到端 K-means 难以处理。

## 2. 方法创新
论文提出**可微且严重程度不变（DSI）离散 token**，核心由三部分组成：
1. **迭代离散伪标签更新**：交替执行 token 监督的量化器更新与离散 token 更新，用当前 token 标签优化 HuBERT 编码器和 DKM 量化器，再用更新后的模型重新 tokenize 语料，逐步精炼 token。
2. **端到端优化**：将 HuBERT 编码器、DKM 量化器与 Conformer ASR 后端联合优化，使离散 token 直接学习面向 ASR 的表示；损失为 L_E2E = L_ASR(Y; ASR_CFM(Q_DKM(Enc_HB(O))))，其中 L_ASR = 0.3L_CTC + 0.7L_Att。
3. **严重程度不变正则化（SIR）**：在 E2E 优化中最小化内容平行的病理语音与健康语音、以及不同损伤严重程度组之间的 utterance-level 离散 token 分布差异，从而减少严重程度相关变化。

基础技术包括：HuBERT + bottleneck 模块提取连续表示；DKM 使用负欧氏距离 softmax 计算软分配，配合 Gumbel-Softmax 采样和 straight-through argmax 更新码本；损失包括 L_KM、L_TSP 和 L_E2E。

## 3. 实验结果
- 在 **UASpeech** 和 **TORGO** 两个构音障碍语音语料上评估。
- 使用 DSI token 训练的 Conformer 模型优于可比的 HuBERT 离散/连续特征基线：在 UASpeech 与 TORGO 上分别取得 **2.22%/0.78% 绝对（9.14%/3.41% 相对）** 和 **1.78%/1.06% 绝对（18.43%/11.86% 相对）** 的统计显著 WER 下降。
- 系统组合后，UASpeech 和 TORGO 上最低 WER 分别为 **18.90%** 和 **6.38%**。
- Phoneme-specific T-SNE 可视化显示，SIR 使不同严重程度组的分布重叠更大、边界更不明显，说明其降低严重程度相关变异。
- Qwen-based SpeechLLM 系统上的实验确认 DSI token 可跨后端泛化，并在两个任务上获得一致 WER 降低。

## 4. 一句话评价
本文针对离散语音 token 在构音障碍 ASR 中目标失配和病理异质性两大问题，提出可微、严重程度不变的 token 学习框架，在 UASpeech/TORGO 上取得显著且一致的 WER 改善，方法创新与实证价值兼具。

---

## 4. The Evolving Bottleneck in Speech Generation: Interface Co-design and Staged Alignment from CosyVoice to Qwen-Audio-3.0-TTS

**作者**: Qian Chen, Xiangang Li, Xiang Lv, Han Zhao, Tianyu Zhao
**链接**: [2609.16514](https://arxiv.org/abs/2609.16514)
**分类**: Text-to-Speech | **关键词**: Speech Generation, Text-to-Speech, Bottleneck Relocation, Interface Contract, CosyVoice, Qwen-Audio-3.0-TTS, Flow Matching, Semantic Tokens, Staged Alignment

# 论文总结：The Evolving Bottleneck in Speech Generation

## 核心痛点
- 语音生成需要同时优化语言正确性、说话人相似度、韵律自然度、音质、多语言与方言覆盖、可控性、延迟、长音频稳定性和对不完美参考语音的鲁棒性。
- 这些目标不在同一模块失败，提升一个目标会在别处暴露新约束：适合声学重建的丰富表示可能难以被自回归模型预测；语义 tokenizer 有利于稳定规划却可能丢失表现力线索；强离线模型可能因需要未来上下文而不适合流式；大规模训练混合可扩大覆盖，但 token 准确率与感知质量之间仍有差距。
- 论文反对“模型更大、tokenizer 更好、数据更多”的线性叙事，提出“瓶颈迁移”视角：从 CosyVoice 到 Qwen-Audio-3.0-TTS，进展来自反复重新定位系统的主导瓶颈。

## 方法创新
- 稳定分解：文本和提示 → 自回归语义规划 → 流匹配声学渲染 → 波形。各代均保留“自回归 LM 规划 + 流匹配 FM 渲染”结构，变化的是两者之间的接口契约。
- 四维接口契约 I=(R,O,A,G)：
  - R（Representation）：跨边界传递的表示；
  - O（Ownership）：内容、说话人等因子由哪个模块负责；
  - A（Availability）：推理时接口值何时可用；
  - G（Gradient reach）：哪些目标可跨边界回传梯度。
- 四级瓶颈迁移：
  1. CosyVoice：瓶颈为无监督声学单元难从文本预测；方法为监督语义 token 加流渲染。在多语言 ASR 编码器中插入 VQ，训练 4096 条目码本，LM 预测语义 token，最优传输条件流匹配生成 mel，声码器重建波形。确立“紧凑规划、连续渲染”不变式。
  2. CosyVoice 2：瓶颈为因果可用性与信息泄漏；方法为 FSQ、预训练 LM、LM 中去掉句级说话人嵌入、chunk-aware FM。FSQ 码本为 6561 且充分利用，对比 4096 条目 VQ 仅 23% 利用率。LM 从 Qwen2.5-0.5B 初始化，去掉独立文本编码器和句级说话人嵌入，提示文本和语音 token 仍用于上下文学习，显式说话人嵌入和参考声学条件给 FM。双流式调度交错文本和语音 token，chunk-aware 因果 FM 切换流式与离线掩码。
  3. CosyVoice 3：瓶颈为覆盖和后训练信号；方法为多任务 tokenizer、百万小时数据、更大 LM、DiffRO 可微奖励优化，提升接口可学习性和覆盖。
  4. Qwen-Audio-3.0-TTS：瓶颈为仅 token 容量和模块不匹配；方法为 12.5 Hz token、用连续 LM 隐状态而非 token embedding 条件渲染器、联合与分阶段优化。Token 仍用于语义规划、高效自回归解码和 token 域优化，但不再是渲染器的直接条件接口；语义 token 预测头保留，连续隐状态条件 FM。渐进式训练协调模块而不牺牲有效因子化。
- 理论形式：级联 pθ(z|x) 与 pφ(y|e(z),x)；耦合系统 pφ(y|h,x)，L=L_token+λL_flow，联合训练时 ∇θL_flow≠0。速率不是容量：Bmax = r log2 K bits/s 仅为名义索引预算上界，不是测量熵率；降低帧率缩短 AR 序列，增大 K 可部分恢复表示损失。
- 设计空间定位：离散自回归、连续非自回归、离散非自回归、连续自回归和混合 AR/NAR 系统。应按“谁承载长程规划、谁负责局部声学实现”组织，而非离散与连续二分。

## 实验结果
- 论文为技术回顾，不是合成排行榜。强调四篇源论文时间、数据、checkpoint、评测集、识别器、说话人编码器和部署目标不同，不应把跨论文分数差异解释为受控因果效应。
- 架构主张由文档化模型设计支持；机制主张锚定在源论文内部消融。跨版本数字仅在最新工作于同一表格显式评估新旧 tokenizer 时报告。
- CosyVoice 2 模块消融：在中文、英文和 hard 子集上，预训练 LM 初始化、移除说话人嵌入、VQ 换成 FSQ 逐步降低识别错误。FSQ 使中文 CER 2.56→1.45，英文 WER 3.81→2.57，hard 集 WER 9.66→6.83；说话人相似度变化较小。支持两点：该配置下码本利用率与内容准确率相关；从规划器移除句级说话人向量可改善内容预测，同时系统仍保留显式说话人条件，条件是迁移而非消除。
- 流式消融：离线与流式 LM/FM 组合在标准集上保持相近准确率和相似度。

## 一句话评价
本文用“瓶颈迁移 + 接口契约”重述 CosyVoice 到 Qwen-Audio-3.0-TTS 的技术史，把模块化语音生成的关键从“堆模型与数据”转向“规划器与渲染器之间传什么、何时传、谁负责、梯度如何回流”，对诊断和训练模块化语音生成系统具有方法论价值。

---

## 5. Segmental Posterior Decoding for Audio Moment Retrieval

**作者**: Seungdeok Choi, Seongmin Choi, Inhan Choi, Junho Kim, Jeong-gyu Ban, Yong-Hwa Park
**链接**: [2609.16495](https://arxiv.org/abs/2609.16495)
**分类**: Audio Moment Retrieval | **关键词**: Audio Moment Retrieval, Conditional Random Fields, Posterior Decoding, Segmental CRF, DETR, Temporal Localization

# 论文总结：Segmental Posterior Decoding for Audio Moment Retrieval

## 核心痛点
- 音频时刻检索（AMR）需要在长音频中根据自由文本查询定位最匹配的时间段。
- 现有方法多沿用视频时刻检索中的 DETR 式固定槽解码器，为候选 proposal 分配 proposal-level 置信度分数。
- 这类分数没有在完整时间线的所有竞争性解释上进行全局归一化，不能显式量化某个候选时刻相对于其他可能分段的相对合理性。
- QFL、VFL 等虽改善置信度与 IoU 的对齐，但仍是 proposal 级标定，未改变检索决策规则。

## 方法创新
- 提出 segmental posterior decoding：定义全局归一化的时序分段分布，用半马尔可夫 CRF 建模查询条件下的音频时间线。
- 将前景段和背景帧分别赋予势函数，其中前景段势由起点、终点和段偏置组成；背景帧由背景分数组成。
- 通过前向后向推理计算精确的分段边缘后验，作为候选时刻的检索分数；该分数聚合了所有包含该候选时刻的合法分段。
- 训练时扩展分割空间，把前景跨度及其相邻细分视为不同假设，使真实分割与更丰富的替代解释竞争。
- 训练目标联合使用 NLL 和 minimum-IoU-risk：NLL 提升真实分割的全局概率，IoU-risk 让高 IoU 候选获得更高边缘后验。
- 推理时丢弃 DETR 解码器，以段边缘后验对 top-K 候选排序，再做时序 NMS 去重。
- 与原始 DETR 分支共享 audio memory 并联合优化，不改变骨干特征提取器。

## 实验结果
- CASTELLA dev-test：R1@0.5 53.95、R1@0.7 41.15、mAP 34.68。
- 相比同一网络 DETR slot confidence，R1@0.7 提升 10.91 个百分点，mAP 提升 9.20 个百分点。
- 对比 DETR baseline（47.41/30.76/25.28）、+QFL（50.04/32.96/26.23）、+VFL（51.05/33.14/26.52），所提方法全面领先。
- UnAV-100 zero-shot：R1@0.5 72.33、R1@0.7 61.00、mAP 60.33；QFL/VFL 在该设置下不再优于 DETR baseline，而段边缘解码保持明显优势。
- 消融显示：段边缘解码优于 DETR 置信度、local potential 排序和 Viterbi MAP 解码；对短时刻和长时刻均有改善。
- 添加 span-mean 内容势无显著提升，添加 duration prior 反而下降，说明增益主要来自结构化边缘化而非更复杂的局部评分器。
- 移除 IoU-risk 或禁止相邻 FG 段都会降低性能。
- 在 DCASE 2026 Task 6 排行榜上，41.15 R1@0.7 与最强非集成、非 LLM 提交（41.13、40.70）相当，接近含集成和 LLM refinement 的最佳结果 45.14。

## 一句话评价
该论文指出 AMR 的关键瓶颈之一是检索决策规则，并通过全局归一化的段边缘后验解码显著提升性能，方法无需改变骨干网络且具备跨数据集泛化潜力。

---

## 6. Language Orthogonalization for Zero-Shot Cross-Lingual Audio Deepfake Detection

**作者**: Minu Kim, Ji Sub Um, Hoirin Kim
**链接**: [2609.16458](https://arxiv.org/abs/2609.16458)
**分类**: Audio Deepfake Detection / Speech Anti-spoofing | **关键词**: Audio Deepfake Detection, Cross-Lingual Transfer, Self-Supervised Speech Models, Language Orthogonalization, Language Identification, Zero-Shot Transfer

## 论文总结：Language Orthogonalization for Zero-Shot Cross-Lingual Audio Deepfake Detection

### 核心痛点
- **跨语言部署困境**：语音合成已覆盖 1000+ 语言，但反欺骗（anti-spoofing）基准仍以英语为主，多语言资源覆盖有限。检测器需要在一个训练中完全未出现的目标语言上工作——既无真实语音也无伪造语音可用于适配或校准。
- **S3M 的语言混淆**：自监督语音模型（S3M）虽在音频深度伪造检测中表现强劲，但其表征同时编码了语言身份（language identity）。检测器容易把“语言条件化的声学特征”误当成“可迁移的伪造线索”，导致跨语言（尤其是远距离语言）迁移时性能显著下降。
- **缺乏目标语言数据**：现实场景下无法获取目标语言的标注数据来做自适应。

### 方法创新
- **语言正交化（Language Orthogonalization）**：一种**无目标数据（target-free）** 的岭回归映射，将 S3M 表征中“可被连续 LID 嵌入预测”的语言变化分量减去。
- **具体流程**：
  1. **特征提取**：6 个冻结 S3M 作为话语级特征提取器，对全部隐层做 mean+std pooling、逐层平均并 L2 归一化，得到 2048 维表征 x。
  2. **外部语言参考**：使用在 VoxLingua107 上预训练的 ECAPA-TDNN 提取 256 维连续 LID 嵌入 g（无需语言特定微调），其连续空间具有反映音系、地理、谱系关系的几何结构。
  3. **岭回归拟合**：仅用**源语言真实语音**（bonafide）拟合 W* = argmin ||X_bf − G_bf W||²_F + λ||W||²_F，闭式解 W* = (G_bfᵀG_bf + λI)⁻¹ G_bfᵀ X_bf（λ=0.1）。
  4. **正交化**：对每条话语（真伪均适用）执行 X_orth = X − gW*，减去语言可预测分量，保留伪造线索。
- **动机**：已有工作表明 S3M 音系变化近似位于线性子空间，因此移除线性语言方向即可在无目标数据条件下消除跨语言混淆。

### 实验结果
- **数据集**：SEA-Spoof，六种南亚/东南亚语言——南亚 SA（印地语、泰米尔语）、大陆东南亚 MSEA（泰语、越南语）、海洋东南亚 MRT（印尼语、马来语）。
- **骨干网络**：MMS-300M、XLS-R-300M、mHuBERT-147（多语种预训练）与 wav2vec2-Large-LV60、HuBERT-Large、WavLM-Large（单语预训练）。
- **评估协议**：Leave-N-Out（N=1~5），留出语言完全未见；分类器为类别平衡 L2 正则的逻辑回归（L-BFGS）。
- **主要发现**：
  1. **LID 距离预测迁移难度**：跨语言 EER 与 LID 空间距离正相关（图 3），LID 距离体现语言区域结构；距离越远 EER 越高。
  2. **全面一致提升**：所有骨干与所有 N 设置下 EER 均下降，平均相对降低 9%–17%（如 N=4 时平均从 9.83% 降至 8.19%）。
  3. **远距离迁移收益最大**：单语训练（Leave-5-Out）下，SA×SEA 远距离对提升最大（如 XLS-R 下降 22%）；两语训练（Leave-4-Out）下，受限的同族训练配置提升显著（XLS-R 在 intra-group 降 41%、MRT×MSEA 降 45%），说明正交化可补偿源语言多样性不足。
  4. **表征几何对齐**：正交化后真实语音语言质心的欧氏距离大幅缩小——wav2vec2.0 −70%、HuBERT −59%、WavLM −55%、XLS-R −54%、MMS 与 mHuBERT 各 −44%，跨语言域差距被拉近且保留判别性。
- **结论**：语言正交化是一种无需目标语言数据、可即插即用于多种 S3M 的跨语言音频深度伪造检测增强方法；连续 LID 空间距离可作为刻画迁移难度的清晰度量。

### 一句话评价
通过“减去 LID 可预测分量”的简单闭式岭回归正交化，在严格零样本跨语言设定下稳定降低多种 S3M 的 EER，远距离迁移收益最大，方法轻量、即插即用且无需任何目标语言数据，为跨语言反欺骗提供了一条简洁有效的去语言混淆路径。

---

## 7. StepAudio 3 Music Technical Report

**作者**: Chengli Feng, Zhiyue Wu, Jiahao Song, Zheqi Dai, Boyang Wang, Ruibin Yuan, Junming Gong, Wenxiao Zhao, Jing Guo, Gang Yu, Xiangyu Zhang, Xuerui Yang, Chao Yan
**链接**: [2609.16034](https://arxiv.org/abs/2609.16034)
**分类**: Text-to-Music Generation | **关键词**: 音乐生成, 长音频生成, ABC 记谱, Mixture-of-Experts, Flow Matching DiT, 音乐 Tokenizer, DPO, 可控生成

# StepAudio 3 Music 技术报告总结

## 核心痛点
1. **长篇幅音乐生成中的多尺度协调困难**：完整歌曲需要同时处理旋律发展、段落过渡、歌词与音乐关系等长程结构，以及音色、人声质感、瞬态等细粒度声学实现。
2. **音频表征的生成友好性与重建质量存在权衡**：多码本 RVQ 通常重建更好，但单码本 VQ 作为自回归目标更可预测，更利于长序列音乐一致性。
3. **可控音乐创作需要可读、可修改的中间计划**：全局文本提示只能描述风格、情绪、配器，难以直接控制乐句发展、和弦变化、副歌与主歌旋律关系。
4. **开放域文本控制与显式音乐规划需要统一框架**：如何让模型自身中间计划暴露清晰音乐语义与时间结构，使创作者可在音频生成前检查并修改编曲决策。

## 方法创新
1. **生成导向的音乐表征与渲染器**
   - 在 25 Hz 下对比单码本 VQ、Semantic RVQ、Acoustic RVQ，发现单码本 VQ 更适合自回归生成，尽管多码本 RVQ 声学重建更强。
   - 最终 StepAudio Music Tokenizer 采用 50 Hz、65536 条目单码本，提供更密集时间监督并保持单一 token 流。
   - 使用语义启发的自监督与多任务训练，保留音乐结构和重建相关信息。
   - Flow-matching DiT 预测连续 StepAudio VAE latent，VAE 解码器输出 48 kHz 波形；编解码器独立训练并在自回归模型训练时固定。

2. **显式音乐规划：ABC-CoT**
   - 使用 ABC 记谱表示中间编曲计划，包含 tempo、meter、key、和弦、小节结构、旋律序列等。
   - MoE 自回归模型采用两阶段分解：先生成 ABC-CoT 编曲计划，再以该计划为条件预测 50 Hz 音乐 token。
   - 训练包含 music-to-ABC 与 ABC-to-music 任务，将符号化计划与其声学实现连接。
   - ABC-CoT 作为旋律、和声、节奏、曲式的条件接口，可被创作者检查和修改。

3. **训练流程与对齐**
   - 渐进式多任务课程：大规模预训练建立通用音乐生成、识别、理解能力；多任务中期训练引入显式规划和任务特定参考条件；高质量退火聚焦核心创作任务。
   - 监督微调增强任务执行，DPO 使输出对齐专家对条件遵循和音乐质量的判断。
   - 支持歌曲生成、器乐生成、干声生成伴奏、翻唱歌曲合成，最长 5 分 30 秒。

## 实验结果
1. 经 DPO 的最终模型在 AudioBox Content Enjoyment、Content Usefulness、Production Quality 上取得最高分，并在评估系统中取得最高 MuQ-MuLan 相似度；SongBench 结果有竞争力。
2. 在初步的 Artificial Analysis Music Arena Vocals 排行榜上，Quality Elo 为 1105，仅次于 Suno V5.5 和 Mureka，领先于 Suno V5、MiniMax 模型及其他系统。
3. 报告图 1 展示 MuQ-MuLan、AudioBox-Aesthetics、SongBench 三个基准族上的相对表现，紫色表示 StepAudio 3 Music。
4. 论文片段被截断，未提供完整实验细节、消融设置和精确数值表格。

## 一句话评价
StepAudio 3 Music 是一个技术栈完整的长篇幅音乐生成系统，通过生成导向的单码本 tokenizer、MoE 自回归 ABC-CoT 显式规划、flow-matching DiT 渲染和 DPO 偏好对齐，在主观与客观音乐质量指标上达到有竞争力甚至领先的水平。

---

## 8. Self-Distilled Pronunciation and Accent Control for Neural Text-to-Speech

**作者**: Shuhei Kato
**链接**: [2609.17234](https://arxiv.org/abs/2609.17234)
**分类**: Text-to-Speech | **关键词**: Text-to-Speech, Pronunciation Control, Pitch Accent, Self-Distillation, Parameter-Efficient Fine-Tuning, Japanese TTS

## 论文信息

**标题**: Self-Distilled Pronunciation and Accent Control for Neural Text-to-Speech
**作者**: Shuhei Kato（Independent Researcher / KOWRO Inc., Japan）
**领域**: 神经语音合成（TTS）中的发音与音高重音控制

## 核心痛点

1. **端到端 TTS 丢失了 G2P 前端**：传统级联式 TTS 通过词典查表解决发音，未知词只需加一条词典条目；而基于原始文本训练的端到端 TTS 丢掉了这一环节，遇到生僻汉字、专有名词或领域术语时只能"猜着读"，唯一的补救办法是改动模型本身。
2. **日语还多一层音高重音（pitch accent）问题**：重音是词汇性规定的（lexically specified），读错不仅是"不自然"，听众会在心理词典里检索一个从未被说出的词，代价直接落在**识别（recognition）**上。
3. **已有方案代价高、覆盖窄**：
   - 输入侧控制（如 UtterTune、Sarashina2.2-TTS）需要录音数据——UtterTune 用了 15,097 条人工校正的 JSUT/JVS 对，Sarashina2.2-TTS 用了约 4,000 小时监督微调，且该能力**未包含在公开发布的权重中**。
   - 混合音素/读音输入（CosyVoice 3 的 pronunciation inpainting、GLM-TTS 的混合音素-文本输入）只在基座训练时包含该能力的地方才可控。
   - 免训练编辑（SonoEdit 的闭式权重编辑、FlowEdit 的文本嵌入扰动）需要给定"范例（exemplar）"，一次只能改一个词，且只处理**音段层发音，不处理重音**。
4. **遗留问题**：对已发布模型而言，"事后装这条控制通道"的成本与可达范围（reach）尚不明确。

## 方法创新

### 1. 自蒸馏训练对（Self-Distilled Teacher）——全文的核心思想
- 取一个基座**本来就读对**的常见词 \(w\)，构造含该词的天然载体句 \(c(w)\)；
- 用**冻结的基座**合成 \(c(w)\)，把**它自己的输出**当作目标（teacher）；
- 学生输入 \(\tilde{c}(w)\) 是把 \(w\) 替换为带标签的重音片假名读音后的同一句；
- 蒸馏目标：\(\tilde{c}(w) \rightarrow \text{base output for } c(w)\)。
- 由于 teacher 与 student 描述的是**同一句话**，模型只需学会"遵守显式的读音与重音指令"，其余一切不变。
- **完全不需要录音、人工标注或语料库**——只需要一个文本集和公开前端（G2P），训练数据选择时才用公开 ASR 当工具。

### 2. 控制信号
- 目标词被替换为 `<PHON_START> + 带重音片假名 + <PHON_END>`；
- 撇号标记音高下降后的那个 mora（accent nucleus），斜杠标记重音短语边界，无标记即平板型（heiban），记法遵循 JEITA IT-4006；
- 跨不同基座仅标签拼写不同。

### 3. 训练方式（参数化是次要的）
- 实例为 rank-16 LoRA（\(\alpha=64\)），只作用于 query/key/value/output 投影 **+ 仅两个 tag token 的 embedding 行**，其余全部冻结；
- 移动参数 <0.5%，flow/vocoder 栈完全不碰，单张消费级 GPU 约 **1 小时**训练完；
- 作者明确声明不为低秩适配本身的创新性背书，任何保持合成栈冻结的适配方式都应可行。

### 4. 词表与数据设计
- 533 词 × 10 载体句，在 10 个语义域、mora 首辅音行、四种重音类型上均衡；
- 对最难的 **odaka**（尾高型）刻意过采样至 15%：其音高下降落在**后接助词**上，孤立时听不出来，因此所有 odaka 载体句都把助词紧跟在目标词后；为此专门增设第 10 个语义域（身体/人称词）来补充常见 odaka 名词；
- 与评测集（difficult / katakana / Joyo）在表层形式或规范化读音上冲突的 50/533 词被剔除，**训练与评测词表在构造上不相交**。

### 5. 部署形态："注册一次，自动生效"
- 维护一个 **registry**，把表层形式映射到带重音读音（{reading, accent index} 或直接写带重音片假名）；
- 路由器在合成时对**整句**跑公开前端，在**词素边界**匹配已注册表层形式，然后：
  1. 只用标签包裹匹配到的 span，携带该条目的重音读音；
  2. 当前端附带后缀时**把后缀一并吸收进包裹**，避免标签紧邻未转换的原始正字法；
  3. 若无注册表层形式与词素边界对齐，则回退到未编辑基座，并记录"编辑未触发"。
- **第 2 步很关键**：蒸馏时标签总是包裹整个前端 token（含屈折）；若标签在一个 token 内部闭合（词干被标、屈折留在外面），模型会遇到训练中从未见过的序列，实验中会导致**重复 mora 的循环退化**。
- 一个词注册一次后，任何句子中后续出现都自动被纠正，无需逐句标注、无需重训，也**不像逐词编辑器那样需要范例**。

## 实验结果

### 设置
- 四个基座横跨生成范式、codec 与 tokenizer：**Sarashina2.2-TTS**（自回归 LLM）、**CosyVoice 2**（自回归）、**Irodori-TTS-500M-v3**（扩散）、**T5Gemma-TTS**（编码器-解码器）；
- 配方在 Sarashina 上开发，**未调参**直接迁移到其余三个；teacher prompting 与 take 选择按基座不同；
- 评测集：Joyo Kanji Yomi Benchmark 中所有"公开词典 G2P（pyopenjtalk）读错被标 span"的句子，共 **424 条**，在任何适配器被测量**之前**按 (word, reading) 图的连通分量切成 105 条选择半 / **319 条测试半**，词与读音不跨越；
- 参考音色：每项从 **42 个留出音色**（ReazonSpeech 说话人嵌入空间聚类中心，按 hash 在音频存在前分配）中取一个，保证各列可比、且不出现于任何训练或 teacher 生成阶段。
- 评价：读音用 kana 约束 ASR（kana-whisper）打规范化目标词命中（≥0.82 校验）；重音由筛选过的评分员听辨，**Fleiss' κ = 0.85**。

### 主要量化结果（Table 1）
| 指标 | Sarashina | CosyVoice 2 | Irodori | T5Gemma |
|---|---|---|---|---|
| Reading − none（相对不编辑） | +.31 | +.47 | +.25 | +.35 |
| Reading − kana（相对纯 kana） | −.02 n.s. | −.09 | −.07 | −.07 |
| Accent realized | **.89** | .66 | .78 | – |
| 对照 | kana .57 | rec. .96 | none .78 | – |
| Naturalness NI（不劣性，margin 0.15） | **yes** | −.08 no | +.33 no | +.30 no |

- **核心证据**：在 Sarashina2.2-TTS 上，标签在未见词上实现规定重音的比例为 **0.89**，而纯 kana 仅 **0.57**（kana 无法表达重音），kana 在其中**一对都没赢**；自然性无可测损失（NI 通过）。
- **迁移性**：同一配方未调参迁移到另外三个基座，**三个都迁移了读音能力**（+0.25 到 +0.47，319 词）；重音在 CosyVoice 2 上每三词对两词（.66，但对照修过录音数据的 rec. 高达 .96），在 Irodori 上未迁移（.78 与 none .78 持平）；自然性四个基座中只有开发基座 Sarashina 未受损，其余三个均未通过 NI。
- 论文明确"定位了原因"（§4.4、§4.6）：T5Gemma 因基座自身读得太差，1,932 个 take 中删掉 1,068 个只留 864 个 teacher（覆盖 427/483 词），其结果只是该配方在该基座上的**下限**而非上限；CosyVoice 2 的 teacher 天然带音色（其 LLM 输入拼接说话人嵌入），Irodori 的 teacher 在合成参考音色库上循环。

### 明确声明的 Non-claims
- 不为低秩适配、不为"用特殊 token 标音素 span"本身（E2 TTS 已做）主张新颖性；
- 不主张语言无关性；
- 不测句级字符错误率（改为测退化，§4.2），也不针对同音词消歧。

## 一句话评价

该论文用"让冻结基座给自己当老师"这一极简自蒸馏训练对，在**不录一句音、不标一条数据、不用任何语料**的前提下，把可同时指定读音与音高重音的控制通道事后装进已发布 TTS，并在多个异构基座上验证了读音能力的可迁移性——方法优雅、成本极低、实验严谨（κ=0.85、词表不相交、42 音色哈希分配、测试集预先切分），但重音与自然性的跨基座迁移仍不稳定，且只在开发基座 Sarashina 上实现了"重音+自然性无损"的双赢。

---

## 9. SongCraft: Unified Song Generation and Editing with Reconstructive Learning

**作者**: Haohe Liu, Varun Nagaraja, Gael Le Lan, Xinhao Mei, Zhaoheng Ni, Vikas Chandra, Abdelrahman Mohamed, Yangyang Shi
**链接**: [2609.16315](https://arxiv.org/abs/2609.16315)
**分类**: Song Generation and Editing | **关键词**: Song Generation, Song Editing, Reconstructive Learning, Latent Flow Matching, Representation Alignment, Phoneme Alignment, Beat Conditioning

## 核心痛点

- **生成与编辑分离**：现有歌曲生成和歌曲编辑通常被当作两个独立任务，缺少统一模型。
- **编辑方法局限**：
  - 基于反演（inversion）的方法（如 AudioLDM、MelodyFlow、MEDIC、DITTO）需要注入噪声后重生成，需仔细调节噪声水平：噪声太少无法有效编辑，噪声太多则破坏原始内容，且输出随机。
  - 基于修复（inpainting）的方法（如 SongCreator、Seed-Music）需要手动指定编辑边界，只能处理时间局部编辑，难以应对全局属性改变（如音色转换/歌手身份转换）。
  - 基于配对数据微调的方法依赖精心构建的前后配对数据，构建困难，只能覆盖易于模拟的操作（如加/减声音）。
  - ACE-Step / FlowEdit 类直接编辑方法仍需超参数调节，在大幅修改时表现不足。
- **生成质量挑战**：端到端流匹配模型以歌词为条件时，常出现跳词、重复等语言错误；节拍是音乐的基本要素，但此前没有工作探索歌曲生成中的节拍条件；REPA 在 VAE 潜在空间上的作用尚未被探索。

## 方法创新

- **统一框架与重建预训练**：将生成和编辑视为条件谱上的两个点。稀疏条件（文本描述、歌词）用于生成，模型自由决定其余音乐属性；密集条件（词级歌词时间戳、人声 MIDI、和弦进行、说话人嵌入、学习到的残差音频编码）用于重建目标，从而支持编辑。
- **重建即编辑**：训练模型从一组可解释属性重建音频。训练后这些属性成为控制旋钮：修改任意单一属性并保持其他属性固定，即可产生定向编辑，例如改歌词、换歌手音色、改旋律。无需配对编辑数据，也无需噪声注入采样。
- **SongCraft 模型**：基于潜在流匹配（latent flow matching）的生成与细粒度编辑统一模型。
- **生成侧三项技术**：
  1. **词级音素对齐**：在词边界对齐文本和音素嵌入，并通过交叉注意力提供给模型；相比简单拼接音素和文本序列，提供清晰的词-发音对应，加快发音学习、提升清晰度。
  2. **节拍条件**：显式提供节拍和强拍位置，显著提升输出音乐性。
  3. **VAE 潜在空间表示对齐（REPA 扩展）**：将 VAE 潜在空间与预训练音乐理解模型的特征对齐，产生语义上有意义的潜在表示，提升生成质量。
- **权衡研究**：系统研究残差编码器瓶颈容量如何控制重建保真度与编辑灵活性之间的权衡。

## 实验结果

- SongCraft 在评估的歌曲生成基线中取得**最低词错误率（WER）**，同时保持有竞争力的音频质量。
- 单个模型可支持歌词、人声旋律、节拍、歌手身份等属性的编辑。
- 验证了重建质量与可编辑性之间的权衡，并对各组件进行了消融验证。

## 一句话评价

SongCraft 通过“从可解释属性重建音频”的预训练思路，把歌曲生成与细粒度编辑统一到一个潜在流匹配模型中，无需配对数据和噪声调参即可实现可控编辑，并在生成清晰度（WER）上超过现有基线，是歌曲生成与编辑统一建模的一次重要尝试。

---

## 10. EMODY Flow: Emotion-Aware Audio-Driven Full-Body Motion Generation

**作者**: Harsh Kumar Agarwal, Xavier Alameda-Pineda, Olivier Perrotin
**链接**: [2609.16011](https://arxiv.org/abs/2609.16011)
**分类**: Audio-Driven Full-Body Motion Generation (Co-speech Gesture Generation) | **关键词**: Emotion-Aware Motion Generation, Flow Matching, Co-speech Gesture Generation, Omni-modal LLM, Mimi Audio Codec

# EMODY Flow：情感感知的音频驱动全身动作生成

## 核心痛点
1. **具身响应缺口**：全能模态大语言模型（Omni-modal LLM，如 Qwen-3 Omni）虽能理解文本、音频、图像、视频，但仅输出语言，无法生成与语音和情感状态同步的**全身动作（身体姿态 + 面部表情）**。
2. **情感条件被抑制**：论文识别并定义了一个关键失败模式——当 flow-matching 模型同时接收高维音频嵌入与离散情感标签时，低维情感标签被高维音频信号压制（属于条件生成器对“弱条件信号”利用不足的已知现象），导致无论指定何种情感，生成的动作几乎完全相同、趋于情感中性。
3. **既有方案依赖专用编码器**：现有协同语音手势生成方法多基于单独训练的音频编码器，丢弃了基础模型内部已计算的丰富上下文表征；情感可控方法则依赖显式的解耦模块或情感编码器。

## 方法创新
- **复用 Omni-LLM 内部音频嵌入**：首次直接利用 Qwen-3 Omni 的 Talker 组件内部使用的 Mimi 音频编解码器（512 维嵌入，24 kHz 下 12.5 codes/秒，取 8 条残差流），无需训练或对齐额外音频编码器，也无需运行非确定性的波形合成步骤。手势、唇动与语音天然保持同步。
- **双并行 DiT 生成器**：分别生成 **SMPL-X 身体姿态**（θ∈R^165 与平移 t∈R^3）和 **FLAME 面部表情**（blendshape ψ_f∈R^100）；每个模块仅约 35M 参数，6 层、16 注意力头、隐藏维 512。
- **条件注入方式**：通过 AdaLN 将时间步正弦编码与情感标签（8 类情感 + 1 类无）嵌入求和为统一条件向量，每块回归 9 个调制参数（每个子层的 shift/scale/gate），使情感均匀调制所有子层。
- **训练时辅助情感分类器**：强制生成动作具有情感可辨识性，从而恢复情感敏感性，作为完整解耦的轻量替代方案（仅在训练时使用）。
- **实用训练技巧**：① 时序帧打乱正则化（减少动作抖动）；② 唇同步辅助损失（FLAME 唇部 blendshape 上的 L2 损失，权重与主重建损失相同，缓解面部不同步）。
- **流匹配建模**：采用线性插值路径 x_t=(1−t)x_0+t x_1，目标速度 u=x_1−x_0，网络预测速度，推理时用自适应 RK45（dopri5）求解 ODE。生成 300 帧（10 秒）序列，长音频可自回归扩展。

## 实验结果
- **BEAT2 手势质量达到新 SOTA**：FGD 0.302、Beat Correlation 0.853、Diversity 24.62，分别较此前最佳结果提升 **26%、5%、62%**。
- **加入情感控制代价小**：开启情感控制后 FGD 仅小幅升至 0.362，仍为次优水平。
- **零样本迁移**：无需领域微调即可在 TFHP 上实现零样本面部动画。
- **定性分析**：通过生成手势的多维标度（MDS）分析，展示出清晰的情感分离动作。

## 一句话评价
EMODY Flow 以轻量（约 35M 参数/模块）流匹配框架复用冻结 Omni-LLM 内部的 Mimi 音频编码，并通过训练期辅助情感分类器巧妙破解“情感条件被高维音频抑制”的难题，在协同语音全身动作生成上同时实现了 SOTA 质量与有效的情感可控性。

---

## 11. Acoustic Image Source Interpolation with Optimal Transport Barycenter

**作者**: Yuyang Liu, Rumeshika Pallewela, Jesper Brunnström, Isabel Haasler, Filip Elvander
**链接**: [2609.15981](https://arxiv.org/abs/2609.15981)
**分类**: Room Acoustics / Acoustic Signal Processing | **关键词**: Room impulse response, Image source method, Optimal transport barycenter, Point cloud interpolation, Room acoustics

## 核心痛点
- 房间冲激响应(RIR)可通过镜像源模型(ISM)估计，但前提是已知物理源的镜像源点云(ISPC)。
- 当声源移动时，整个ISPC会随源位置改变，传统方法通常需要重复声学测量并重新估计ISPC，过程不直接且成本高。
- 通过推断房间几何可辅助估计，但几何误差在高阶反射中容易累积，且基于有限源位置的估计可能产生有偏或不完整的房间模型。
- 本文目标：不显式恢复房间几何，直接从已知源位置的ISPC插值得到新源位置的ISPC。

## 关键观察与问题建模
- 关键观察：物理源的小位移会诱导每个对应镜像源产生相同位移，但方向在缺乏房间几何信息时未知，因此可用位移不变性构造几何惩罚。
- 实际ISPC因边界散射和采样量化误差存在位置扰动，需要鲁棒地同时处理镜像源关联与目标点云定位。
- 将ISPC表示为等权离散概率测度，用最优传输(OT)重心框架联合估计镜像源关联（传输计划）和目标ISPC。
- OT ground cost 设计为 C_ij^(k)(Y) = (||x_i^(k) - y_j||_2 - rho^(k))^2；无扰动时正确排列对应零代价。

## 方法创新
1. **OT重心框架**：把ISPC插值建模为OT重心问题，联合估计关联与靶点云位置。
2. **Grid-based association barycenter**：在固定网格上求解，问题为线性规划，即固定支撑离散Wasserstein重心的标准形式；凸但精度受网格分辨率限制；选取质量最大的N个网格点作为估计ISPC。
3. **Free-support association barycenter**：直接在连续空间优化支撑，避免细网格带来的计算成本。由于联合问题非凸，采用交替优化：
   - Step 1 OT数据关联：给定当前支撑Y，构造代价并求解固定支撑OT线性规划，得到软关联P^(k)。
   - Step 2 支撑插值：固定传输计划，对每个支撑点y_j最小化加权平方距离残差：min_y sum_k sum_i P_ij^(k)(||x_i^(k)-y||_2 - rho^(k))^2，并用基于特征值的加权平方距离近似求解。
   - 迭代直到RMS坐标变化≤τ或达到最大迭代次数Lmax。
4. **初始化策略**：Uniform、All-PC circular（在所有K个已知ISPC的镜像源周围按半径rho^(k)采样候选点）、One-PC circular。

## 实验设置与结果
- 使用模拟2D数据；房间为3×4 m矩形，但插值方法假设房间几何未知。
- 每个物理源的ISPC包含N个最多二阶反射的镜像源，按ISM生成。
- 每个镜像源加入独立高斯扰动Δ_i^(k) ~ N(0, σ_x^2 I)，模拟墙面散射与采样量化误差。
- K个已知物理源置于均匀间隔圆形阵列上。
- 评估所提方法的三种初始化策略。
- 由于提供的论文片段被截断，未包含完整数值结果；实验部分主要展示了2D仿真设置与初始化对比方案。

## 一句话评价
本文提出一种基于最优传输重心的ISPC插值框架，可在声源移动时无需重复测量地估计新位置镜像源点云，并给出凸网格版与非凸自由支撑版两种实现，为高效灵活的室内声学建模提供了有前景的新思路。

---

## 12. Directivity-Conditioned Low-Latency Neural Filtering for Speech Enhancement in Hearing Aids

**作者**: Lennart Uphaus, André Merboldt, Markus Hofbauer, Timo Gerkmann
**链接**: [2609.15760](https://arxiv.org/abs/2609.15760)
**分类**: Binaural Speech Enhancement for Hearing Aids | **关键词**: directivity pattern, hearing device, binaural speech enhancement, low-latency, FiLM, neural directional filtering, OnlineSpatialNet, Mamba, IPD

# Directivity-Conditioned Low-Latency Neural Filtering for Speech Enhancement in Hearing Aids

## 核心痛点
- 现有神经方向滤波（NDF）能够在推理阶段调整方向图的方向和形状，但忽略了助听器真实约束：场景高度动态、麦克风位置随头径和助听器佩戴变化、头影效应、以及严格的延迟限制（≤10ms）。
- 既有 NDF 方法如 FiLM-JNF 基于 FT-JNF，总延迟约 40–50ms，不适合助听器。
- 直接缩短 STFT 窗来降低算法延迟会降低频域分辨率，使 FiLM-JNF 性能显著下降。
- 经典 MVDR 波束形成器依赖导向矢量/DoA 估计，在低 SNR 和非语音干扰下不稳定。
- 助听器场景希望保留空间感知，而不是完全抑制干扰，因此需要可配置方向图。

## 方法创新
- 提出 FiLM-OnlineSpatialNet（FiLM-OSN）：在 OnlineSpatialNet 中加入 FiLM 条件层，实现低延迟（10 ms）双耳神经方向滤波。
- 输入为多通道复数 STFT 的实部/虚部拼接；核心由 L 个交替的 cross-band block、FiLM 层和 narrow-band block 组成，输出通道 C=96。
- FiLM 层将 72 维方向图向量线性映射到通道维，在推理时连续控制方向图。
- narrow-band block 使用状态空间模型 Mamba 替代 FT-JNF 中的窄带 LSTM，更好建模长时依赖，并配合时间卷积模块（通道 C'=196）。
- 输出双通道 STFT 系数，经 iSTFT 重建双耳时域信号。
- 提出保持跨通道频谱关系的 IPD 相位正则损失：L1,IPD = L1 + αLIPD，α=0.03，用余弦形式避免相位模糊，并用 |Y0|^2 抑制低能量分量。
- 提出基于余弦的可配置主瓣宽度 W 的方向图 Λ(θ)，并设最大衰减 M（实验中 -20 dB、W=90°），兼顾方向选择性和空间感知。

## 实验设置与结果
- 数据集：WSJ0 语音 + BTE 助听器 BRIR/HARTF 仿真；5 个说话人，4 麦配置，T60 0.2–0.5s；训练/验证/测试为 6000/1200/600 BRIR，结合 5 种方向图。
- 基线：FiLM-JNF（32ms 和 8ms 窗）。
- 低延迟设置：8 ms STFT 窗、2 ms hop，总延迟 10 ms；FiLM-OSN 使用 L=4、700k 参数。
- 指标：PESQ、ESTOI、SI-SDR。
- 结果：FiLM-OSN 8ms（L1）PESQ 2.04，ESTOI 77%，SI-SDR 5.66 dB；加入 IPD 后 PESQ 2.06，ESTOI 77%，SI-SDR 5.72 dB；优于 FiLM-JNF 8ms（PESQ 1.72，ESTOI 66%，SI-SDR 2.98 dB），接近放宽延迟的 FiLM-JNF 32ms（PESQ 2.10，ESTOI 74%，SI-SDR 4.70 dB），且参数更少（700k vs 950k）。
- IPD 相位正则对方向图准确重建重要，且略微提升 PESQ/SI-SDR。

## 一句话评价
该工作通过 FiLM-OSN 与 IPD 相位正则，在 10 ms 低延迟约束下实现了接近放宽延迟基线的双耳神经方向滤波，为助听器实时语音增强提供了实用方案。

---

## 13. OpenEnded: An Open-Response Speech Corpus for Speaking Proficiency Assessment with Human Annotations and ALM Supervision

**作者**: Yu-Wen Chen, Eric Zhou, Evelyn Ding, Tianyi Shen, Zhou Yu, Julia Hirschberg
**链接**: [2609.15666](https://arxiv.org/abs/2609.15666)
**分类**: Automated Speaking Assessment (ASA) | **关键词**: automated speaking assessment, open-response speech, speech corpus, audio language models, pseudo-labeling, accuracy fluency prosody assessment

# OpenEnded: 面向开放式回答口语能力评估的公开语料库

## 核心痛点
- 自动口语评估（ASA）的发展受限于公开数据集稀缺，现有工作大多依赖朗读式语音（read-aloud），难以适用于真实开放式交流场景。
- 已有开放式语音数据集（如 Speak & Improve、ICNALE）通常只提供 CEFR 整体水平分数，缺少 utterance 级别的准确性（accuracy）、流利度（fluency）和韵律（prosody）细粒度标注。
- 人工标注耗时且昂贵，需要探索伪标签以降低标注成本；同时，音频语言模型（ALM）在 ASA 伪标签中的应用仍未被充分探索。

## 方法创新
1. **OpenEnded 语料库**：收集普通话母语者在开放式任务中练习英语的语音，约 10,000 条 utterance，包含音频、问题和说话人 ID。
2. **混合标注框架**：从约 10,000 条录音中抽取 1,000 条，由三名高英语水平标注者独立评分，并通过分歧解决、rubric 迭代细化、专家咨询形成高质量测试集；其余约 9,000 条由 ALM 伪标注，构成训练集（6,109 条）和开发集（2,673 条），来自 753 个不同说话人。
3. **隐私与质量控制**：使用 NER 模块识别人名、组织、地缘政治实体、国籍、设施，并用 LLM 检查转写是否含隐私信息；仅保留 10–45 秒的录音。
4. **细粒度评分**：准确性、流利度、韵律均按 1–5 分（poor 到 excellent）标注，并提供详细 rubric。
5. **ALM 伪标签**：提示 ALM 联合预测 accuracy、fluency、prosody 分数，并给出推理理由，实现多任务 ASA 和可解释反馈。
6. **VoxPA 基线**：提出新的 ASA 模型作为更强基线，用于 OpenEnded 基准评测。

## 实验结果
- 在 OpenEnded 测试集上评估 ALM 与现有 ASA 模型，并加入 VoxPA 基线。
- ALM 生成的伪标签用于训练后，效果优于直接使用原始 ALM 评分。
- VoxPA 在所有基线中取得最佳性能，证明所提架构有效，并为 OpenEnded 提供更强基线。

## 一句话评价
OpenEnded 通过“人工高质量标注测试集 + ALM 伪标签训练/开发集”的混合范式，填补了开放式口语评估中 utterance 级 accuracy/fluency/prosody 标注数据的空白，并为 ASA 提供了可复现基准和更强基线。

---

## 14. OLAC: An Overlapped Lossless Audio Codec in the Time-Domain with MDCT Compatibility

**作者**: Jean-Marc Valin
**链接**: [2609.15616](https://arxiv.org/abs/2609.15616)
**分类**: Lossless Audio Coding / Audio Compression | **关键词**: OLAC, lossless audio coding, time-domain aliasing cancellation (TDAC), MDCT compatibility, CELT/Opus, linear prediction, Golomb-Rice coding

## 核心痛点
- 无损音频编码已高度成熟，纯压缩性能提升空间有限。
- 新兴实时无线音频应用需要根据网络容量在损编码与无损编码之间动态、无缝切换。
- 现有独立无损编解码器（FLAC、ALAC、MPEG-4 ALS、IEEE 1857.2、Monkey's Audio 等）大多基于时域线性预测，无法与基于 MDCT 的损编码无缝切换，否则会产生不连续，或需要传输冗余信息来覆盖 MDCT 重叠区并避免量化噪声突变。
- MPEG-4 SLS 使用 IntMDCT 可实现嵌入式/可逆变换，但引入额外复杂度与性能代价。

## 方法创新
- 提出 OLAC（Overlapped Lossless Audio Codec），一种与 Opus/CELT 变换编码模式无缝集成的时域重叠无损音频编解码器。
- 核心贡献：完全在时域内实现与 MDCT 兼容的 TDAC，只使用线性预测，跳过 IntMDCT 方案所需的频域 DCT-IV 变换步骤，保持传统时域无损编码的简单性和低计算开销。
- 架构三阶段：1）仅在重叠区进行可逆 TDAC 加窗，保证 MDCT 兼容；2）前向自适应线性预测去相关；3）用 Golomb-Rice 编码残差。另加可逆预加重以匹配 CELT 信号条件。
- TDAC 使用 CELT 的 Vorbis 窗，平顶窗下仅重叠区加窗；重叠长度固定为 120 样本（2.5 ms），与帧长无关，look-ahead 等于重叠时长。
- 通过提升分解实现可逆 TDAC 旋转矩阵 W，并用整数舍入得到可逆公式，确保完美重构。
- 预测：Burg 谱估计，最大阶 Pmax=63；按总码率最小化截断阶数，典型平均 P≈30；采用 PARCOR/反射系数域渐进阶预测，使帧内仅第一个残差样本完全未预测。
- 低功耗实现：避免 64 位累加器，自适应缩放滤波器系数到 13 bit、信号到 12 bit，使用 16-bit MAC；即使 24-bit 音频，累加也保证在 32-bit 内。
- 系数编码：根据预测增益调整量化分辨率，Q0 与整体预测增益相关，并随已解码反射系数逐步调整后续量化步长。
- 残差编码：Golomb-Rice；正负样本交织为单边分布；传输移位参数 m，支持最多两个子块（8 样本分辨率），并为静音保留特殊 m 值。
- 预加重：CELT 使用 A(z)=1−µz^−1，µ=0.85；整数反滤波为 IIR，为支持随机访问/无缝切换，编码上一帧最后样本模 K 值，K=1+2 floor(1/(1−µ))=13，保证一帧内收敛。
- 立体声：在残差域从左声道预测右声道，预测增益以 1/16 分辨率量化，用 Golomb-Rice 编码；当前版本不对反射系数做通道间预测。

## 集成与切换
- 编码器无法预知某帧能否无损，因此尝试无损编码，若包大于阈值则回退到 CELT 损编码。
- CELT 与 OLAC 切换时复制 TDAC/预加重状态；解码端同样支持任意帧间模式切换。
- 从 CELT 切到 OLAC 时，利用码流中的模 K 值强制去加重滤波器状态收敛；随机 seek 需先解码前一帧，再用模 K 值完成无损收敛。

## 实验结果
- 在自定义自由分发音乐语料上评估：28 首立体声曲目，48 kHz、16-bit PCM，总时长 105 分钟，覆盖 6 个流派。
- 与 FLAC、ALAC、MPEG-4 ALS、Monkey's Audio 比较。结果表 1 显示 OLAC 优于 FLAC，且使用 TDAC 没有带来压缩性能损失；预加重还能改善压缩。
- 帧长影响实验（2.5、5、10、20 ms）表明：OLAC 在短帧下仍保持优势；MPEG-4 ALS 的高阶选项仅适合 20 ms 帧，短帧会严重退化。
- 总体说明 OLAC 在不被 TDAC 惩罚的情况下达到 state-of-the-art 无损压缩，并可用于无缝损/无损切换。

## 一句话评价
OLAC 是一种巧妙且实用的 MDCT 兼容时域无损音频编解码器，能在 Opus/CELT 生态中实现无间断的损/无损切换，同时保持有竞争力的无损压缩性能。

---

## 15. Reducing the Output-Mode Gap in Speech Language Models via Joint-Output On-Policy Distillation

**作者**: Daxin Tan, Dehua Tao, Chengxi Deng, Hanlin Zhang, Xiao Chen
**链接**: [2609.15313](https://arxiv.org/abs/2609.15313)
**分类**: Speech Language Models / Interleaved Speech-Text Generation | **关键词**: speech language models, on-policy distillation, interleaved generation, output-mode gap, spoken question answering

# 论文总结：Reducing the Output-Mode Gap in Speech Language Models via Joint-Output On-Policy Distillation

## 核心痛点
- 在交错文本-声学 token 自回归生成的语音大模型（SLLM）中，生成声学 token 会进入后续文本预测上下文，导致同一语音输入下，S2TS 模式内部文本答案准确率显著低于 S2T 模式答案准确率，作者称之为 Output-Mode Gap (OMG)。
- OMG 量化：S2T accuracy 减去 S2TS internal text accuracy。Step-Audio-2-mini 在 Spoken-MQA 和 speech-rendered GSM8K 上分别达 42.87 和 29.72 个百分点；Baichuan-Audio-Instruct 为 12.41 和 10.39 个百分点。显式推理指令在 VoiceBench-BBH 上进一步扩大 OMG。
- 已有工作多关注输入侧 modality gap，本文关注输出模式差异，保持语音输入和模型固定。

## 方法创新
- 提出 Joint-Output On-Policy Distillation (JO-OPD)，用模型自身更强的 S2T policy 作为 teacher，在 student 生成的 S2TS 轨迹上进行 on-policy 蒸馏。
- 历史投影：teacher 条件于 student 前缀的 text-only projection PT(z<i) 并处于 S2T 模式；student 条件于完整交错历史 H(z<i) 并处于 S2TS 模式。
- 文本蒸馏 LT：在文本词表内比较 teacher 与 student 预测。JO-OPD-Soft 保留 teacher top-k 文本 token 并重归一化；JO-OPD-Hard 使用 teacher 最高概率文本 token 的 one-hot 目标。
- 非文本保持 Lpres：对声学输出和控制 token 预测进行正则，防止共享参数更新破坏原生非文本生成。Step-Audio 2 在共享输出头上对非文本位置用重归一化 top-k reference targets 做 CE；Baichuan-Audio 对 controller 和 codec 分布分别用 reference-to-student KL 正则。
- 总损失 L = LT + Lpres。

## 实验结果
- 模型：Step-Audio-2-mini、Baichuan-Audio-Instruct；训练集 27,847 prompts（Tulu 3 + NaturalReasoning），语音由 flite SLT 合成；评测 Spoken-MQA（1,402）和 speech-rendered GSM8K（1,319），另用 VoiceBench-BBH 1,000 题考察推理指令影响。
- Step-Audio-2-mini 上 JO-OPD-Soft 将 Spoken-MQA 的 OMG 从 42.87 降到 16.26 个百分点，GSM8K 从 29.72 降到 13.04 个百分点；JO-OPD-Hard 也有降低但弱于 Soft。S2T 准确率基本不变。相比 Self-SFT 和 Response-SFT 提升显著，其中 Self-SFT 反而扩大 OMG。
- Baichuan-Audio-Instruct 上 OMG 从 12.41 降到 9.49 个百分点（Spoken-MQA），GSM8K 从 10.39 降到 9.78 个百分点。
- ASR 评测显示 Spoken-MQA 的 spoken-answer accuracy 提升 7.49 个百分点。
- 主要训练设置：1 epoch，固定初始 student 的 S2TS 轨迹；AdamW，batch size 32，learning rate 2e-6；JO-OPD-Soft 文本蒸馏 top-32；Step-Audio 2 preservation top-32，权重 0.05；Baichuan controller/codec preservation 权重 1 和 10。

## 一句话评价
JO-OPD 通过把更强 S2T 策略在 student 自身 S2TS 轨迹上蒸馏，并正则化非文本预测，有效缩小了交错语音-文本生成中的输出模式差距，在多个语音大模型和基准上验证了有效性。

---

## 16. Word Timestamps and Speaker Attribution with a Non-Autoregressive LLM

**作者**: Zvi Kons, Avihu Dekel, Hagai Aronowitz, Vishal Sunder, Ron Hoory
**链接**: [2609.15218](https://arxiv.org/abs/2609.15218)
**分类**: Speech Recognition | **关键词**: Non-Autoregressive LLM, Word-Level Timestamps, Speaker-Attributed ASR, Speaker Diarization, Speech Alignment, Granite-Speech

## 核心痛点

**Granite-Speech-Plus (GSP)** 是一个自回归(AR)、基于 LLM 的富语音转写模型，能在转写中附加**词级时间戳 (TS)** 和**说话人归属 (SAA)** 信息（以文本标签形式）。但其自回归本质加上必须额外生成标签 token，使其推理速度远慢于其他模型，成为实际部署的瓶颈。此外，AR 逐个生成标签无法保证单调性，解码代价高。

论文要解决的问题：如何在**给定转写文本**的前提下，快速、准确地为其标注时间戳与说话人信息。

## 方法创新

作者将 **Granite-Speech-NAR** 的非自回归编辑架构扩展到转写标注任务，提出两个共用同一架构、仅预处理/后处理不同的模型（一个做 TS，一个做 SAA）。

**架构组成（图1）：**
- **音频编码器**：16 层 Conformer，用 CTC-ASR 预训练模型初始化并**冻结**；将第 3 层输出与最后一层输出拼接，得到每帧 2048 维向量（因原始输出含极少说话人信息）。
- **投影器 (Projector)**：单层窗口 Q-Former，对 15 个声学嵌入为一块、用 3 个可训练 query 做 5 倍下采样，输出 10 Hz 帧率。
- **LLM**：基于 Granite-4.0-1B-base，改为**双向注意力**，使每个位置都能关注全部音频/文本/标签 token；通过 LoRA (rank 128) 微调。
- **占位符机制**：对输入转写分词后，在每个词后插入占位符 token，模型需在**单次 NAR pass** 中把所有占位符替换为对应标签，其余 token 保持不变。

**两类标签设计：**
- **SAA**：每个词后插入 1 个占位符；tokenizer 将 0–999 的每个数字编码为单 token，模型对 0–999 的 logits 做 argmax 选说话人 ID，最后后处理成 `[Speaker 1]: ...` 的轮次级格式。
- **TS**：每个时间戳 t 用两个整数表示（f mod 1000 与 ⌊f/1000⌋，f=⌊t/10ms⌋ 为帧号），起始+结束共 4 个 token/词。后处理先恢复单调性（把越界的时间戳夹到相邻时间戳之间），再转成文本标签（如 `hello [T:25] world [T:42]`）。作者指出用 4 个普通数字 token 而非一个大时间词表（如 LLM-ForcedAligner），可避免训练新输出头或让 LLM 赋予 token 非常规含义。

**训练细节：** 仅训练投影器与 LoRA，2.11B 参数中仅 205M 可训练；AdamW，仅在生成的 TS/SAA token 上计算交叉熵；32 张 H100 约 4 天。训练时用在线拼接生成长音频（插入随机静音、制造重叠），并对输入转写做随机词删除，以模拟 ASR 错误。

## 实验结果

**时间戳 (AAS ↓ms)：** 在 8 个英文 + 8 个多语种测试集上，本模型在**全部 16 个测试集上 AAS 最低**。相对 GSP，平均 AAS 在英文降低 **32%**、其他语言降低 **55%**；若使用相同的 GSP 输入转写，则分别降低 34% / 56%。模型对转写质量不敏感：用 GSP 文本或 Whisper 文本时结果与用 GT 时非常接近。对比外部系统 Qwen3-FA、CrisperWhisper、Canary-v2、WhisperX 均更优（英文 avg：本模型 25.8 vs Qwen3-FA 42.7 vs GSP 37.7）。

**说话人归属：** 在 Fisher、CallHome English、AMI-SDM 上，NAR 模型在**每个测试集的 cpWER 最优**。VibeVoice-ASR 平均 WDER 最低（Fisher 除外），但 WDER 不惩罚删除，cpWER 排序反转；且 VibeVoice RTFx 仅 19，比 GSP 还慢约 2.5 倍，因此「NAR 标注器 + 快 ASR」可在精度媲美 VibeVoice 的同时大幅提速。相比 pyannote 3.1 + GSP 的级联基线，NAR 在 WDER 上更优。

## 一句话评价

本文证明：把 GSP 的自回归标注任务拆成「非自回归占位符填充」，在共享架构与训练数据下即可同时获得**更准（SOTA 的时间戳精度、最优 cpWER）**与**快 1–2 个数量级**的转写标注，核心洞见是标注标签在给定转写与音频的条件下近似条件独立，天生适合 NAR 并行生成。

---

## 17. Interpreting hierarchical organisation of speaker embeddings

**作者**: Yanze Xu, Wenwu Wang, Mark D. Plumbley
**链接**: [2609.15203](https://arxiv.org/abs/2609.15203)
**分类**: Speaker Recognition | **关键词**: Explainable AI, Speaker Recognition, Speaker Embeddings, Hierarchical Clustering, Cluster–Class Matching

# 论文总结：Interpreting hierarchical organisation of speaker embeddings

## 核心痛点
- 说话人识别网络学习到的说话人嵌入内部机制不透明，现有可解释 AI（XAI）多解释网络关注什么、对什么敏感，很少解释表征的组织方式。
- 先前对说话人嵌入组织的研究采用降维或平聚类，只得到平坦、独立的簇，无法回答簇之间的层次关系。
- 在说话人日志中，层次聚类只作为中间结果，完整的层次组织结构未被可视化，更未被语义解释。
- CCM（Cluster–Class Matching）只给出一个整体匹配分数，不能为每个簇赋予具体语义；且未区分个体类别与合取类别。

## 方法创新
- 从 XAI 视角解释和诠释说话人嵌入的层次组织。
- 提取说话人嵌入（取识别网络倒数第二层输出），用 Single-Linkage Clustering (SLINK) 分析其是否自然形成具有层次关系的簇，并用树状图可视化。
- 用 CCM 评价层次组织的整体匹配性能（以 F-score 聚合最佳簇–类对）。
- 提出 Hierarchical Cluster–Class Matching (HCCM)：在层次簇与预定义语义类别之间迭代寻找一对一匹配，用匹配到的类别解释每个簇。
- 定义个体语义类别（如 male、UK）与合取语义类别（如 UK & male，通过索引集交集构造），从而可解释更多簇。
- 提出 L-score（Liebig 分数）：取精确率与召回率中的较小值，即 L(c,h)=|c∩h|/max(|c|,|h|)，使不完美匹配可诊断（受限来自精确率还是召回率）。

## 实验设置与结果
- 网络与数据：ResNetSE34L，以 angular prototypical loss 在 VoxCeleb2 开发集上训练；输入 VoxCeleb1 测试集的 4 秒话语（400×10 ms 频谱图帧）；取倒数第二层输出作为说话人嵌入。
- 语义类别：VoxCeleb1 测试集包含 40 个说话人身份、2 个性别、9 个国籍，共 51 个个体类别；由性别与国籍的非空两两交集构造 13 个合取类别；总计 64 个类别用于 CCM 与 HCCM。
- CCM 结果（表 1）：说话人身份 F=0.9754，性别 F=0.9997，国籍 F=0.7710，国籍&性别合取 F=0.8316，平均 F=0.8944，说明 SLINK 得到的层次组织整体匹配良好。
- HCCM 结果：树状图中不同位置的层次簇可分别用说话人身份、性别、国籍相关的语义类别解释，为嵌入的层次组织提供了语义洞察。

## 一句话评价
该工作将层次聚类与簇–类匹配引入 XAI，提出 HCCM 与 L-score，为说话人嵌入的层次组织提供可量化、可诊断的语义解释；但实验仅基于 VoxCeleb 与单一 ResNetSE34L 网络，结论的普适性仍待验证。

---

## 18. Learned Bow Control on a Measured Bowed-String Model: a Revised Minimum-Bow-Force Law, a Recurrent Controller, and the Domain of a Supervision Ceiling

**作者**: Homayoon Beigi, Grace Conneely
**链接**: [2609.14990](https://arxiv.org/abs/2609.14990)
**分类**: Physics-Based Audio Modeling and Neural Control | **关键词**: bowed-string instruments, Helmholtz motion, stick-slip friction, finite-difference time-domain, imitation learning, recurrent neural networks, neural network control

# 论文总结

**标题**：Learned Bow Control on a Measured Bowed-String Model: a Revised Minimum-Bow-Force Law, a Recurrent Controller, and the Domain of a Supervision Ceiling  
**作者/机构**：Homayoon Beigi, Grace Conneely；Columbia University Nonlinear Control Lab  
**报告编号**：Technical Report No. 20260913-01

## 核心痛点
- 弓弦接触是强非线性 stick-slip 过程，必须在有限差分网格中隐式求解接触力。若将摩擦力滞后一个时间步，由于点力作用在约 10^-6 kg 的集中质量上，弓点速度会被改变数 m/s，导致任意弓压下都无法形成黏滞相。
- 现有可演奏性图/开环参数图难以跨弦、跨弓速、跨弓桥距离泛化；学习型弓控制常以音色或黑箱模型为目标，缺少对 Helmholtz 运动本身的可测量诊断。
- 模仿学习存在监督上限：行为克隆通常不超过示范者，但该上限在什么域内成立很少被定量测量。
- 缺少显式 stick test 的 regime classifier 会把小振幅连续滑移误判为 Helmholtz；谐波性指标也可能把弓从未真正抓住的弦评为 Helmholtz。

## 方法创新
- 建立有限差分弓弦模型，采用隐式求解的 Stribeck 摩擦；摩擦特性、波阻抗和品质因数均取自已发表测量，而非拟合参数。
- 提出 stick fraction 作为诊断量，即窗口内弓携带弦的时间比例，并用于识别假 Helmholtz 运动。
- 在四根开放弦上重新检验 Schelleng 弓压上下限：最大弓压被复现，最小弓压被修正为 Z v_b β^{-1}，而非传统预测的 Z^2 v_b β^{-2}。
- 在匹配容量下比较六种控制器，包括前馈网络与门控循环网络；控制器命令弓根处法向力，这是机器人弓可实际施加的量，并与弓速协调以应对传输因子变化。
- 将控制器视为模仿学习器，教师是稳态逆问题的穷举查表规则；通过控制器得分对教师得分回归，测量监督上限的适用域。
- 在刚性指板停止条件下，被控对象可证明不变，因此跨音高迁移损失归因于控制器，并追溯到一个特征。

## 实验结果
- 四根开放弦在各自中频带弓压下均返回 Helmholtz 运动：stick fraction 为 89.1%，理想值为 90.0%；滑移频率与 flattening 预测误差在 0.83% 以内；滑移抖动达到机器精度。
- 单一工作点不可用：在 A 弦上选定的力，在 E 弦达到最大值的 99%，在 G 弦仅为 36%。
- Schelleng 最大弓压在所有弦上复现，四个指数跨度仅 0.05。最小弓压拟合为 Z v_b β^{-1}，将两个平方依赖降为一次方，分别偏离预测 8.9 和 8.7 个标准误，残差减半；阻抗依赖幅度为 +1.06±0.07，而预测为 +2。
- 六种控制器、四根弦、每根弦 20 个种子：门控循环网络整体优于前馈网络，尤其在中段扰动下；前馈网络只在模型可演奏性图判定为 Helmholtz 区域之外的起点完成更多 strokes。
- 最小门控变体失败：仅由输入计算门控无法清除 latched state。
- 训练损失既不能选择容量，也不能选择上下文长度；没有学习控制器超过生成标签的查表规则。控制器在教师失败处超过教师，在教师有效处受其约束，回归斜率为 0.32，低于 1 超过十个标准误。
- 无 stick test 的 regime classifier 会把小振幅周期滑移标为 Helmholtz；谐波性度量会把弓从未抓弦的情况评为高于 Helmholtz。

## 一句话评价
这是一项把物理测量、隐式接触求解、可演奏性边界修正与模仿学习上限测量紧密结合的弓弦控制研究，既给出了可复现的建模与诊断流程，也明确划定了数据驱动弓控制相对规则教师的适用边界。

---

## 19. Bridging Data, Reasoning, and Alignment: A Unified Framework for Context-Aware Instruction-Following TTS

**作者**: Jingbin Hu, Luyu Wang, Wenjie Tian, Kangxiang Xia, Qirui Zhan, Haoyu Zhang, Yunxiang Chen, Houdun Liu, Lei Xie, Liumeng Xue
**链接**: [2609.14740](https://arxiv.org/abs/2609.14740)
**分类**: Text-to-Speech | **关键词**: Context-Aware TTS, Instruction-Following TTS, Chain-of-Thought Reasoning, Direct Preference Optimization, Data Distillation

# 论文总结：Bridging Data, Reasoning, and Alignment: A Unified Framework for Context-Aware Instruction-Following TTS

## 核心痛点
- ISCSLP 2026 CoT-TTS Challenge 要求 TTS 系统在合成语音前，先从对话历史中生成 Chain-of-Thought（CoT）推理；而官方 baseline 存在上下文理解有限、指令保真度弱、音频质量欠佳等问题。
- 电影域原始数据约 16,000 小时，包含严重背景噪声、转写错误、CoT 与对话历史不一致、语义标注模糊等问题，损害语义理解和音频保真度。
- 多模态条件输入带来高生成方差，仅靠 SFT 的 token-level loss 难以区分“全局上下文合适”与“局部合理”的输出，无法保证 holistic “Context→CoT→Speech” 一致性。
- 缺乏公开的 context-specific benchmark 和细粒度指标，难以独立诊断 contextual reasoning（Context→Instruct）与 instruction execution（Instruct→TTS）中的失败。

## 方法创新
- 提出三阶段系统优化 pipeline：
  1. 基于清洗数据的 continued pre-training；
  2. distillation-based supervised fine-tuning；
  3. Context-Aware Direct Preference Optimization（CA-DPO）。
- 数据清洗与治理：使用 FullSubNet 去噪、Qwen3-ASR 重转写、Qwen3.5-35B-A3B 进行 history-CoT 一致性分析，过滤语义矛盾或逻辑不连贯样本；continued pre-training 阶段全参数微调优于 LoRA。
- 蒸馏数据构造：以 Qwen3-TTS Voice Design 为 teacher，根据目标文本和来自对话上下文的风格指令合成 545K 语音样本；再通过 Seed-VC 将音色转换到目标说话人，同时保留风格信息。
- 多模型质量过滤：Qwen3-ASR 过滤 WER≥1% 样本；WavLM-based speaker verification 保证说话人一致性；UTMOS-v2 评估感知质量；Qwen3-Omni 评估 style-content alignment。SFT 阶段 LoRA 优于 full-parameter，可平衡合成蒸馏数据与真实数据。
- CA-DPO：通过 multi-candidate rollout sampling 和 cascaded filtering 获得高置信 preference pairs，包括 ASR prescreening、Gemini 3.1 tournament-based ranking（评估 Context-CoT-Speech 一致性）、speaker similarity verification；用 DPO 加 SFT anchor loss 训练，提升上下文推理准确率、输出可懂度和说话人一致性。
- 评估体系：建立中英双语 500-sample test set，以及 LLM-as-Judge 框架，独立评估 Context-to-Instruct（C2I）推理质量、Instruct-to-TTS（I2T）执行保真度和端到端一致性，并辅以 WER、SIM、UTMOS 等传统客观指标。

## 实验结果
- 论文摘要与引言指出：在 ISCSLP 2026 CoT-TTS Challenge Track 1 官方 baseline 上，所提系统在所有客观指标、LLM-as-Judge 分数和主观 MOS 上均显著优于 baseline。
- 结果验证了系统性数据治理与偏好对齐对 context-sensitive speech synthesis 的有效性；但所给片段未包含完整实验数值和消融细节，内容在方法部分后被截断。

## 一句话评价
该工作围绕 CoT-TTS 任务提出从数据清洗、蒸馏 SFT 到 CA-DPO 偏好对齐的完整优化框架，并通过双语 500 样本 LLM-as-Judge 评测证明系统性数据治理与偏好优化能显著提升 Context→CoT→Speech 的一致性和语音质量。

---

## 20. Parameter isolation with domain-specific experts for incremental audio classification

**作者**: Jongyeon Park, Do-Hyeon Lim, Sang-won Park, Hong Kook Kim, Kyungdeuk Ko, Hyeongcheol Geum, Jeong Eun Lim
**链接**: [2609.14730](https://arxiv.org/abs/2609.14730)
**分类**: Audio Classification / Domain-Incremental Learning | **关键词**: Domain-Incremental Learning, Audio Classification, Parameter Isolation, Data-Free Generative Replay, Cross-Domain Feature Generation, Prototype Classifier

# 论文总结：Parameter Isolation with Domain-Specific Experts for Incremental Audio Classification

## 1. 基本信息
- 标题：Parameter Isolation with Domain-Specific Experts for Incremental Audio Classification
- 会议/挑战：DCASE 2026（Detection and Classification of Acoustic Scenes and Events 2026），DCASE 2026 Challenge Task 7
- 作者/机构：Jongyeon Park、Do-Hyeon Lim、Sang-won Park、Hong Kook Kim 等（GIST）；Kyungdeuk Ko、Hyeongcheol Geum、Jeong Eun Lim 等（Hanwha Vision）
- 任务：domain-incremental learning（DIL）/ domain-agnostic incremental audio classification

## 2. 核心痛点
- 真实音频部署环境存在 domain shift，模型需要持续适应新域，同时不能访问旧域原始数据。
- 现有 DIL 方法分为三类：正则化、回放、参数隔离。
- 正则化方法（如 EWC）通过惩罚项间接保护旧知识，稳定-可塑性平衡难以调优，长域序列中重要性估计会越来越不可靠。
- 回放方法保留样本或生成样本，但样本缓冲区会随域数量增长；生成回放也可能需要额外条件或旧数据。
- 参数隔离方法直接冻结旧域参数，能避免遗忘，但已有 Audio DIL 使用 domain-shared backbone，仅第一域学习后冻结，后续域受限于初始特征集，域间差异大时性能下降。
- 在严格 DIL 下，旧域原始音频不可用，且新加入的 expert 对旧域样本没有输出，导致共享分类器输入不完整。

## 3. 方法创新：FoIL（Full-order Incremental Learning）
### 3.1 核心思想
- 将 DIL 重新解释为跨域递归更新过程：第 t 个域模型 Mt 由之前所有模型 {M1,...,Mt-1} 条件化得到，即 Mt = F(M1,...,Mt-1)。
- 区别于 first-order（只用 Mt-1）和 anchored（只锚定 M1），FoIL 使用 full-order 历史，保留所有旧域知识。
- 为每个域分配专用 expert，新 expert 追加而非替换；旧 expert 冻结，因此已学域不会退化。

### 3.2 网络与更新
- 输入音频分帧，提取 log-mel 特征。
- 每个 expert Ei 输出 embedding φi，拼接为 z，送入分类器。
- 更新函数 F(X,Y) 实现为拼接 expert 输出向量。Mi 使用 zi(Di)=[zi-1(Di), φi(Di)] 更新，z0(Di)=∅。
- Expert 基本架构为 CNN14。对于 i>=2，Ei 需要同时建模“从旧域投影的信息”和“当前域新信息”。
- E2 包含 CRNN：一部分由 E1 的 CNN14 微调，另一部分在 D2 上从头训练。E3 由两个 CNN14 分别处理投影信息和新信息。
- 分类器使用可学习 prototype，交叉熵优化，并用余弦相似度 prototype classifier Gi。

### 3.3 实现严格 DIL 的两个关键组件
- Data-free generative replay：在不能存储旧域原始音频时，利用冻结 expert 重建旧域数据（基于 DeepInversion 思路）。
- Cross-domain feature generation：合成缺失的 expert 特征，使分类器始终获得完整输入，并让新 expert 从旧 expert 特征中得到更丰富表示。

## 4. 实验与结果
- 在 DCASE 2026 Challenge Task 7（domain-agnostic incremental learning for audio classification）上评估。
- 结果：micro accuracy 78.4%，macro accuracy 78.9%。
- 相比 Challenge baseline：分别提升 33 和 25 个百分点。
- 论文称该结果在所有提交中达到最佳。
- 进行了消融实验，分析 data-free generative replay 与 cross-domain feature generation 等组件对分类精度的贡献。

## 5. 一句话评价
FoIL 通过“每域一个专用 expert + 全历史递归更新 + 无数据生成回放 + 跨域特征生成”，在严格 DIL 设定下同时缓解灾难性遗忘并补全分类器输入，在 DCASE 2026 Task 7 上大幅超越基线，是参数隔离式增量音频分类的有力方案。

---

## 21. Exploring Multimodal Turn-Taking Cues in Face-to-Face Conversation using Voice Activity Projection

**作者**: Willem Berner, Julio Cesar Cavalcanti, Kalle Åström, Gabriel Skantze
**链接**: [2609.14666](https://arxiv.org/abs/2609.14666)
**分类**: Multimodal Turn-taking Prediction | **关键词**: Voice Activity Projection, Turn-taking Prediction, Multimodal Fusion, Facial Action Units, Face-to-Face Conversation

# 论文总结：Exploring Multimodal Turn-Taking Cues in Face-to-Face Conversation using Voice Activity Projection

## 核心痛点
- 轮流发言（turn-taking）是口语交互的基础，人类自然依赖语言与非语言线索，但现有对话系统多只依赖音频或静音阈值，容易造成打断或响应迟缓。
- Voice Activity Projection（VAP）虽已用自监督 Transformer 在原始音频上预测未来语音活动并优于静音阈值，但仍是纯音频模型。
- 先前多模态 VAP 研究多基于小规模数据或视频会议场景；视频会议中的轮换更短更频繁、注视估计模糊，结论不一定能泛化到面对面共处对话。
- 因此需要在大规模面对面数据上回答：视觉线索能否超越音频基线？哪些视觉特征组最重要？模型在即兴表演与自然互动子集间如何变化？

## 方法创新
- 在 VAP 音频自监督框架上扩展视觉模态，使用 Meta Seamless Interaction 数据集，约 400 小时双人面对面对话；训练 328h、验证 41h、测试 41h，各划分中 improvised/naturalistic 分布平衡。
- 视觉特征共 182 维，30Hz 提取后线性插值至 50Hz，包含：
  - Gaze：每帧注视方向 pitch/yaw；
  - Head：头部 pitch/yaw/roll；
  - Body & hand：SMPL-H 21 个身体关节 + ViTPose 15 个手部关节；
  - FAU：24 个面部动作单元强度，排除注视相关单元；
  - 消融子集：All、Body、Gaze、FAU。
- 融合方案逐步设计：
  - M1 拼接：视觉 182 维与音频 256 维拼接后投影回 256；
  - M2 交叉注意力：视觉先投影并自注意力，再以音频条件化视觉，最后用音频条件化视觉更新音频；
  - M3/M4 Delta 特征：加入相对短时均值的偏差，N=3 或 N=10，维度翻倍后映射回 256；
  - M5/M6 可训练门控：早门控在视觉自注意力前，晚门控在交叉注意力前，门控初始化为 0.5。
- 评估除 VAP loss 外，还使用 Hold/Shift、Short/Long、Shift Prediction 等可解释轮流发言任务。

## 实验结果
- 视觉信息整体优于仅音频基线。
- FAU 显著比其他视觉特征组更有信息量。
- Body 与 Gaze 特征提供互补信息，所有特征组合的模型性能最佳。
- 在 improvised（演员即兴角色扮演）与 naturalistic（非演员提示互动）训练/测试设置下，具体任务性能存在差异，说明数据来源会影响轮流发言预测表现。

## 一句话评价
该工作在大规模面对面对话数据上系统验证了多模态 VAP 的视觉增益，确认 FAU 是核心预测特征、身体与注视信息具有互补价值，为更自然的轮流发言预测提供了可扩展的融合框架与数据洞察。

---

## 22. Modeling, Scaling, and Decoding: Optimizing Controllable Speech Generation with Nonverbal Vocalizations

**作者**: Ziyu Zhang, Yun Chen, Taihui Wang, Hanzhao Li, Qicong Xie, Rilin Chen, Zhixian Zhao, Lei Xie
**链接**: [2609.14231](https://arxiv.org/abs/2609.14231)
**分类**: Text-to-Speech | **关键词**: Nonverbal Vocalizations, Controllable Speech Synthesis, Diffusion Autoregressive Models, Data Augmentation, Best-of-N Sampling, Long-tail Learning

# 论文总结：Modeling, Scaling, and Decoding: Optimizing Controllable Speech Generation with Nonverbal Vocalizations

## 核心痛点

- **非语言发声（Nonverbal Vocalizations, NVVs，如笑声、叹息、呼吸、清嗓、喘息等）的可控合成**对自然、富有表现力的语音至关重要，但现有 TTS 系统主要以流畅的词汇内容为优化目标，NVVs 常在数据清洗中被过滤掉。
- 现有零样本 TTS（基于 codec language modeling 或 diffusion/flow matching）虽在自然度与音色相似度上大幅提升，仍**无法可靠地在指定位置放入指定 NVV 并给出可信的声学实现**。
- ISCSLP 2026 NVVSpeech Challenge Track 2 设立基准，但**缺乏官方训练集**，且每类 NVV 内部声学变化极大、数据分布高度不均衡（cry、snore、sneeze、yawn、burp 等类别覆盖极少），需要细粒度建模与数据构造。

## 方法创新

### 1. NVV-aware DiTAR 建模
- 基于自研 **1.5B 参数 DiTAR** 骨干：将连续 VAE latent 分组为 acoustic patch，因果语言模型为 LocDiT 提供 patch 级条件，自回归生成下一段连续语音 patch；相比量化 codec token 方法更能保留 NVV 的细粒度声学细节。
- **NVV 专用 token 条件化**：将 16 个 NVV 标签（如 [laugh]）注册为文本词表中的专用特殊 token，每个标签映射到唯一 token id 与可学习 embedding，而非切分为多个 subword；NVV token 与普通文本 token 共享 embedding 空间与自注意力参数，无需独立 NVV 编码器或显式事件位置输入。
- **NVV-aware stop prediction**：保留标量量化瓶颈与二分类线性头，但仅将最后一个有效 patch 监督为 stop，所有中间 patch（含 NVV patch）标为 continue；配合固定正类权重、label smoothing 和不 detach 的 LM hidden state，使 stop loss 塑造语义表示，从而区分句内插曲式 NVV 与真正的句尾边界。

### 2. 双语预训练 + 长尾感知 SFT
- 在大规模双语语音语料上预训练，NV 部分包含 NVSpeech-170K、NonVerbalSpeech-38K 等公开英/汉语资源，全部注释归一到 16 类。
- 针对长尾类别，使用表达力强的商业 TTS 合成英/汉语数据，将 NVV 标签置于句首/句中/句尾，配合多样短上下文与多说话人以减少位置与词汇偏差。
- 采用 **tag-frequency-aware resampling** 构造 continued-SFT 混合数据，重复因子 r_i = clip(sqrt(f_max/f_i)·b_i, 1, r_max)，并对英语样本上采样以达成目标英汉比例；同时限制单说话人贡献、语句重复次数并过滤过长样本，依据局部客观指标而非训练损失选择 checkpoint。

### 3. 推理时优化
- **解码配置搜索**：评估 LM-guidance scale w 与 noise-injection scale τ 的 4 组组合，用局部 intelligibility、NVV-detection、audio-quality 指标在验证集上排序，仅用 12 份官方提交反馈确认排序可迁移（粗粒度搜索，过拟合风险有限）。
- **Best-of-N 采样**：同一配置下对每条带标签文本生成 N=5 个候选，用多指标加权选择 C_i = 0.40L_i + 0.30D_i + 0.20R_i + 0.10Q_i（L 为局部 LALM 聚合分，D 为 NVV 检测器分，R 为 ASR 词法保真分，Q 为 DNSMOS 分），仅用局部自动评测，不使用官方测试反馈。

## 实验结果

训练设置：100k 小时双语语音预训练，Adam，lr 5e-5，32×NVIDIA H20，单卡 batch 4，全局 batch 128，patch size P=10。评测：Paraformer-zh（汉语 CER）、Whisper-large-v3（英语 WER）、BEATs NVV 检测器（P/R/CA-F1/NTD）、DNSMOS 及局部 LALM judge。

| 系统 | CER↓ | WER↓ | DNS↑ | P↑ | R↑ | F1↑ | NTD↓ |
|---|---|---|---|---|---|---|---|
| Official baseline | 6.267 | 3.159 | 3.026 | 0.769 | 0.251 | 0.569 | 0.073 |
| NVV-aware DiTAR | 5.603 | 2.949 | 3.126 | 0.816 | 0.263 | 0.570 | 0.071 |
| + Long-tail SFT | 5.211 | 2.711 | 3.172 | 0.878 | 0.275 | 0.574 | 0.069 |
| + Decoding search | 5.098 | 2.597 | 3.183 | 0.863 | 0.265 | 0.582 | 0.068 |
| + BoN (final) | 5.012 | 2.194 | 3.221 | 0.870 | 0.271 | 0.589 | 0.069 |

- **最终系统官方加权双语得分 62.786**：Track 2 中普通话第一、英语第二、总成绩第一。
- 消融显示：定向合成增强对严重欠代表的 NVV 类别收益最大；稳健的候选选择需在 NVV 正确性、词法保真度与感知质量之间平衡，而非只优化单一指标。

## 一句话评价

该工作以「NVV-aware 建模 + 长尾数据配方 + 推理时两阶段解码优化」三条线系统性地解决了可控非语言发声合成中的数据稀缺、类别不均衡与生成不稳定问题，并在 ISCSLP 2026 NVVSpeech Challenge Track 2 中以 62.786 的加权双语得分取得总榜第一，是一份工程完整、实验扎实的竞赛级技术报告。

---

## 23. HARP: Agentic Hybrid Retrieval and Analysis for Long-Form Audio

**作者**: Chin-Jou Li, Masao Someki, Woojeong Jin, Yashish M. Siriwardena, Tanmay Laud, Shanil Puri, Shinji Watanabe
**链接**: [2609.14116](https://arxiv.org/abs/2609.14116)
**分类**: Audio Retrieval | **关键词**: Long-form audio, Audio retrieval, Agentic audio systems, Retrieval-augmented generation, Large audio-language models, Benchmark, Hybrid retrieval, Multimodal evidence

# HARP: Agentic Hybrid Retrieval and Analysis for Long-Form Audio

## 核心痛点
- 长音频分析需要定位并整合分布在长录音中的证据。
- 现有工作主要通过结构化文本表示检索语义内容，但许多现实查询依赖声学证据（如情感、音乐特征），这些在连续表示或原始音频中保存更好。
- 不同检索策略和证据模态在可解释性、信息保留和检索效率之间存在权衡，但尚不清楚哪种组合最适合长音频分析。
- 现有基准多关注对话语义，声学信息有限，且通常只评估答案准确率。

## 方法创新
- 提出 HARP（Hybrid Audio Retrieval Pipeline），一个轻量级 agentic 框架，分离规划、检索和答案生成。
- 支持独立变化：(i) 检索策略：关键词、向量或混合搜索；(ii) 证据模态：文本元数据、音频片段或两者。
- 离线提取：将长音频分段，构建结构化元数据（时间戳、ASR 转录、领域标签、通用和领域特定嵌入）。
- 推理流程：agent 生成检索计划，指定时间窗口和工具调用；工具包括关键词匹配和向量搜索；候选合并排序后取 top-K；按需加载音频片段；生成答案和理由。
- 构建基准，涵盖三个领域：情感理解（MSP-Podcast/MSP-Conversation）、临床症状分析（MedMosaic）、歌曲美学评估（SongEval）。
- 评估指标包括检索质量（hit rate）和答案/理由准确性，分别评估答案正确性和理由质量。

## 实验结果
- 混合检索（关键词+向量）表现最稳健。
- 当结合元数据和检索音频作为证据时，平均答案准确率比单模态检索和证据提升约 10%，理由准确率提升约 6%。
- 仅答案准确率会高估系统能力。
- HARP 在查询类型上大致遵循人类表现趋势；检索系统擅长穷举定位，但人类在整合复杂证据方面仍更强。
- 不同任务受益于不同的检索和证据形式，但 HARP 在混合检索和多模态证据下各阶段表现一致良好。

## 一句话评价
HARP 通过系统性地解耦检索策略与证据模态，为长音频分析提供了灵活且可扩展的 agentic 框架与基准，强调了混合检索和多模态证据的重要性，并倡导超越答案准确率的评估。

---

## 24. DualSpecSE: A Dual-Path Speech Enhancement Network Integrating Mel and Complex Spectrograms

**作者**: Xingchen Li, Ziqian Wang, Zikai Liu, Yike Zhu, Zihan Zhang, Longshuai Xiao, Lei Xie
**链接**: [2609.13911](https://arxiv.org/abs/2609.13911)
**分类**: Speech Enhancement | **关键词**: Dual-path speech enhancement, Mel-spectrogram, Complex spectrogram, Interaction module, ASR front-end

# DualSpecSE 论文总结

## 核心痛点
- 现有语音增强多在时频域或时域直接映射，或采用两阶段 ERB/Mel 增益估计再滤波；低维 ERB/Mel 增益限制频谱分辨率。
- 以 Mel 频谱为预测目标的方法利于 ASR，但通常需要额外预训练声码器重建波形，带来级联误差、幅度/相位细节损失和计算开销。
- 复杂频谱分支可高保真重建，但直接学习细粒度复数谱较难，且与 Mel 表示存在尺度鸿沟。

## 方法创新
- 提出 DualSpecSE 双路径框架，共享编码器，并行运行 Mel 分支与复数谱分支。
- Mel 分支：Mel filterbank 将线性频域特征变换到 Mel 域，经若干 cross-band/narrow-band 块增强，直接输出增强 Mel 频谱，可送入 ASR。
- 复数谱分支：同样堆叠 cross-band/narrow-band 块，学习细粒度复数谱细节，无需外部声码器。
- 交互模块 Interaction Module：将 Mel 分支中间特征线性投影对齐到复数分支维度，经时序分组卷积 T-GConv、LayerNorm、PReLU，再经频率分组卷积 F-GConv、LayerNorm、Sigmoid 预测交互 mask，按 h_out = h_complex + h_mel ⊙ M 注入 Mel 幅度线索，降低复数分支学习难度。
- 融合模块 Fusion Module：用 Mel filterbank 的伪逆 W+ 将增强 Mel 近似回幅度谱，再用轻量 ConvNeXtV2 学习残差得到粗幅度估计，结合带噪相位重建复数谱，并与复数分支输出逐元素相加做残差精修。
- 骨干修改自 CleanMel 的 cross-band 与 narrow-band 块；narrow-band 中用 GroupMamba 替换原 Mamba，将特征维度分组并行处理以降低计算量。
- 损失函数：Mel 分支用 log-Mel L1 与幅度 MSE；复数分支用 log-Mel L1、幅度 MSE 及实部/虚部复数谱 MSE；总损失为加权和。

## 实验结果
- 训练数据：387 小时干净语音（DNS3、EARS、Emilia，按 DNSMOS 筛选）与 376 小时噪声（DNS3、ESC、FSD），RIR 来自 SLR26/SLR28；训练/验证 9:1。
- 评估：在 Interspeech 2020 DNS Challenge 测试集评估增强质量；在 CHiME-4 模拟测试集用 ESPnet 预训练 ASR 评估 WER。
- 指标：WB-PESQ、NB-PESQ、ESTOI、DNSMOS（SIG/BAK/OVRL）及 WER。
- 结果：摘要与引言报告，与单分支模型相比，DualSpecSE 在语音保真度、感知质量和 ASR 性能上取得一致提升；增强 Mel 可直接用于 ASR，复数分支提升重建质量。由于提供片段截断，具体数值未列出。

## 一句话评价
DualSpecSE 通过 Mel 与复数谱双路径联合建模、交互引导与伪逆融合，在不依赖预训练声码器的情况下兼顾 ASR 友好表示和高保真语音重建，是一次面向增强-识别联合优化的有效架构探索。

---

## 25. Subphonetic Acoustic Modeling via Optimal Transport for Pronunciation Assessment

**作者**: Haopeng Geng, Jiun-Ting Li, Daisuke Saito, Nobuaki Minematsu
**链接**: [2609.13694](https://arxiv.org/abs/2609.13694)
**分类**: Pronunciation Assessment | **关键词**: Pronunciation Assessment, Optimal Transport, Subphonetic Modeling, Phone Segmentation, Forced Alignment, Mispronunciation Detection

## 核心痛点
发音评估（Pronunciation Assessment, PA）需要时间精确、具有诊断意义且忠实反映学习者实际发音的声学证据。然而，现有声学模型难以同时提供可靠的识别证据和分割证据：
- **CTC 音素识别器**：可灵活预测音素序列，但后验稀疏、峰化、以 blank 为主，常常错过音素边界和细粒度发音线索，且 subphonetic 线索被 CTC 准则 largely neglected。
- **文本依赖强制对齐器**：在给定转写时能提供可靠时间信息，但不适用于无参考的发音分析。
- 这形成了 **识别–分割权衡（recognition–segmentation trade-off）**。

## 方法创新
论文提出一种 **topology-aware frame-wise acoustic model**，用于学习每个音素内部密集、有序的状态后验，核心是 **有序子音素状态（ordered subphonetic states）+ 最优时间传输分类（OTTC）** 的组合：
- 将每个音素扩展为多个有序子音素状态，引入 HMM 风格的音素内部拓扑，例如 `S1T1` 表示标准单状态 CTC，`S3T2⋆⋆` 表示三状态、最小二状态遍历。
- 使用 **OTTC** 将对齐建模为一维质量传输问题，把帧级源质量传输到扩展后的拓扑状态序列，优化密集单调传输计划，鼓励所有有序状态接收帧级声学证据，而非仅产生孤立识别峰值。
- **拓扑感知解码**：推理时将拓扑作为有限状态解码约束；在 TDFA 中使用参考单音素序列扩展为拓扑约束图并搜索最佳路径；在 TI 设置中无参考图，在拓扑约束下解码，并仅将有效路径折叠回音素标签与边界。
- 该方法在保留较强音素识别能力的同时，提供密集、单调、帧级的子音素状态判别证据，从而支持 GOP、MDD 和 APA 等下游任务。

## 实验结果
- 训练仅使用 **LibriSpeech**，评估覆盖 **TIMIT、Buckeye、L2-ARCTIC、speechocean762 (SO762)**，涵盖朗读语音、自发语音和 L2 语音。
- 在文本依赖强制对齐（TDFA）和文本无关（TI）分割/识别设置下评估。
- 结果显示：相比神经基线，在朗读、自发和 L2 语音上改善了分割性能，同时保持有竞争力的识别性能。
- 下游评估显示在 **误发音检测（MDD）** 和 **自动发音评估（APA）** 上均有增益。
- 探测分析表明，学习到的拓扑状态捕获的是音素依赖的声学结构，而不是任意的帧级分布。
- 对比基线包括 Kaldi TDNN-F、ZIPA、Charsiu 等；表中报告了 TSE、R-value、PER、MDD F1 等指标，所提模型在分割与时序定位方面表现更优。

## 一句话评价
该工作将 HMM 式有序子音素拓扑与 OTTC 的密集单调传输相结合，有效缓解了 CTC 稀疏后验与强制对齐文本依赖之间的冲突，为发音评估提供了更精细、更可靠的帧级声学证据。

---

## 26. Building a Production Greek-English Speech Recognizer

**作者**: Christos Petrocheilos, Cleopatra Papadopoulou, Chris Porikis, Ioakeim Perros, Ayoub Kirouane, Themistoklis Nikolis
**链接**: [2609.13498](https://arxiv.org/abs/2609.13498)
**分类**: Speech Recognition | **关键词**: Bilingual ASR, Greek-English Speech Recognition, Production Machine Learning, Model Ensembling, ROVER, Language Identification, Data Quality Calibration

## 核心痛点
- 商业 ASR 对高资源语言已接近工程可解，但对希腊语（约 1100 万使用者）与英语在单句内不可预测混用、且多来自电话线路和拥挤会议室的场景，仍非常困难。
- 论文将“生产就绪”定义为同时通过九个门限：四个希腊语 WER 上限（干净朗读、非正式对话、商务会议、噪声环境）、三个英语 WER 上限（商务会议、噪声环境、社区来源语音）、语言识别（LID）准确率不低于 95%、非语音音频零幻觉文本（在 1500 条静音/噪声片段上测量）。
- 核心负面发现：在 1.7B 参数双语模型的前七个版本中，没有任何单一训练数据组合能同时满足九个门限；论文认为这不是数据量问题，而是固定容量下希腊语与英语竞争容量的权衡。

## 方法创新
- 系统名为 Sophea，是 Kiefer 的生产 ASR 服务，支持希腊语和英语噪声环境音频、商务会议以及句中语言切换。三个产品消费该系统：Sophea Meet（会议摘要）、Sophea robot voice harness（机器人噪声环境语音）、Sophea Nous（聊天产品中的语音转文字）。
- 模型谱系：一支基于 Whisper 架构（大型和 turbo 生产层级），另一支基于 Qwen audio-language model 传统适配双语转写；集成中还使用 NVIDIA Canary 的希腊语适配微调模型。
- 六阶段数据质量管线：音频质量分、词/分钟合理性过滤、转写置信度过滤、多独立教师转写交叉校验等。关键创新是“锚点校准”：用域内锚点重新校准 UTMOS 音频质量过滤器，而非使用教科书阈值。
- 预注册消融实验将幻觉 bug 定位到一个训练数据包。
- 集成方法：三模型 confusion-network（ROVER）词投票集成；另一套系统使用学习到的逐片段仲裁器（learned per-clip arbiter）在两个模型间选择。
- 服务架构：不强行用单模型满足所有门限，而是用路由层按预期语言和领域将通话/会议路由到专用 checkpoint，在希腊语为主的领域使用强制语言解码，其他场景回退到隐式 LID。

## 实验结果
- 希腊语噪声环境门限（WER ≤ 25.25）需要约 ≥1500 步密集噪声环境暴露；英语 LID 门限（≥95）在基线混合下最多容忍约 ≤250 步，在重新平衡混合下最多约 ≤1250 步，但代价是希腊语准确率停滞在约 26，距其门限差约 0.75 WER 点。两个步数预算相差近 6 倍，联合可行点位于测量前沿之外约 1 个 WER 点。
- 数据保护实验：加入 835 小时干净工作室级英语无法保护英语门限；加入 577 小时噪声、重叠、会议风格英语（约三分之一音频量）能在相同训练步数下保持准确率。结论是只有与干扰来源共享“声学邻域”的数据才能保护门限。
- UTMOS 锚点校准效果：按教科书阈值 3.0 会丢弃 98.7% 的希腊语训练音频；按域内锚点校准到阈值 1.30 后，丢弃比例降至 10.6%。
- 三模型 ROVER 集成将门限覆盖从单模型的 4–7/9 提升到 9/9，并将重叠语音 WER 从 53.35% 降至 37.87%（相对降低 29%）。
- 另一套不同组合系统（两模型上的学习型逐片段仲裁器）以 sophea/asr-k1 (preview) 列在公开 Open ASR Leaderboard 上，在榜单八个公开英语集上平均 WER 4.26%，截至 2026 年 9 月 11 日在默认视图中排名第 11；在实时希腊语噪声环境流量上达到 25.88%，是首个低于 26% 门限的单服务模型。
- 论文报告五个内部测量工具先给出看似合理但错误数字、后被第二工具抓出的案例；以及七项被测量但未上线的重大训练和架构工作。
- 限制：多数轨迹为单次训练运行，无重复随机种子，未量化 run-to-run 方差；不发布模型权重或训练数据，只报告方法和定量结果。

## 一句话评价
这是一篇罕见的、以负面结果和工程权衡为核心的生产级双语 ASR 复盘：它用九个生产门限和约 23 次训练迭代证明，小模型在固定容量下难以同时满足希腊语噪声环境 WER 与英语 LID，而真正的出路是数据声学邻域校准、路由服务和 ROVER 集成，而非继续寻找单一完美训练配方。

---

## 27. Typhoon ASR Streaming: Steerable Low-Latency Thai Speech Recognition with Real-Time Shallow Fusion

**作者**: Warit Sirichotedumrong, Tanawin Samutsin, Shah Faisal Wani, Sittipong Sripaisarnmongkol, Kunat Pipatanakul
**链接**: [2609.14991](https://arxiv.org/abs/2609.14991)
**分类**: Speech Recognition | **关键词**: Thai ASR, Streaming Speech Recognition, Cache-aware Transducer, Shallow Fusion, Contextual Biasing, n-gram Language Model, Phrase Boosting

## 论文信息
- 标题：Typhoon ASR Streaming: Steerable Low-Latency Thai Speech Recognition with Real-Time Shallow Fusion
- 作者/机构：Warit Sirichotedumrong 等，Typhoon Team, SCB DataX, Bangkok, Thailand
- 领域：泰语流式语音识别、解码时可操控、实时浅融合

## 核心痛点
1. 开源泰语 ASR 以离线 Whisper 类模型为主，需要完整语音后才能转写，无法满足实时字幕、语音助手、会议转写等低延迟场景。
2. 之前发布的 Typhoon ASR Real-time 虽是 FastConformer-Transducer，计算成本约为 Whisper Large-v3 的 1/45，但采用全上下文双向训练，强行流式时 CER 从 11.0% 升到 62.8%，极低延迟下甚至不再输出有效文本。
3. 泰语没有词间空格，同一发音存在多种书写形式（数字、mai yamok 重复符、借词等），且实时系统需要控制专名和领域词，但逐客户重训练不现实。
4. 开源泰语 ASR 生态缺少解码时 n-gram LM/短语偏置的实现、训练配方和系统研究。

## 方法创新
- 提出模型无关的可操控泰语流式 ASR 框架：cache-aware 识别 + 解码时 n-gram 融合 + 短语 boosting，并给出将全上下文 Typhoon ASR Real-time 转为 cache-aware 流式模型的配方。
- 两个流式模型：
  1. typhoon-asr-streaming-115m：从 Typhoon ASR Real-time 全上下文 checkpoint 转换，替换为因果卷积和 chunked limited-context attention，复制权重做 warm start，再在约 11k 小时泰语语料上短时微调。
  2. typhoon-asr-streaming-nemotron-0.6b：将 NVIDIA Nemotron 流式 ASR 适配到泰语；其多语言 tokenizer 无泰语子词，因此扩展加入 Typhoon ASR Real-time 的多字符泰语 BPE，而非替换，以保留其他语言；并增加数字规范化微调阶段。
- 实时浅融合：在每个解码步对候选 token 重排序，score(y)=log p_AM(y|x)+Σ_i α_i log p_LM,i(y)+β·boost(y)。使用 n=4 的 GPU n-gram LM 和用户词表构建的 phrase boosting tree。融合只重排模型已经提出的候选，不改变声学候选生成。
- 泰语文本规范化沿用 Typhoon ASR Real-time 技术报告的规则。

## 实验与结果
- 数据：训练语料约 10,999.1 小时、9,971,887 条，主要来自 GigaSpeech2 10,329.5 小时，另有 curated media、Common Voice 17、合成 TTS。
- 测试：TVSpeech（570 条，经济/政治，含人名、数字、英文 code-switching）和 GigaSpeech2-Thai（1000 条 YouTube 通用语音）。指标：CER、TVSpeech 英文 code-switch 关键词召回、RTF、首 token 延迟。look-ahead 从 80 ms 扫到 3200 ms。
- 全上下文模型无法流式：CER 从离线 11.0% 退化到 1040 ms 的 62.8%，80 ms 时 100%。两个流式模型在全部延迟下可用，0.6B 在每个延迟领先，1040 ms 达 14.1% CER，相比流式基线降低约 4.5×；通用语音同样为 9.3% vs 39.8% @1040 ms。
- 解码时 steering 将 TVSpeech held-out 测试（285 条，1040 ms）关键词召回从 16.6% 提到 20.7%，CER 基本不变（14.4 → 14.1 或 14.6）；general n-gram 单独已达 20.2%，keyword-synth n-gram 20.4%，phrase boost 20.7%；上限 27.8%。
- 效率：1040 ms 下 batch-1 RTF 0.020（115M）/0.024（0.6B），加融合不变；batch-16 RTF 0.0023/0.0031；首 token @1040 ms 约 1.06/1.07 s，@480 ms 约 0.49 s。融合带来的 RTF 变化小于 3%。
- 关键发现：普通 ASR 训练转录本上训练的 general n-gram 已能恢复高频 code-switched 术语，因为它把模型听到但拼写不一致的词（如 eco system vs ecosystem）校准到规范写法；keyword synthesis 和 phrase boosting 主要对稀有领域词有价值。

## 一句话评价
论文把成熟的 cache-aware 流式 Transducer、GPU n-gram 浅融合和短语偏置工程化打包到泰语 ASR，系统性地证明全上下文泰语模型流式会崩溃，而 cache-aware 转换/适配可恢复低延迟识别，且无需重训练即可用 n-gram/短语 boosting 在解码时 steering 词汇，在准确率几乎不降、RTF 几乎不增的前提下显著提升 code-switch 关键词召回。

---

## 28. CAL-MOS: Bridging Layers with Adapters for Robust MOS Prediction Across Speech Foundation Models

**作者**: Alef Iury Siqueira Ferreira, Pedro Lustosa Rege Botelho, Fernanda Silva, Daniel Casanova, Rafael Faustino, Frederico Oliveira, Arlindo Galvão Filho, Anderson da Silva Soares
**链接**: [2609.14956](https://arxiv.org/abs/2609.14956)
**分类**: Speech Quality Assessment | **关键词**: MOS Prediction, Speech Foundation Models, Layer-wise Analysis, Adapters, Cross-layer Aggregation

## 核心痛点
- 语音质量评估（SQA）对现代语音技术至关重要，但主观 MOS 听测昂贵、耗时、难扩展，且受标注者偏差影响，因此自动非侵入式 MOS 预测成为实用替代方案。
- 近年非侵入式 MOS 预测越来越依赖语音基础模型（Speech Foundation Models, SFMs）。然而 SFM 暴露多层表示，究竟哪些深度对 MOS 预测最有信息量，以及如何跨不同骨干与数据集可靠融合多层信息，仍不清楚。
- 全量微调性能强但计算成本高；朴素跨层加权融合可能在不同骨干和数据集上不稳定。

## 方法创新
- 论文在统一协议下基准测试 10 个 SFM：wav2vec 2.0 Large、XLS-R 300M/1B、MMS 300M/1B、Wav2BERT 2.0、WavLM Large、HuBERT Large、data2vec Large、Whisper Large-v3。
- 在 4 个 MOS 数据集 BVCC、BRSpeech-MOS、SingMOS、TMHINT-QI 上比较多种层利用策略：
  1. Last Layer（LL）：仅使用冻结骨干最后一层，作为标准特征提取基线；
  2. Best Layer（BL）：从逐层分析中选取单个冻结中间层；
  3. Weighted Sum（WS）：用可学习标量权重对全部层表示做归一化加权求和，作为朴素跨层聚合；
  4. Full Fine-Tuning（FT）：整个 SFM 与回归头联合优化，作为强基线；
  5. Adapter + Mean（A+M）：即 CAL-MOS 的层校准聚合方案，每层先经过独立 adapter（线性投影、LayerNorm、ReLU、第二线性层），再将适配后的各层序列拼接并 mean-pool，形成固定维话语表示，使每层在融合前被转换到更任务对齐的空间，而无需全量适配骨干。
- 聚合或层选择后，使用 masked mean pooling 得到话语级嵌入，送入 MLP 回归头（线性→ReLU→线性），预测值裁剪到 [1,5]。
- 训练目标为 MSE，batch size 64，AdamW（β1=0.9, β2=0.98, ε=1e-8），weight decay 1e-6，基于范数的梯度裁剪阈值为 10，cosine 学习率调度配合 500 步线性 warm-up，学习率在 1e-5 到 5e-5 之间调整。

## 实验结果
- 先进行 20-epoch 筛选以覆盖所有骨干和训练机制，再对最有竞争力的骨干做详细逐层分析，并将最终比较扩展到 100 epochs。
- 指标包括话语级和系统级 MSE 与 SRCC。
- 关键发现：最有利的层强依赖骨干和数据集，强层常出现在网络早中期，而不是固定出现在最后一层；朴素 Weighted Sum 相比 Last Layer 常有提升，但跨骨干和数据集并不稳定，不是可靠通用解；Full Fine-Tuning 通常性能更强，但计算代价更高。
- 提出的 Adapter + Mean / 层校准聚合在冻结骨干条件下提升了多层融合鲁棒性，缩小了与全量微调的差距，是比朴素加权聚合更稳健的冻结骨干替代方案。
- 论文贡献可概括为：系统实证了 MOS 预测中的层利用问题；证明最佳深度强依赖骨干和数据集且朴素加权融合不可靠；证明聚合前进行逐层校准能提供更强、更鲁棒的冻结骨干方案。

## 一句话评价
该工作系统刻画了 SFM 层选择与跨层融合对 MOS 预测的影响，并用轻量逐层适配器校准提升融合鲁棒性，为资源受限下的鲁棒 SQA 提供了实用方案与经验指南。

---

## 29. Tracing the Origins: Legacy Codec Identification in Neural Audio Transcoding

**作者**: Wonje Heo, Shinee Youn, Yooshin Kim, Chuck Chae, Donghoon Shin
**链接**: [2609.14916](https://arxiv.org/abs/2609.14916)
**分类**: Audio Forensics / Neural Audio Codec Forensics | **关键词**: audio forensic, neural audio codec, transcoding, legacy codec identification, Residual Vector Quantization, Transformer

## 核心痛点
传统音频取证主要依赖线性信号处理假设，通过分析解码波形或比特流中的统计伪影（如频谱截断、量化噪声、频带失真）来追溯压缩历史。然而，基于残差矢量量化（RVQ）的神经音频编解码器（NAC）将连续音频转换为离散 token，这种非线性神经转码会掩盖 legacy 编解码器留下的底层痕迹，导致传统取证方法性能崩溃。论文将 legacy-to-neural transcoding 场景下的源编解码器识别定义为新的取证空白，并指出已有研究多关注 NAC 本身特性或下游生成任务，尚未系统解决 RVQ token 中叠加伪影的解耦与 legacy codec 溯源问题。

## 方法创新
论文提出一个基于 Transformer 的取证框架，直接从离散神经 token 域恢复 legacy 压缩痕迹。框架输入 RVQ token 序列 X ∈ R^{B×L×T}，先利用预训练 NAC 码本映射到连续嵌入空间 E ∈ R^{B×C×L×T}。为解耦 legacy-to-neural 转码叠加的伪影，设计三个模块：
- **Layer-Causal RVQ Transformer (LCR-Trans)**：通过 2D 卷积提取时间步与码本层局部相关性，经 GroupNorm 和 GELU 后，使用沿码本层轴的因果掩码注意力建模层间依赖，避免未来层信息泄漏。
- **Dynamic Layer-wise Attentive Aggregator (DLAA)**：利用不同量化层对取证贡献不均的特性，联合 Global Layer Weight 与 Temporal Layer Attention，经 sigmoid 生成动态注意力图 A ∈ R^{B×1×L×T}，对层轴加权聚合并经 1D 卷积得到压缩时序特征 Z ∈ R^{B×C×T}。
- **Temporal Context Transformer (TC-Trans)**：建模长时上下文，捕捉 legacy 编解码器在处理预回声、瞬态等事件时的时序签名，经 Adaptive Average Pooling 得到全局特征 v，最后送入 MLP 分类器进行源识别。

## 实验结果
基于 VCTK 构建大规模数据集：语音先经 FFmpeg 使用 MP3、AAC、Opus、Vorbis、G.711 µ-law 五种 legacy 编解码器压缩，再经预训练 48 kHz EnCodec 转码；同时设置未经 legacy 压缩的 clean 参考。测试覆盖 32、64、96、128 kbps 四种比特率。固定比特率编解码器识别中，32 kbps 达 99.99%，64 kbps 达 99.70%，96 kbps 达 98.36%，128 kbps 达 97.32%，准确率与 Macro-F1 均超过 97%。固定编解码器的比特率分类中，AAC 为 99.97%，Vorbis 为 99.65%，MP3 为 84.43%，Opus 为 71.01%。结果表明低比特率下 legacy 伪影更强、更易识别，且传统编解码器痕迹在神经转码后仍可被检测。

## 一句话评价
本文首次系统定义并验证了 legacy-to-neural transcoding 下的音频取证问题，证明传统编解码器痕迹在 RVQ-NAC 转码后仍可被 Transformer 层次-时序建模有效识别，为神经编解码时代的音频完整性与来源追踪提供了可行基础。

---

## 30. POLARIS: Training-Free Audio Fingerprinting with Saliency-Based Landmarks and Delaunay Grouping

**作者**: Jiheng Li
**链接**: [2609.14820](https://arxiv.org/abs/2609.14820)
**分类**: Audio Fingerprinting / Music Information Retrieval | **关键词**: Audio Fingerprinting, Music Information Retrieval, Saliency Map, Delaunay Triangulation, Landmark-based Hashing, Training-free

# POLARIS: Training-Free Audio Fingerprinting with Saliency-Based Landmarks and Delaunay Grouping

## 核心痛点
- 实际音频指纹查询常受压缩、噪声、滤波、混响、声学录音等失真影响，但全局音高与节奏保持不变。
- 传统基于频谱峰值的地标检测只保证局部极大值，不衡量突出程度、不考虑局部背景变化，稳健性受限。
- 参考库索引需要紧凑，查询处理需要高效；训练免费方法与神经方法之间存在精度与成本权衡。
- 真实重录音评测不足：合成失真可控但无法完全反映播放设备和环境。

## 方法创新
1. **基于显著性的地标选择**
   - 输入对数幅度谱图 X，归一化最大值为 80。
   - 细尺度平滑 Xs = Gs(X)，宽背景 C = Xs − Gb(Xs)。
   - 对比度归一化 N = C / sqrt(Gn(C^2) + eps^2)，使用周围对比能量归一化。
   - 显著场 S = βN + γ[Xs − τ]_+，结合归一化对比度与幅度项。
   - 在 S 上检测局部极大值，丢弃 S ≤ 5，按 S 排序；2 s 滑动窗口速率控制保留约 22 个地标/秒。
2. **Delaunay 指纹构建**
   - 将地标坐标 (f_i, t_i) 归一化为 z_i = (f_i/r_f, t_i/r_t)，平衡频率与时间尺度。
   - 对每首参考音频的所有地标做 Delaunay 三角剖分，每个三角形面是一个候选指纹。
   - 满足空圆准则；三角形数量随 n 线性增长（< 2n），避免 C(n,3) 组合爆炸。
   - 过滤退化三角形和跨度太大的三角形（时间跨度、归一化面积、最长边、外接圆半径）。
   - 哈希：按时间排序三个顶点，编码第一个顶点的绝对频率及其余两个顶点的相对时频偏移，按标准地标哈希量化 hΔ = Q([f1, f2−f1, t2−t1, f3−f1, t3−t1])；t1 一并存储用于时间对齐。
3. **查询端扩展与匹配**
   - 失真会移动地标或产生新地标，改变 Delaunay 剖分，导致参考三角形在查询中不再构成面。
   - 两跳邻域扩展：只在查询端，对每个查询地标考虑时间上更晚、最多两跳可达的地标，与其中两个邻居组成额外查询指纹；不限于是 Delaunay 面。限制为 12 个最近邻、每个地标最多 24 个额外指纹。参考索引不变。
   - 匹配：常规哈希匹配与时间偏移投票；对五个量化值分别 ±1 查找以减少量化边界漏检；稀有哈希匹配权重更高；最强加权聚类给出曲目得分和查询偏移。
   - 自适应查询扩展：先只用原始 Delaunay 面匹配；若 top 曲目至少有 8 个匹配哈希且得分领先第二名的 margin ≥ 0.40，则直接返回；否则加入两跳指纹重匹配。margin = (s1−s2)/s1。

## 实验与结果
- **数据集**
  - PEX Hard Medium：953 首参考曲目；只保留 tempo 为空或 100、pitch 为空或 0 的标注，得到 791 个查询，覆盖压缩、滤波、噪声、增益变化、回声及组合失真。
  - SD-RR（Song Describer Real Re-recording）：从 Song Describer 开放许可音乐中构建；排除禁止衍生许可和音频不足的曲目，706 首中保留 496 首作为参考集；固定随机种子 20260819，每首取 3 个不重叠 10 秒片段，共 1488 个查询。
  - 录制设置：14 英寸 MacBook Pro (2023) 内置扬声器以 40% 系统音量播放；iPhone 14 Pro Max 约 1.6 m 处用 Apple Voice Memos 录音；460 首在住宅公寓、36 首在户外录制。通过同步 chirp 和频谱对齐确定 ground-truth 偏移。
- **对比系统**
  - POLARIS-O：仅原始 Delaunay 面指纹。
  - POLARIS-F：始终结合两跳查询指纹。
  - POLARIS-A：自适应，先 POLARIS-O，不满足置信准则再加入两跳指纹。
  - 基线：Audfprint、Panako v2.1、OLAF v2.0.10、NMFP。Audfp-M 和 OLAF 匹配 POLARIS 的逻辑参考负载；Audfp-Q 使用 Audfp-M 参考索引但生成更多查询指纹，近似匹配 POLARIS-F 在 SD-RR 上的查询负载；NMFP 使用预训练 NMFP-Triplet，不重训练。
- **主要结果**
  - POLARIS 在两个基准上均取得所评估训练免费方法中的最佳性能。
  - 在真实录音 SD-RR 上，POLARIS-A 还优于神经 NMFP 基线，查询时间相当，逻辑参考负载更小。
  - 论文片段未给出完整数值表格，但摘要、贡献和实验设置支持以上结论。

## 一句话评价
POLARIS 通过局部归一化显著场提升地标稳健性，并用 Delaunay 三角形与查询端两跳扩展实现无需训练的音频指纹，在合成失真和真实手机重录音上达到训练免费方法最优，且自适应模式在真实录音上超过 NMFP 基线。

---

## 31. CCMAN: Cognitive Instability-Aware Cross-Modal Attention Network for Interpretable Temporal Biomarkers of Verbal Fluency Speech

**作者**: Madhurananda Pahar, Caitlin Illingworth, Dorota Braun, Daniel Blackburn, Heidi Christensen
**链接**: [2609.14764](https://arxiv.org/abs/2609.14764)
**分类**: Speech-based Cognitive Decline Detection | **关键词**: Cognitive Decline, Verbal Fluency, Cross-Modal Attention, Temporal Biomarkers, Multimodal Fusion, Dementia, MCI

# CCMAN：认知不稳定性感知的跨模态注意力网络用于言语流畅性语音的可解释时序生物标志物

## 核心痛点
- 认知衰退早期检测需要可扩展、非侵入式方案，言语流畅性任务尤其有信息量。
- 现有自动化方法多对整段录音做特征聚合，忽略时间维度上的语音动态（如停顿轨迹、语义漂移、词汇熵进展），且可解释性有限。
- 传统指标（停顿、词数、重复、类别切换等）虽有价值但较粗粒度，静态聚合难以捕捉连续规划、词汇提取和发音过程。

## 方法创新
- 提出 CCMAN：一个迁移学习框架，先在 12 个记忆探测任务上预训练任务无关的认知语音表征，再在 60 秒语义和音位言语流畅性任务上微调。
- 词级多模态时序特征：语义嵌入（Sentence-BERT/Word2Vec/FastText）、声学嵌入（Wav2Vec 2.0）、语言描述符（spaCy）、停顿特征和语义漂移，并通过 ASR 时间戳对齐。
- 架构：双向跨模态注意力、门控多模态融合、Transformer 时序建模和 mask-aware 全局池化。
- 训练：结合 focal loss、监督对比损失和熵正则化；注意力熵等用于量化跨模态对齐离散度。
- 可解释性：从语义漂移方差、停顿方差、停顿进展等提取全局与渐进式时序不稳定性生物标志物。

## 实验结果
- 数据：165.44 小时语音，843 名参与者（498 HC、245 MCI、100 dementia）；ASR 系统包括 Whisper、Wav2Vec 2.0 和 NVIDIA NeMo。
- 性能：语义流畅性二分类 Macro-F1 0.81，多分类 0.59；音位流畅性二分类 0.77，多分类 0.53，持续优于静态和时序基线。
- 统计分析：MCI 和痴呆组的语义漂移方差与停顿方差显著高于健康对照组，但平均语义漂移不显著；痴呆组停顿时长随任务进行增长最快。
- 泛化性：在独立 PROCESS-2 基准上，Macro-F1 较基线最高提升 9%。

## 一句话评价
CCMAN 通过词级跨模态时序建模与认知不稳定性统计，为言语流畅性任务中的可解释、可泛化认知衰退早期检测提供了有效框架。

---

## 32. Neyshekar: An Open Persian Read-Speech Corpus for Automatic Speech Recognition

**作者**: Ahmad Amirivojdan, Farzad Nadiri, Abolfazl Alizadeh, Shaghayegh Yaraghi
**链接**: [2609.14542](https://arxiv.org/abs/2609.14542)
**分类**: Speech Recognition | **关键词**: Persian ASR, read-speech corpus, formal and informal register, named entities, Common Voice, Whisper, XLS-R, CC0

# Neyshekar: 面向自动语音识别的开放波斯语朗读语音语料库

## 核心痛点
- 波斯语 ASR 在非正式语体、地区口音和命名实体上持续存在错误；其中非正式语体与命名实体覆盖由本语料库处理，地区口音未覆盖（元数据未记录口音）。
- 现有波斯语资源多面向语音/说话人/情感识别、TTS 旁白或众包朗读，缺少对正式/非正式双语体、命名实体和较长话语的系统覆盖。
- 波斯语正字法省略短元音，加剧发音歧义；正式与非正式波斯语在音系和形态句法上差异显著（diglossia）。
- 众包语料质量不能仅由规模推断，需要可复现的验证、标注一致性和说话人/文本划分。

## 方法创新
- 构建开放 CC0 波斯语朗读语音语料 Neyshekar v6：62,279 条验证录音，99.02 小时，190 位贡献者，34,541 个不同提示。
- 提示池来源：约 5% 来自 HomoRich 同形异义词人工文本，13% 为人工日常短语，82% 由 Claude Sonnet 4.5（36%）、GPT-4.5（27%）、GPT-5.1（19%）生成并经句级审核；覆盖正式/非正式语体与命名实体（足球运动员、歌手、教授、政治家、历史宫殿、街道、纪念碑、机构等）。
- 文本用 shekar 库归一化与分句，支持正式和非正式波斯语；管理员逐句审核，要求完整、流畅、分段正确、语体一致。
- 通过专用 Web 应用录制，无设备限制或信噪比阈值；要求逐字、完整、清晰、流畅朗读，出现重启、犹豫或纠正时必须重录。
- 六准则波斯语验证 rubric：增词、漏词、替换/即兴词；重启、重复、犹豫、句中修正；不完整句子；改变词义的发音错误；正式/非正式替换；破坏性背景噪声。69,744 条提交中 62,279 条（89.3%）被接受。
- 标注可靠性：4 位标注者独立标注 300 条共享样本，Fleiss κ = 0.679 [0.591, 0.757]，Gwet AC1 = 0.900 [0.866, 0.930]，总原始一致率 92.4%，接受类一致率 95.6%，拒绝类一致率 72.3%。
- 预处理：转为单声道 16-bit PCM WAV 16 kHz；使用 shekar Normalizer 标准化波斯字符与空格。
- 划分：按贡献者级别 speaker-disjoint，训练/验证/测试为 142/26/30（注册贡献者），发布版本为 134/26/30（190 位有接受录音的贡献者）；每条 clip 带不透明贡献者标识，划分可审计；包含 text-disjoint 测试子集。
- 提供每条 clip 的贡献者录音负载和无参考信号质量特征；提供 item-level 标注者标签以复现一致性估计，并支持贡献者聚类不确定性估计。

## 数据特征与对比
- 全文：62,279 条话语，99.02 小时，190 位贡献者，平均时长 5.72 秒，626,370 词，29,520 词型，34,541 个不同提示，非正式占比 24.44%（自动分类器，未人工验证）。
- 训练/验证/测试：58,244/1,886/2,149 条；91.99/3.14/3.88 小时；134/26/30 位贡献者；平均时长 5.69/6.00/6.49 秒；词数 585,022/19,187/22,161；词型 29,129/5,868/6,118；不同提示 33,357/1,844/2,101；非正式 24.23%/27.57%/27.55%。
- 评估集 OOV 率 1.11–1.12%（相对训练词表）。
- 与已验证波斯语 Common Voice 26.0 在相同处理下比较：Neyshekar 平均 clip 时长长 46%（5.72s vs 3.93s）；在匹配 626,370 tokens 时词型多 18%（29,520 vs 24,973）；非正式 clip 24.44% vs 16.08%；每 100 词实体数 3.05 vs 1.70；每提示朗读次数 1.80 vs 6.58。
- 贡献者分布：中位 129 条（IQR 16–452，范围 1–5,935）；中位 12.2 分钟；最大贡献者占音频 7.7%，前 10 位占 35.6%，23 位贡献者覆盖一半语料；Gini 0.657，低于 Common Voice 的 0.871。

## 实验结果
- 使用两种 ASR 架构、三个优化种子，报告 WER 和 CER，并在公共 PSRB 样本上独立评估。
- 与时长匹配（约 32 小时）的 Common Voice 训练相比：域内 WER 在 Whisper 上降低 9.5 个百分点，在 XLS-R 上降低 11.6 个百分点；在独立 PSRB 样本上两种架构均约降低 8 个百分点。
- 迁移与混合收益在不同架构和训练预算下并不一致。
- 语料以 CC0 发布，代码与数据见 https://github.com/amirivojdan/neyshekar。

## 一句话评价
Neyshekar 是一个文档完善、验证严谨、划分可审计的开放 CC0 波斯语朗读语音语料库，在正式/非正式语体、命名实体和较长话语覆盖上具有明显特色，并在域内 ASR 上带来显著 WER 增益；但其自动语体/实体标签未经人工验证，迁移与混合收益尚不稳定。

---

## 33. Bridging the Modality Gap in Long-Form Clinical Audio: A Comparative Study of Lightweight and Heavyweight End-to-End SOAP Generation

**作者**: Ziyu Zhang, Mingchen Shao, Wenjie Tian, Tianlun Zuo, Longhao Li, Lei Xie
**链接**: [2609.14467](https://arxiv.org/abs/2609.14467)
**分类**: Clinical SOAP Note Generation / End-to-End Long-Form Clinical Audio Understanding | **关键词**: Clinical SOAP Note Generation, Long-Form Audio Understanding, End-to-End Multimodal Understanding, Generative Reward Policy Optimization, Online Preference Distillation

# 论文总结：Bridging the Modality Gap in Long-Form Clinical Audio

## 核心痛点
- 从长时医患对话中自动生成临床文档仍是现代音频-语言模型的难题，超过 5 分钟的长音频推理尤其困难。
- 级联 ASR 系统表现良好，但端到端（E2E）模型在扩展音频上常出现信息丢失与幻觉。
- BeTraC 2026 挑战要求模型绕过传统 ASR-to-text 级联流程，直接从原始医疗音频生成临床 SOAP 笔记。

## 方法创新
- 提出全 E2E 多模态系统，直接将原始医疗音频映射为结构化 SOAP 笔记，不生成中间转写文本。
- 构建约 141 万有效样本、约 8,650 小时音频的多任务语料，覆盖长音频 ASR、稠密音频描述、时间定位、医学 ASR、SOAP 生成和文本医学 NLP 等十类来源。
- 采用四阶段训练流程：领域预训练、监督微调（SFT）、生成式奖励策略优化（GRPO）、在线偏好蒸馏（OPD）。
- GRPO 使用四维自定义奖励：Concept F1、ROUGE-2、SOAP 格式、长度惩罚，以提升医学概念召回并减少幻觉。
- OPD 使用 Chain-of-Thought 蒸馏策略，将复杂临床推理能力蒸馏进标准单次生成策略，并抑制超长音频触发的重复循环。
- 系统架构：冻结音频编码器提取声学表示，经冻结 audio-to-LLM aligner 投影至 LLM 嵌入空间，再由全微调 dense LLM decoder 自回归生成 SOAP。
- 双轨对照：Lightweight 基于 Qwen2.5-Omni-3B，移除视觉塔和语音生成头；Heavyweight 基于 Qwen3-Omni-30B，保持相同 E2E 单次前向架构，刻意不使用 RAG 或 CoT 外部工具以隔离模型规模影响。
- 推理使用确定性 greedy decoding（T=0, p=1.0）、重复惩罚 1.15、最大生成长度 2048 tokens，后处理仅提取 dialog_id 并保留模型输出原文。

## 实验结果
- Lightweight 轨道：zero-shot Concept F1 为 0.2604，SFT 提升至 0.3872，GRPO 进一步提升至 0.4082；ROUGE-2 从 0.0920 提升至 0.2155，再到 0.2323。
- Heavyweight 轨道：zero-shot Concept F1 为 0.1879，领域预训练后大幅升至 0.5129，SFT 为 0.5136，GRPO 达到 0.5167；ROUGE-2 从 0.0558 提升至 0.3410，最终 GRPO 为 0.4093。
- 从 3B 扩展到 30B，在相同 E2E 架构与训练流程下，Heavyweight 比 Lightweight 的 Concept F1 绝对提升 0.108（0.5167 vs. 0.4082）。
- 最佳 Lightweight 模型在 Concept F1 上超过 Whisper-Large-v3 + Qwen3 级联基线（0.2860）和 Qwen3-ASR-1.7B + Qwen3 级联基线（0.2772），绝对优势超过 0.122。
- 每个训练阶段均带来渐进提升；大模型显著增强长上下文潜在推理与临床信息保留能力，但大模型上 GRPO 相对增益较温和。

## 一句话评价
该工作通过四阶段端到端多模态优化和 3B/30B 双规模对照，证明直接音频到 SOAP 生成可稳定超越级联 ASR+LLM 基线，并为长音频临床文档自动化提供了可复现的训练与评测范式。

---

## 34. Grounded in Sound: Reinforcement Learning with a Frozen Acoustic Judge to Curb ASR Insertion Hallucinations

**作者**: Tingzhen Xiong, Rilin Chen, Weiwei Li, Wentao Zhang, Qicong Xie
**链接**: [2609.14455](https://arxiv.org/abs/2609.14455)
**分类**: ASR Reinforcement Learning / Insertion Hallucination Mitigation | **关键词**: ASR hallucination, insertion errors, GRPO, acoustic-fidelity reward, frozen CTC judge, wav2vec2, speech LLM, selective ASR, out-of-distribution generalization

## 核心痛点
- 当前用于 ASR 后训练的强化学习奖励几乎都活在文本空间：只比较 hypothesis 与 reference，从不检查 hypothesis 是否被音频支持。
- 在高度规则的语音上，这会纵容一条捷径——依赖强语言先验去猜，而不是聆听。一旦声学条件退化，捷径不受约束，模型就会输出流畅但无音频依据的词，即 insertion errors（插入错误/ASR 幻觉）。
- 作者基线测量显示：μ=0 的纯 WER-GRPO 基线中，插入率随声学难度严格单调上升，从干净语音的 0.37% 升至真实远场会议语音 AMI-SDM 的 5.75%。插入错误恰好集中在 ASR 部署最需要可靠性的场景。

## 方法创新
- 提出 acoustic-fidelity reward：在 GRPO 奖励中加入一个单独预训练、永久冻结、非自回归、字符级 wav2vec2-CTC acoustic judge。该 judge 只在训练时使用，推理时完全不存在，最终模型只做一次 greedy decoding。
- 两个模型角色：policy 为 Qwen2-Audio-7B（LoRA 适配），judge 为字符级 wav2vec2-large-960h（永久冻结）。二者读同一段音频，但 policy 随训练变化，judge 是固定标尺。独立性指优化独立：judge 不接受 policy 梯度。
- 奖励设计：对每个音频采样 G=8 个候选转写；奖励包含文本项 -WER 和声学项 S_ctc(y,X)。组内 robust Z-normalize 后加权：R_i = Z_grp(-min(WER(y_i,ref),2.0)) + μ Z_grp(S_ctc(y_i,X))。μ=0 恢复纯 WER-GRPO 基线；无 KL penalty，β=0，因此 μ 是唯一差异。
- 声学项：S_ctc(y,X) = -CTCLoss(logp_ctc(X), tok(y)) / max(|tok(y)|,5)。judge 对音频前向一次获得帧级字符 log-prob，再对候选的字符序列 tok(y) 计算 CTC alignment loss。8 个候选复用同一 logp，因此每 utterance 只增加一次 judge 前向，而不是每候选一次。
- tok(·) 不是发音模型，而是 judge 自身的 32 符号字符词表（A-Z、撇号、分隔符）；y 被大写并逐字素映射，无 G2P、无词典，因此不受词典覆盖限制，适合 OOD 词。空转写或字符数超过可用帧数的候选绕过 CTC，取固定 -10。CTC 使用 zero_infinity=True，存在一个实现锐边：若候选名义上短但 CTC 不可对齐，可能返回 loss 0，即最有利分数。
- 选择字符级 CTC judge 的原因：0.3B judge 尽管有句级监督带来的弱语言先验，但非自回归、无外部语言模型、使用条件独立帧预测，架构和目标都与 policy 不同，适合作为独立声学一致性裁判。
- 训练数据：LibriSpeech 上的 RL 训练使用四个固定桶，各 25%——clean、noise@10dB、noise@7.5dB、noise@5dB，固定种子预生成，噪声来自 MUSAN 训练子集且与测试不相交。同一退化音频用于所有 μ，差异归因于奖励权重而非数据。AMI 被排除在 RL 训练之外，仅用于最终评估；训练只用加性噪声，无混响增强，因此 AMI-SDM 测试远场迁移。
- 训练条件通过 judge gate 筛选：clean、10dB、5dB 的 pairwise ranking accuracy 分别为 0.996、0.993、0.984，均通过；7.5dB 在 10dB 与 5dB 之间插值。AMI 上为 0.843(IHM) 和 0.775(SDM)，低于 0.85 阈值且 SDM margin 为负，因此远场条件不进入训练混合。
- 推理：所有主要比较使用一次 greedy decode（temperature 0），无外部 scorer。CTC rescoring 和 reference-WER oracle 仅作诊断例外；selective-ASR confidence 只用 policy log。
- 论文还做了四个预设分析：反事实行为、CTC rescoring、judge-free selective ASR、插入成本，用于评估训练时声学反馈是否能在无推理时辅助的条件下提升可靠性。

## 实验结果
- 在 LibriSpeech 上训练，并在六层难度梯度上评估，包括真实 AMI 会议语音，共 33,282 个 utterance-condition 实例。
- 相对 schedule-matched WER-GRPO 基线：插入错误在 close-talking AMI-IHM 上降低 28.3%，在 far-field AMI-SDM 上降低 22.3%。
- AMI-SDM 的 WER 从 35.89% 降至 34.71%，显著；其余五个难度层没有可检测的 WER 差异。
- 插入错误降低在 meeting-level clustered bootstrap 下保持。
- 四个预设分析支持 content-conditioned insertion calibration：在保留能量和 VAD 的不可理解音频上，输出崩溃 85–90%；评估的 32-best CTC rescoring 配置无法恢复增益，但 RL 把增益内化到单次 greedy decoding；policy-only confidence 在四个评估设置下都给出更低的 insertion-AURC；并测量插入成本。
- 作者将论文定位为机制论文，在一个实例中演示：7B speech LLM 加 0.3B CTC judge。贡献包括：六层声学难度梯度下的插入错误特征；声学一致性奖励减少 held-out AMI 插入；以及四个预设分析。

## 一句话评价
- 该工作把“音频是否支持该转写”变成训练时的独立奖励，用冻结 CTC judge 抑制 ASR 插入幻觉且不增加推理成本；思路清晰、机制验证充分，但效果依赖 judge 在目标域的质量，奖励归一化存在长度依赖，zero_infinity 等实现细节也有锐边。

---

## 35. Exploiting Speech LLM Representations for Multilingual and Cross-Lingual Parkinson's Disease Detection

**作者**: Sarthak Giri, Zi Haur Pang, Tatsuya Kawahara
**链接**: [2609.14431](https://arxiv.org/abs/2609.14431)
**分类**: Pathological Speech Analysis / Speech LLM Representation Probing | **关键词**: Speech LLMs, Parkinson's Disease Detection, Cross-Lingual Transfer, Layer Aggregation, Representation Probing, Pathological Speech Analysis

# 论文总结

## 核心痛点
- Speech LLM 在多种语音任务上表现强，但在病理语音分析，尤其是帕金森病（PD）检测中的内部表征利用仍未被充分探索。
- 现有 PD 相关 Speech LLM 研究多将其视为黑盒预测器，依赖零样本提示和生成输出，未检查内部表征是否包含更丰富的病理信息。
- 已有分析表明，音频表征投影到语言模型空间后，副语言信息可能逐渐衰减；而病理语音依赖细微副语言异常，因此 PD 相关线索是否保留尚不清楚。
- 逐层选择最佳表征需要穷举搜索，且可能无法跨模型或跨语言稳定泛化。

## 方法创新
- 首次系统比较 Speech LLM 的音频编码器表征、LLM 解码器表征和生成输出在多语言与跨语言 PD 检测中的效果。
- 对冻结的预训练模型进行逐层表征探测：对每一层隐状态做时间/序列维平均池化，再训练轻量下游分类器。
- 提出基于 Squeeze-and-Excitation（SE）的样本自适应动态层聚合框架：对每层做时间与特征维平均池化得到汇总向量，经两层 MLP 与 softmax 生成样本级层权重，再加权融合各层表征。
- 零样本生成评估包含两种提示：原始音频提示，以及额外提供手工声学生物标志物描述的 biomarker-guided 提示；通过 Spearman 相关性跨语言筛选出 17 个生物标志物特征，覆盖持续元音、DDK、朗读语音三类任务。

## 实验设置
- 数据集：捷克语、德语、西班牙语（PC-GITA，哥伦比亚）PD 语音数据，由 OneVoice-MSD 特别会议组织方提供；包含持续元音、朗读、DDK 任务；说话人级不重叠划分。
- 评估协议：多语言设置与 leave-one-language-out（LOLO）跨语言设置，包括 German+Czech→Spanish、Spanish+Czech→German、Spanish+German→Czech。
- 模型：Qwen2-Audio、Phi-4-Multimodal、Ultravox 1、Qwen2.5-Omni；并比较 Whisper-large、XLS-R 2B、HuBERT-large 等语音基础模型基线。
- 指标：表征探测与层聚合使用 AUC 与 UAR；零样本生成仅使用离散文本 PD/HC 预测的 UAR；统计显著性采用说话人级 bootstrap 与 Benjamini–Hochberg 校正。

## 主要发现与实验结果
- 编码器表征在大多数模型和设置中持续优于解码器表征。
- 提出经验层级：encoder > decoder > generative output，说明病理线索在 Speech LLM 流程中逐步衰减。
- 编码器和解码器内部均在中间层达到较好分类性能，说明 PD 相关声学线索分布在多个 Transformer 层，而非集中于单一层。
- 所提出的 SE 层聚合方法在多个实验中超过最佳单层选择和全层平均池化，减少了对穷举层搜索的需求。
- 生成输出在临床任务中可靠性低于内部表征，表明不应仅依赖生成文本进行 PD 判断。

## 一句话评价
该工作通过系统探测揭示 Speech LLM 编码器内部表征携带最丰富的 PD 病理线索，并提出样本自适应 SE 层聚合方法，为多语言与跨语言 PD 检测提供了无需穷举层搜索的稳健方案。

---

## 36. Differentiable Digital Signal Processing Mixture Model-Guided Diffusion for Synthesis Parameter Estimation from Harmonic Sound Mixtures

**作者**: Kengo Takemoto, Tomohiko Nakamura, Hiroshi Saruwatari
**链接**: [2609.14427](https://arxiv.org/abs/2609.14427)
**分类**: Neural Audio Synthesis / Music Information Retrieval | **关键词**: DDSP, DDSPMM, Denoising Diffusion Probabilistic Model (DDPM), Synthesis Parameter Estimation, Harmonic Sound Mixtures, Music Source Analysis

### 核心痛点
- DDSP autoencoder 通过三类逐帧合成参数（F0、loudness、timbre features）重建单音谐波乐器声音。
- 先前提出的 DDSP mixture model（DDSPMM）将混合音表示为多个预训练 DDSP autoencoder 解码器合成源信号之和，从而可直接从观测混合音估计各源的合成参数，而无需先做显式源分离。
- 但 DDSPMM 的拟合过程把每帧合成参数当作独立变量，未显式建模合成参数的时间变化，容易产生过度的时间波动，导致估计轨迹偏离真实演奏。真实演奏中，F0 和音色在延音段通常平滑变化，而 loudness 和音色在音符起始附近可快速变化，这些时间特性未被显式约束。

### 方法创新
- 提出将 denoising diffusion probabilistic model（DDPM）作为合成参数轨迹的生成先验，并嵌入 DDSPMM 的 analysis-by-synthesis 估计流程。
- DDPM 以乐谱信息为条件预训练，条件包括乐器类型 one-hot 向量 c_inst 与标准化的乐谱 F0 序列 c_score，从而建模与乐谱相关的时间变化。
- DDPM 的生成目标不是原始参数，而是相对于乐谱初始化值的残差：F0 残差、loudness 残差以及 timbre 特征各维标准化后拼接为 u0 ∈ R^{T×(D+2)}；定义变换 Φ 将合成参数矩阵 x 转为 u0，并用 Φ^{-1} 逆变换。
- 噪声预测器采用 U-Net：三级编码器-解码器结构，含跳跃连接、2D 卷积块、最大池化下采样、双线性上采样以及瓶颈卷积块；扩散步 τ 经正弦位置编码和 MLP 注入，c_score 下采样后经 Conv2D+ReLU 注入，c_inst 通过 FiLM 进行通道级缩放和平移调制。
- 估计阶段将合成参数先验作为正则项：L_prop({x_k}) = λ L_MS(y, Σ_k Dec_ψk(x_k)) + Σ_k R_k(x_k)，其中 R_k(x_k) = -log p(x_k|c_k)。
- 利用预训练条件 DDPM 的 score 估计近似 -∇_{x_k} log p(x_k|c_k)，在 DDPM 反向扩散过程中使用 DDSPMM 从当前参数估计重合成混合音，并以观测混合音与重合成混合音之间的重构误差引导去噪，从而得到时间上更合理的合成参数轨迹。
- 源合成器 Dec_ψk 在估计时保持预训练参数固定；整体思想是用扩散生成先验正则化 DDSPMM 拟合，同时保留混合音重构保真度。

### 实验结果
- 在木管乐器与弦乐器合奏混合音上进行了实验。
- 摘要与引言指出，基于 DDPM 的正则化通过施加时间合理性约束，提高了合成参数估计性能，尤其对 loudness 和 timbre 特征的估计改善明显。
- 论文还强调 DDSPMM 基线容易产生过度时间波动，而引入 DDPM 后轨迹更符合真实演奏中的时间特性。片段中未给出完整数值结果，但总体结论是所提方法优于原始 DDSPMM 估计。

### 一句话评价
- 该工作把条件扩散模型作为 DDSPMM 合成参数估计的时间先验，通过扩散先验加混合音重构误差引导，生成更 plausible 的参数轨迹，是 DDSP 混合音分析与生成式先验正则化相结合的有前景探索。

---

## 37. AURA: Unified Multimodal Framework for Conversational Music Editing

**作者**: Quoc-Huy Trinh, Minh-Van Nguyen, Debesh Jha
**链接**: [2609.14344](https://arxiv.org/abs/2609.14344)
**分类**: Music Editing / Controllable Music Generation | **关键词**: Conversational Music Editing, Multimodal Large Language Model, Controllable Music Generation, Concept Tokens, MusicGen, LoRA

# AURA: 统一多模态会话式音乐编辑框架

## 核心痛点
现有指令驱动的音乐编辑系统（如 AUDIT、InstructME、M2UGen、Instruct-MusicGen、LeVo）通常**将每一次编辑请求独立处理**，不支持多轮对话。这导致它们无法解析依赖前序对话轮次的编辑指令（例如“把这个底鼓收一点”之后再说“再补一层高频质感”）。在真实音乐制作流程中，用户会**逐步精修**一首曲目，期望每次编辑都与不断演化的对话上下文保持一致，因此单轮范式存在明显局限。

## 方法创新
AURA 是一个统一的多模态会话式音乐编辑框架，核心思路是**把多模态意图理解与音频生成解耦**：

1. **多模态大语言模型（MLLM）**：采用 Qwen2.5-Omni 的 Thinker 组件，联合处理完整的对话历史 T、可选图像 I 与参考音频 X_ref，输出自然语言回复以及 n_c 个特殊 `<EDIT_CONCEPT>` token；这些 token 的最终隐状态（d_llm = 3584）紧凑地编码了编辑操作类型、目标乐器、期望属性与对话约束。若无需音频编辑，则只输出文本、不产生 concept token。
2. **概念与音频投影器**：concept token 经 LayerNorm + 两层 MLP 投影到 MusicGen 隐空间（d_m = 1536）；参考音频经冻结的 EnCodec 编码得到帧级表示，再由 audio projector 映射到同一空间。前者规定“改什么”，后者提供“保留什么”的帧对齐信息。
3. **概念到音频模块（C2A）**，插入冻结的 MusicGen-medium 解码器中：
   - **BiFAM（双向特征对齐模块）**：用共享的位置对齐 query 同时从参考流与生成流检索信息（分别配 full mask 与 causal mask，带可学习层权重 α_r、α_m），再通过 FiLM 变换（rank-256 瓶颈 MLP 产生 γ/β，门控初始化为零）调制解码器自注意力输出，从而在不向自回归序列追加 token 的前提下保留参考结构。
   - **Concept Cross-Attention**：投影后的 concept token 作为跨所有解码层与生成步共享的语义记忆被交叉注意力读取，仅在该注意力的 K/V 投影上使用 rank-64 LoRA。
4. **训练策略**：MLLM 与 MusicGen 主干参数冻结，仅训练 LoRA 适配器、投影器和 C2A 模块，共 **91M 可训练参数**（冻结主干 1.9B）。零初始化的 BiFAM 与 LoRA 保证初始时等价于预训练模型，使 AURA 学习的是“编辑残差”而非重新学习音频生成。推理时采用 classifier-free guidance：将 Z_concept 置零做无条件 pass 而保留 Z_ref，使引导方向隔离出编辑操作、固定参考内容。
5. **联合目标**：L = L_MLLM（多轮推理与 concept token 位置监督）+ L_music（codebook 交叉熵），使学到的 token 既具语言意义又对音频生成有用。

## 实验与结果
- **数据**：由 Slakh2100 训练集生成 **66,539 条会话式对话**（含编辑类型与 10 类乐器标注）；评测使用 Slakh2100-test 的 1000 条域内样本与 MoisesDB 的 1000 条域外样本（LLM 撰写指令）。配置：n_c = 9 个 concept token，AdamW，lr 1e-4，有效 batch 16，LoRA rank-64（α=128），CFG scale 2.0。
- **指标**：音频质量（FAD↓、KL↓）、指令遵循（CLAP↑）、编辑正确性（P-Demucs↑）、内容保持（SSIM↑、SI-SDR↑、SI-SDRi↑）。
- **单轮编辑**：AURA 在编辑正确性与内容保持上全面领先。域内 Add 任务 FAD 0.52 vs Instruct-MG 2.01，SSIM 0.78 vs 0.37；Remove 任务 FAD 0.34、SSIM 0.80、SI-SDR +11.32（基线为负）；域外 Add/Remove 的 FAD 相比现有指令方法降低约 **4–5 倍**。
- **多轮编辑（MoisesDB 域外，依次 −drums、+bass、+guitar）**：AURA 在三轮中 SSIM 分别为 0.84 / 0.79 / 0.54，均显著优于 M2UGen、Instruct-MG、LeVo；且优于仅施加最终编辑的对照（Ctrl，0.49），说明对话上下文确实带来增益。

## 一句话评价
AURA 通过“MLLM 提炼概念 token + 注入冻结 MusicGen 的 C2A 模块”，以极少可训练参数（91M）把音乐编辑从单轮指令范式推进到**多轮、多模态、上下文一致**的会话式编辑，在编辑正确性与未编辑内容保持上均大幅超越现有 SOTA。

---

## 38. A New Transformer-Based Approach for Audio-Based Kinship Verification and a New Uncontrolled Mandarin Kinship Speech Dataset

**作者**: Qiyang Sun, Langqing Zhang, Yupei Li, Björn Schuller
**链接**: [2609.14145](https://arxiv.org/abs/2609.14145)
**分类**: Audio-Based Kinship Verification | **关键词**: Audio Kinship Verification, Transformer, Deep Metric Learning, Kinship Speech Dataset, Cross-Corpus Evaluation

# A New Transformer-Based Approach for Audio-Based Kinship Verification and a New Uncontrolled Mandarin Kinship Speech Dataset

## 核心痛点
- **任务本身困难**：基于音频的亲属关系验证（判断两人是否存在一阶血缘关系）显著难于说话人验证等说话人级任务；多模态融合虽能大幅提升性能，但现实场景中往往无法获取多模态数据，单模态系统性能严重退化。
- **数据稀缺且不真实**：视觉亲属数据集丰富，音频对应物却极其稀缺。现有公开音频亲属数据集要么是互联网采集的 in-the-wild 数据（信噪比极低、使用专业设备录制），要么是在录音棚/安静房间等受控环境采集，均无法反映普通用户用消费级设备在真实条件下录音的场景。
- **语言偏差**：现有音频亲属数据几乎全为英语语音，阻碍语言无关（language-invariant）模型的发展。
- **评估不充分**：几乎无人进行跨数据集评估，缺乏对鲁棒性的验证；同时现有文献极少对音频亲属验证模型做可解释性（XAI）分析。

## 方法创新
### 新数据集：ARKIN（Audio under Realistic conditions for KINship verification）
- 首个在非受控条件下、使用消费级设备录制的普通话亲属语音数据集，定位于受控安静环境与 in-the-wild 数据之间的桥梁。
- 规模：256 名说话人、2554 条话语（95% 普通话、5% 英语）、230 对亲属关系、86 个家庭；每位说话人均标注年龄、性别、国籍，且至少与另一名说话人存在亲属关系。
- 每条话语含人工文本转写与语言标签；音频为 16-bit PCM、48 kHz 采样；话语长度约 0.3s–13.3s，包含快速停顿、错误开头、填充音等多样语音模式。
- 采集方式：参与者用日常设备（通常为手机）在任意时间、地点、背景条件下自由录制，先朗读固定短语再即兴发挥，从而覆盖多样化的背景条件。

### 新模型：CONVTRAP-TN（CONVolution-TRansformer-Attention-Pool Triplet Network）
- 首个将 Transformer 架构应用于音频亲属验证，针对亲属信号“稀疏性”问题，利用注意力机制编码音频。
- 采用深度度量学习（triplet network）与随机三元组挖掘策略（锚点、正样本、负样本）。
- 采用两阶段训练方案：先训练较简单的说话人识别任务，以缓解训练不稳定性（训练不稳定的问题）。
- 通过分析模型注意力权重进行可解释性研究，并开展消融实验。

## 实验结果
- **特征表示**：重采样至 16 kHz，提取 24 维 MFCC（Kaldi，25 ms 帧长 / 15 ms 帧移），经 CMVN 与能量阈值 5 的 VAD 处理。
- **基线表示**：512 分量 GMM-UBM 提取 400 维 i-vector；TDNN 训练的 512 维 x-vector、300 维修改 embedding、ECAPA-TDNN 的 256 维 embedding；SpeechBrain 基于 VoxCeleb 预训练的 ResNet 256 维 embedding（迁移学习）。
- **划分与评估**：7:1:2 划分训练/验证/测试，确保不同集合说话人之间不共享亲属关系，结果取五次独立实验平均。
- **基线实验**：说话人验证与识别、语音识别、年龄估计、亲属验证，以及跨数据集亲属验证实验，结果表明现有方法跨数据集并不鲁棒。
- 与 KAN-AV、TALKIN-Family、FIW-MM 等公开数据集的对比表说明 ARKIN 是首个非受控、消费级设备、普通话的亲属语音数据集。

## 一句话评价
该论文首次将 Transformer 引入音频亲属验证并提出 CONVTRAP-TN，同时发布首个面向日常非受控录音条件的普通话亲属语音数据集 ARKIN，并通过跨语料评测揭示现有方法鲁棒性不足，兼具方法创新、数据贡献与可解释性分析价值。

---

## 39. Robust Cross-Domain Speech-Based Alzheimer's Disease Detection via Iterative Adversarial Self-Training

**作者**: Luqi Sun, Shreeram Suresh Chandra, Aurosweta Mahapatra, Emily Mower Provost, Brian MacWhinney, Berrak Sisman
**链接**: [2609.14139](https://arxiv.org/abs/2609.14139)
**分类**: Speech-Based Alzheimer's Disease Detection | **关键词**: Alzheimer's Disease Detection, Speech Processing, Unsupervised Domain Adaptation, Iterative Adversarial Self-Training, Cross-Domain Robustness, XLS-R

## 核心痛点
- 现有语音 AD 检测多在单一数据集上训练与评估，跨域时性能严重下降，最大降幅达 34.38%。
- 模型容易依赖录音环境、设备与数据集特定伪影，而非疾病相关语音线索；例如仅用 Pitt Corpus 静音段训练也能取得高准确率，存在 Clever Hans 效应。
- 真实应用需要应对录音环境、说话人和数据采集条件变化，且目标域通常缺少诊断标签。

## 方法创新
- 采用无监督域适应，提出 Iterative Adversarial Self-Training（IAST），在无目标域诊断标签条件下学习域不变表示。
- 设计三类递增表示能力的 AD 检测模型：eGeMAPS 手工声学特征模型；冻结参数的 XLS-R 自监督嵌入模型；微调 XLS-R 任务自适应模型。
- eGeMAPS 模型：将语音分 10 段，OpenSMILE 提取 25 维 eGeMAPS，经线性投影、BN/ReLU/Dropout、注意力池化和线性分类。
- 冻结 XLS-R 模型：输入 60 秒音频，冻结 XLS-R 提取帧级嵌入，五层线性降维、BN/ReLU、带 mask 的注意力池化和分类。
- 微调 XLS-R 模型：仅更新最后 3 层 Transformer，其余冻结，以缓解灾难性遗忘与过拟合。
- 结合域对抗训练（DAT）与自训练（ST），通过 IAST 迭代对抗自训练提升跨域泛化。

## 实验设置与结果
- 数据集：Pitt Corpus（552 总样本，AD 309，Control 243）、ADReSS（156，78/78）、Lu Corpus（74，38/36），均来自 DementiaBank，采用 Cookie Theft 图片描述任务。
- 跨域实验显示，多种模型架构在跨域评估中准确率一致下降，最大下降 34.38%（Table 2）。
- IAST 在多种跨域设置下显著提升泛化能力和鲁棒性。
- 由于提供的片段截断，完整实验数值与消融结果需参考全文。

## 一句话评价
该论文面向语音 AD 检测的真实跨域鲁棒性挑战，提出 IAST 无监督域适应方法，并用三类递增容量模型进行系统验证，具有明确的临床落地价值。

---

## 40. StepAudio 3 Realtime Technical Report

**作者**: Bin Lin, Bo Zhao, Boyang Zhang, Boyong Wu, Chao Yan, Chen Geng, Chen Wu, Cheng Yi, Chengli Feng, Chenglin Zhu, Chengting Feng, Chengyuan Yao, Daijiao Liu, DanNi Wan, Daxin Jiang, Dongjian Li, Dongqing Pang, Fei Tian, Feng Tian, Future Li, Gang Yu, Guanglong Yang, Haoyang Zhang, Hongyuan Wang, Jia Peng, Jiahao Song, Jialong Xue, Jiamin Fan, Jiangjie Zhen, Jianzheng Gao, Jincheng Wen, Jinghua Liang, Jinglan Gong, Jun Chen, Li Xie, Liang Zhao, Lifang Zhang, Lingli Ji, Lun Cai, Min Xu, Peilin Li, Peng Yang, Pengfei Tan, Qingjian Lin, Qinxin Du, Ruijie Xiong, Runze Li, Shenghua Hu, Shengqian Qin, Shi Qiu, Siqi Tu, Siyi Zhou, Tianjiao Deng, Wanying Lu, Weiming Niu, Wen Sun, WenWen Qu, Xiangyu Zhang, Xianwei Zhang, Xiaosu Su, Xing Chen, Xinyu Liu, Xuerui Yang, Yan Wu, Yang Li, Yang Yang, Yechang Huang, Yibo Zhu, Yifan Zhang, Yinuo Yan, Youjun Chen, Yu Fu, Yu Luo, Yu Zhou, Yujie Chen, Yumang Wang, Yunzhou Ju, Yuxiang Yang, Yuxin Li, Yuxin Zhang, Zekai Liu, Zengwei Yao, Zhaoxin Yuan, Zhenwei Mou, Zhiquan Zhang, Zhiyue Wu, Zichao Li, Zichao Zhou, Ziqi Ren, Zixuan Wang
**链接**: [2609.14005](https://arxiv.org/abs/2609.14005)
**分类**: Realtime Spoken Dialogue / Full-Duplex Audio-Language Model | **关键词**: StepAudio 3 Realtime, Full-Duplex Speech Interaction, Think-While-Speaking, Audio-Language Model, Streaming Voice Agent, Mixture-of-Experts, Speech Recognition

# StepAudio 3 Realtime 技术报告总结

## 一、核心痛点（Core Pain Points）
实时语音交互系统面临三重矛盾：
1. **深度推理 vs 响应延迟**：复杂请求需要模型深度思考，但自然对话要求即时回应，二者难以兼顾。
2. **轮次管理的复杂性**：用户的停顿可能只是未说完，模型说话期间的插话可能是附和（backchannel）也可能是实质性打断，系统必须准确判断对话主导权（conversational floor）。
3. **工具调用与对话流的冲突**：外部任务（如检索、下单）可能比触发它的语音交换持续更久，如何在不打断对话的同时完成异步工具执行并把结果回灌到后续对话中，是开放难题。

## 二、方法创新（Method Innovation）
论文提出以 **listen–converse–think–act（听—说—思—行）连续循环** 组织的音频语言基础模型：
- **Deep Perception（深度感知）**：融合词汇内容与副语言声学线索（情感、韵律、声学事件），解析用户真实意图；ASR 专用分支 StepAudio 3 ASR Max 与之共享预训练与中间训练，仅在 SFT 阶段分叉。
- **Seamless Duplex（无缝双工）**：将用户与模型音频流同步建模，天然处理停顿、附和与打断；生成器输出回灌至模型音频流形成闭环。
- **Think-While-Speaking（边想边说）**：核心创新点，将私有推理与语音输出并行执行，配合 **Adaptive Thinking**（自适应决定何时需要显式推理）与 **MTP / Medusa 多 token 预测**加速私密推理，从而在保持实时说话的同时获得接近专用推理模型的对话与推理表现。
- **Streaming Voice Agent（流式语音智能体）**：在执行前解析意图与所需参数，异步执行工具，并在用户继续说话的同时把返回证据并入对话上下文。
- **架构**：MoE 架构，总参数约 196B，每 token 激活约 11B；语言骨干基于 Step 3.7 Flash，音频前端采用 Qwen3-Omni 的 Audio Transformer（AuT）编码器，经 adapter 映射到 LLM 表示空间。
- **训练流程**：三阶段预训练（模态对齐 → 多模态混合训练 → cooldown），固定序列长度 32K、共 1.2T token，并刻意提升纯文本比例以保留基座通用能力；中间训练将上下文扩展至 128K，并大幅增加音频理解与 Agent 交互数据。
- **数据构建**：自动化大规模音频清洗流水线（SED + VAD 过滤、重切分、多识别系统交叉校验、质量分级）；长尾术语增强（利用 LLM 扩展知识分类体系，构造同音词/罕见字/缩写/产品 ID 的合成语料，仅保留发音与目标文本一致的样本）；短句 + 长伪标注录音融合，采用 ROVER 投票对齐与一致性过滤，LLM 恢复标点。

## 三、实验结果（Experimental Results）
**音频理解（越高越好）**
- MMSU：**90.6**（对比 Doubao 2.0 Lite 80.0、Gemini 3 Flash 77.0、Gemini 3.1 Pro 83.6）
- MMAR：**86.5**（Doubao 2.0 Lite 75.9、Gemini 3 Flash 75.4、Gemini 3.1 Pro 81.7）
- AudioMultiChallenge：49.3（Gemini 3 Flash 56.6、Gemini 3.1 Pro 67.0），存在差距

**交互智能**
- AA Full-Duplex Bench Overall：**98.9**（GPT-realtime-2 High 95.3、Qwen Audio 3.0 Realtime Plus 98.4、Grok Voice Think Fast 2.0 high 95.1）
- StepAudioChat 对话（实时模式）：70.4，与 Doubao 2.0 Lite（Reasoning）70.5、DeepSeek-V4-Flash 71.4 相当；推理模式下宏观平均达 **73.0**
- τ-Voice（Agentic）：56.0% 宏观任务成功率（Grok Voice Think Fast 2.0 High 56.5、Qwen Audio 3.0 Realtime Plus 54.6、GPT-Realtime-2.1 High 45.7）

**通用文本**：HMMT 2026 Feb 86.8、GPQA Diamond 83.0、MultiChallenge 59.7（多轮约束遵循仍是短板）

**ASR（错误率越低越好，StepAudio 3 ASR Max）**：LibriSpeech test-clean 1.18 / test-other 2.28、AISHELL-1 0.49、WenetSpeech test-net 3.99 / test-meeting 4.35，并在 ContextASR-Bench 上全面领先（如 ContextASR-Dialogue-ZH 1.02 vs Doubao 2.0 10.47）。

论文也坦诚指出剩余差距：多轮约束遵循与零售类工具使用任务仍有提升空间。

## 四、一句话评价
StepAudio 3 Realtime 以「边想边说 + 无缝双工 + 流式语音 Agent」的组合拳，在几乎不牺牲实时性的前提下把语音对话、深度推理与工具执行统一进一个连续循环，其中 MMSU 90.6 与全双工 98.9 的分数证明了其在音频理解与自然轮次管理上的顶尖水准，但多轮约束遵循与领域工具任务仍是明显的待补短板。

---

## 41. DiTAR+: Dual Optimization for Robust Autoregressive Diffusion Speech Synthesis

**作者**: Ziyu Zhang, Tianlun Zuo, Hanzhao Li, Haoyu Zhang, Lei Xie
**链接**: [2609.13909](https://arxiv.org/abs/2609.13909)
**分类**: Text-to-Speech (Zero-Shot Speech Synthesis / Autoregressive Diffusion Speech Synthesis) | **关键词**: AR-DiT, Continuous-Latent Modeling, Zero-Shot Speech Synthesis, Dilated Context Sampling, Hierarchical Acoustic Masking

### 核心痛点
- 连续隐变量自回归扩散 Transformer（AR-DiT）在零样本语音生成中表现强，但长句/复杂语言结构下解码稳定性不足。
- 历史感受野受限：LocDiT 主要依赖紧邻的前一个 patch 作为声学 pre-context，长语音中远端说话人和韵律信息不可见，导致误差累积与说话人漂移。
- 声学惯性依赖：迭代去噪时浅层过度依赖局部声学 pre-context，倾向复制/延续前文声学模式，弱化上游语言模型的语义条件，导致重复、漏读、错读、循环退化；更丰富历史还会加剧该问题。

### 方法创新
提出 DiTAR+ 双优化框架：
1. **Dilated Context Sampling (DCS)**：在自回归前端，不改变语音隐序列物理时序，保留紧邻局部上下文窗口 `[P_{i-c},...,P_{i-1}]` 以平滑边界，同时以固定膨胀步长 `j` 稀疏采样远端历史 patch `[P_{i-nj},...,P_{i-j}]`，拼接为条件 `C_i`。在不增加显著计算成本下扩大宏观历史感受野，缓解长程误差传播。
2. **Hierarchical Acoustic Masking (HAM)**：在扩散后端，LocDiT 浅层（前 `N1` 层）屏蔽对历史声学 pre-context 的注意力，迫使模型先基于语言条件建立语义对齐；深层再恢复历史声学上下文，用于说话人一致且平滑的声学渲染。该分层设计显式解耦语义对齐与声学细节重建。

### 实验结果
- 在语言挑战性强的 ZH-Hard 集上，词错误率（WER）从 12.478% 降至 9.893%。
- 在 25–35 秒扩展长语音上，说话人相似度从 0.741 提升至 0.759，同时 WER 从 2.778% 降至 2.173%。
- 有效缓解发音错误和语义幻觉，增强困难句子的生成鲁棒性，并在长语音全程保持较高说话人相似度；优于离散 token 与纯 flow-matching 基线。

### 一句话评价
DiTAR+ 通过前端膨胀上下文采样扩大历史感受野、后端分层声学掩码抑制声学捷径，在几乎不破坏时序连续性的前提下显著提升了连续隐变量 AR-DiT 的零样本长语音合成鲁棒性。

---

## 42. Musical Timing in Studio Recordings

**作者**: Konstantinos Tsioutas, George Xylomenos
**链接**: [2609.13881](https://arxiv.org/abs/2609.13881)
**分类**: Music Information Retrieval | **关键词**: Musical Timing, Studio Recordings, Sound Leakage Detection, Multitrack Analysis, Musical Synchronization, Overdubbing

# 论文总结

## 核心痛点
录音室录制技术差异很大，从同一声学空间中的现场合录，到隔离录音棚录音和叠录（overdubbing）——音乐家分开录制各自声部，并监听已录制的素材。这些方式在物理共处、视觉接触、声音泄漏和声学隔离方面不同，可能影响音乐家之间的协调。本文关注：录音方式是否影响时间精度，尤其是音乐家在同一空间共同演奏是否能获得更紧密的时间协调。现有可用多轨录音往往缺少录制条件文档，因此需要从音频本身推断录制方式。

## 方法创新
1. **两个多轨数据集**：共分析 391 首多轨录音，其中 Cambridge 数据集 369 首，Telefunken 数据集 22 首（Telefunken 为录音室多轨录音）。
2. **自动声音泄漏检测**：计算同一录音内各音轨之间的成对 Mel 频谱相似度，并利用相似度矩阵的汇总统计量来识别具有共享声学内容/声音泄漏的录音，从而推断录制条件。
3. **多角度音轨相似性分析**：论文提到使用两种方法分析各轨相似性，即振幅相似度和频谱相似度。
4. **时间关系度量**：基于多轨录音测量音乐家之间的时间关系（与相关工作中的 Δt/同步误差概念一致），以时间变异性衡量协调程度。
5. **录制方式分类**：将制作分为（a）现场录制、所有音乐家同处一室并共享声学空间（有漏音）；（b）同处一室但通过近距拾音/DI 盒隔离录制（无漏音）；（c）现场共同演奏但处于不同隔离棚（无漏音）；（d）逐轨单独录制/叠录（无漏音）。由于缺少录制元数据，主要利用声音泄漏区分（a）与（b）（c）（d）。

## 实验结果
- 表现出共享房间声学和声音泄漏证据的录音，其音乐家之间的时间变异性通常低于高度隔离的录音。
- 叠录（overdubbing）与时间变异性增加相关。
- 总体结论：在具有物理共处证据的录音中，音乐家之间的时间变异性显著降低；在可能为叠录的情况下，时间变异性增加。

## 一句话评价
该文通过多轨音频的声音泄漏自动检测与时间变异性分析，为“录音方式与物理共处是否影响音乐时间同步”提供了数据驱动的实证证据，但受限于录制条件元数据缺失，只能间接推断录制方式。

---

## 43. CRAF: Cross-View Residual-Aware Fusion for Deepfake Speech Detection

**作者**: Minh-Xuan Phan, Khalid Zaman, Candy Olivia Mawalim, Masashi Unoki
**链接**: [2609.13842](https://arxiv.org/abs/2609.13842)
**分类**: Deepfake Speech Detection | **关键词**: Deepfake Speech Detection, Speech Anti-Spoofing, Cross-View Fusion, Self-Supervised Learning, Auditory Large Language Model, Residual Learning, ASVspoof 5

# CRAF: Cross-View Residual-Aware Fusion for Deepfake Speech Detection

## 核心痛点
- 语音合成与语音转换使深度伪造语音越来越逼真，检测器对未见攻击、录音条件和数据集的泛化仍然困难。
- 自监督学习（SSL）模型擅长细粒度、低层声学特征；听觉大语言模型（ALLM）提供更高层的语义与上下文表示。两者具有互补性。
- 直接拼接或直接融合 SSL 与 ALLM 表示会平等对待两个视图，无法区分共享信息与 SSL 特有的互补信息，可能引入冗余并削弱对细粒度声学线索的利用。
- 因此核心问题不是简单组合 SSL 和 ALLM，而是在引入高层语义指导的同时，保留 SSL 中用于欺骗检测的细粒度互补信息。

## 方法创新
- 提出 CRAF（Cross-View Residual-Aware Fusion）框架，采用非对称设计：SSL 作为主表示，ALLM 作为高层指导。
- ALLM-guided cross-view attention：以 SSL token 作为 query，ALLM token 作为 key/value，得到 ALLM-guided SSL 表示，在保留 SSL 时间分辨率的同时注入上下文信息。
- ALLM-guided residual learning：使用独立参数化的 reference estimator，以 SSL 为 query、ALLM 为 key/value，估计 ALLM 条件下可解释的 SSL reference；再通过跨视图残差 D = LN(S - S_hat) 分离出 ALLM 难以解释的 SSL 互补信息。
- Residual gating：基于原始 SSL、估计 reference 和残差的拼接，通过 sigmoid 门控与 refinement 网络选择性保留检测相关残差。
- SSL-primary adaptive fusion：计算融合权重，最终表示 Z = S + Dropout(G_f ⊙ (R + λS_g))，以残差路径显式保留原始 SSL，同时自适应注入 guided SSL 与 refined residual。
- 后端使用 AASIST-style 分类器，训练目标为加权交叉熵 + label smoothing；预训练 SSL 与 ALLM 编码器冻结，其余模块联合优化。

## 实验结果
- 数据集：ASVspoof 5，Track 1 open condition；评价指标：EER 与 minDCF。
- 编码器：XLS-R 300M 作为 SSL；Step-Audio 2、Qwen-Audio、Kimi-Audio 作为 ALLM。
- 主结果：CRAF (Kimi-Audio) 在 evaluation 上达到 EER 5.96%、minDCF 0.1192，development EER 2.41%，优于对应单编码器基线 Kimi-Audio + AASIST 和 XLS-R + AASIST，也优于文中列出的多个近期单系统方法，如 ASTDT（6.94%）、ProSDD（7.38%）、Fused SSL + NeXt-TDNN（7.23%）等。
- 不同 ALLM 上均有提升，说明 CRAF 的有效性不依赖特定 ALLM，而来自跨视图交互与残差感知融合。
- 消融研究：cross-view attention、residual learning、SSL-primary fusion 各自均有贡献；Kimi-Audio 下完整 CRAF 最佳，w/o Residual Gating 为 EER 6.69%、minDCF 0.1335。
- 攻击类型分析显示 CRAF 相对单编码器基线在未见攻击条件下更稳健。

## 一句话评价
CRAF 通过非对称的 SSL-ALLM 跨视图残差感知融合，有效分离并利用 SSL 细粒度互补信息，在 ASVspoof 5 上取得有竞争力的未见攻击泛化性能，但验证仍主要局限于单一数据集与单系统设定。

---

## 44. Realtime-Venus: A full-duplex interaction system with asynchronous delegation

**作者**: Ruixiang Zhao, Hualei Wang, Renhe Sun, Enzhi Zhou, Jincenzi Wu, Xujie Song, Kexin Shi, Zihang Liu, Pengcheng Zhu, Jiayi Zhou, Baoyue Zhang, Changhao Zhang, Zitong Wang, Jinhong Wang, Tong Niu, Jingjing Liu, Junan Lin, Haolin He, Hengshuo Chu, Yuhui Chen, Jian Liu, Yuge Huang, Junliang Xing, Yuntao Wang, Weiqiang Wang, Chun Yu, Yuanchun Shi
**链接**: [2609.13814](https://arxiv.org/abs/2609.13814)
**分类**: Full-Duplex Multimodal Dialogue Systems | **关键词**: Full-Duplex Interaction, Asynchronous Delegation, Audio-Visual Interaction, Spoken Dialogue, Proactive Interaction, Tool Use

# Realtime-Venus 论文总结

## 核心痛点
- 数字与物理环境中的自然交互需要持续感知和及时响应：语音对话依赖声学与语言线索，视频交互还需将对话落地到不断演化的视觉上下文中。
- 连续交互与外部计算的时间尺度不同：后台任务需要一个稳定的请求记录和支撑证据，但结果必须在可能已经改变的对话中重新解释；如何协调“任务捕获”与“对话内结果交付”是保持交互连贯性的关键。
- 现有 omni / full-duplex 模型更多关注模态覆盖与流式输出，缺乏把对话控制、响应生成、私有异步委托统一到共享策略和共享因果时间线中的系统设计，也缺少对工具/推理后台执行与前台对话并行的运行时支持。

## 方法创新
- 提出 Realtime-Venus，一个主动式全双工交互系统，包含两个分别训练的 9B 模型：Realtime-Venus-Omni 面向音视频交互，Realtime-Venus-Audio 面向语音对话。
- 每个模型都是完整的对话前端，集成连续感知、对话控制和原生语音生成，并通过统一流式建模把用户输入、模型输出、私有委托请求、后台结果对齐到共享因果时间线。
- 前端联合预测交互控制 token、响应文本和委托请求；共享策略支持在用户 backchannel 时维持响应、在用户纠正后修改未说出的续写、在请求需要外部能力时启动后台工作。
- 提出 Realtime-Venus-Harness：共享的异步能力执行与结果交付框架。在双循环运行时中，前端维持实时交互，Harness 在后台管理委托工作；每个委托请求绑定到原会话，并携带请求开始时的证据快照。
- 框架将任务路由到已注册能力异步执行，并将符合条件的结果作为私有上下文返回；通过 freshness check 判断结果是否仍有效，通过 playback-aware delivery 决定结果何时重新进入对话。前端再结合当前对话解释返回信息并决定面向用户的响应。
- 训练侧提出统一数据管线：场景规划、语音实现、时间对齐；覆盖 duplex 场景（backchannels、other-directed speech、需要停止/修复/重定向的中断）、主动轨迹（何时发起响应、何时继续倾听）以及委托场景（私有请求、后台执行、返回信息和后续响应）。
- 后训练配方混合离线理解、主动全双工轨迹和委托工作流；Realtime-Venus-Omni 使用音视频与纯音频数据，Realtime-Venus-Audio 使用纯音频子集。
- 声称 Realtime-Venus-Omni 是首个支持异步后端调用进行推理和工具执行、同时保持视频交互的全双工 omni 模型；结合记忆增强还支持小时级视频理解。

## 实验结果
- 视频理解：在被评估的在线模型中，Realtime-Venus-Omni 在 8 个视频基准中的 6 个取得最高分，包括 StreamingBench 70.2%、OVO-Bench 64.7%、Daily-Omni 81.3%。
- 音频理解与语音问答：Realtime-Venus-Audio 在 MMAU 78.0%、MMAU-Pro 63.2%、Llama Questions 83.8%、Speech CMMLU 67.8% 等基准上领先，并在 VoiceBench AlpacaEval 上达到匹配最佳水平的 4.81。
- Full-Duplex-Bench v1.5：Realtime-Venus-Audio 对 75% 的用户打断做出响应；在 backchannels、other-directed speech、background speech 三种场景下的 continuation rate 分别为 97%、88%、86%，在三项 continuation 指标上均超过 Gemini 3.1 Live 和 GPT-4o。
- 同时论文还补充了工具使用和委托决策评估，用于区分“正确路由”与“成功完成任务”，并指出在对话过程中执行外部工作仍存在挑战。

## 一句话评价
Realtime-Venus 通过共享因果时间线和双循环运行时，把全双工对话控制、响应生成与异步后台委托/工具执行统一起来，并在多项视频、音频和全双工基准上取得领先，是迈向实时主动多模态代理的重要系统工作。

---

## 45. The VoiceMOS Challenge 2026: Evaluating Speech Enhancement, Emotional TTS and Accented TTS Systems

**作者**: Wen-Chin Huang, Wei Wang, Marvin Sach, Xiaoxue Gao, Nicholas Sanders, Erica Cooper, Toda Tomoki
**链接**: [2609.13792](https://arxiv.org/abs/2609.13792)
**分类**: Speech Quality Assessment (MOS Prediction) | **关键词**: VoiceMOS Challenge, Mean Opinion Score (MOS), Speech Quality Assessment, Speech Enhancement, Emotional Text-to-Speech, Codec-based Speech Synthesis, ACR/CCR, Accent Similarity

## The VoiceMOS Challenge 2026 论文总结

### 一、核心痛点（Motivation）
- **人工主观评测成本高昂**：MOS（Mean Opinion Score）听力测试被公认为语音质量评估的“金标准”，但耗时、昂贵、难以大规模复现。
- **语音领域的问题尚未解决**：VoiceMOS Challenge（VMC）自 2022 年创办，历经四届，2025 年一度扩展为 AudioMOS Challenge（AMC），把范围扩到音乐与通用音频。但社区反馈表明**语音评测中的核心问题依然悬而未决**，因此 2026 年决定回归 VMC，重新聚焦语音。
- **评测维度日趋复杂**：从 in-domain 到 zero-shot、从英语到多语种、从单轴到多维、从 TTS 到噪声/增强语音乃至歌声，需要标准化数据集与统一赛道来横向比较自动预测技术。

### 二、挑战赛设计与方法创新（Methodology / Organization）
本届挑战赛于 **2026 年 5 月 20 日至 8 月 10 日**在 CodaBench 平台举行，共设 **三条赛道**，参赛队伍需提交系统说明与反馈问卷。

**Track 1：语音增强系统的 ACR / CCR 预测**
- 数据源自 **URGENT 2026 语音增强挑战赛**，包含 6 个增强系统在 **840 条源语音、9 种语言**上的输出，源语音含真实录制与模拟噪声两类。
- 每个样本有 6 个增强结果用于 ACR；CCR 则包含全部 **15 组两两系统比较**。
- ACR：五级量表打 MOS；CCR：−3 到 +3 的偏好比较得到 CMOS（正值表示偏好第一个样本）。每样本/对通常 8 个评分。
- 训练/开发/测试在说话人与源语音上完全不重叠。开发集：168 源语句、1008 ACR、2520 CCR 对；测试集：672 源语句、4032 ACR、10080 CCR 对。

**Track 2：情感 TTS 的自然度与情感相似度 MOS 预测**
- 数据覆盖 **5 类情感**（neutral, happy, sad, angry, surprised）、**13 个合成系统**，句子与自然参考音频来自 **ESD** 与 **DailyTalk**。
- 每样本 4–9 位听者，除必选的 **QMOS**（发音/语调/信号质量）与 **EMOS**（与真实情感标签的匹配度）外，还有可选的**情感类别多选**与 **Valence/Arousal/Dominance（V/A/D）** 评分。
- 规模：训练 12746 / 开发 2730 / 测试 2730 样本，系统数 10/13/14。

**Track 3：基于 Codec 的语音合成系统的说话人与口音相似度 MOS 预测**
- 基于 **CodecMOS-Accent** 数据集，共 4000 样本、24 个当代 codec 重合成与 TTS 系统、32 位说话人、10 种口音。
- 给定输入语音与参考语音，需预测 **SPK**（说话人）与/或 **ACC**（口音）相似度分数。开发/测试集包含训练中未见过的系统，考验泛化能力。
- 规模：训练 2800 / 开发 600 / 测试 600，系统数 21/23/25，每样本约 4.9 个评分。

### 三、基线系统（Baselines）
- **Track 1 – B01：UrgentMOS**，统一非侵入式语音质量评估模型，同时支持绝对与比较质量预测；使用公开的 `urgent-mos-f1c1m5dcorpus` checkpoint，特征编码器为 **WavLM**，在多语音质量语料上训练；ACR 单样本预测 MOS，CCR 用偏好模块直接由样本对预测 CMOS，**不做微调**。
- **Track 2 – B02：按问题类型分别建模**。QMOS 用 **UTokyo SaruLab UTMOS**；EMOS 与 V/A/D 用 **Gemini LLM-as-judge**（`gemini-3-flash-preview`，prompt 与人类听者指令一致）；情感类别用 **Emotion2vec+ large** 的类别预测概率。全部为 **zero-shot，无微调**。
- **Track 3 – 两个基线**：B03-1 为 zero-shot，直接用预训练 **ECAPA-TDNN** 说话人嵌入的余弦相似度作为 SPK 与 ACC 分数；B03-2 在训练集上微调 ECAPA-TDNN，SPK 与 ACC 各训一个模型，batch size 16、AdamW、lr 0.001、固定 20000 步。

### 四、参赛情况与实验结果（Results）
**参赛规模**：共 **18 支唯一团队**提交评测结果（Track 1/2/3 分别为 4/8/7 支），其中 15 支来自学术界、2 支来自工业界、1 支身份未知；地域覆盖德国、日本、韩国、台湾、法国、中国、印度、美国、巴西、西班牙、加拿大等，仅一支队伍同时参加两条赛道。

**Track 1（指标：ACR-UTT-SRCC / CCR-UTT-SRCC）**
- **所有参赛队均超过基线**；ACR 第一名为 **T09（0.779）**，CCR 第一名为 **T01（0.487）**。
- 关键发现：**CCR 明显比 ACR 更难预测**（0.487 vs 0.779）。图 2 显示，随着真实 |CCR| 增大（即两样本感知差异更明显），**符号准确率（sign accuracy）单调上升**，说明系统在差异大时更容易判对偏好方向。

**Track 2（指标：QMOS-UTT-SRCC / EMOS-UTT-SRCC）**
- 多数队伍超过基线；顶尖系统 QMOS 达 **0.785**、EMOS 达 **0.758**，说明 **EMOS 并不必然比 QMOS 更难预测**。
- 除 T13 与 T18 外，其余队伍均参加可选的类别选择与 V/A/D 子任务，且在 utterance 级指标上**稳健超越基线**（图 3，CAT-ERR 为类别预测误差，越低越好）。

**Track 3**：结果以 SPK-UTT-SRCC 与 ACC-UTT-SRCC 呈现（图 1c），包含 B03-1/B03-2 两个基线以及 T04、T06、T07、T15、T16、T17、T13 等队伍；注意 T13 仅提交了 ACC 结果。

**总体结论**：各赛道基线基本都被多数参赛队伍超越，体现出相较基线的实质性进步；参与者问卷还帮助识别了顶尖系统的有效技术手段，以及社区直接提出的未来方向。

### 五、一句话评价
本文是一篇挑战赛综述型论文，通过 ACR/CCR 语音增强、情感 TTS（QMOS/EMOS/V/A/D/类别）、Codec 口音 TTS（SPK/ACC）三条赛道的标准化评测，系统刻画了当前 MOS 自动预测的能力边界——绝对质量已可较好预测，而**比较式偏好（CCR）与细粒度情感/口音相似度仍是开放难题**。

---

## 46. UniqueShip: Mitigating Data Leakage in Acoustic Ship Classification Benchmark Datasets

**作者**: Connor Hashemi, Trevor Stout, Anthony Hoogs, Jason Parham
**链接**: [2609.13659](https://arxiv.org/abs/2609.13659)
**分类**: Underwater Acoustic Target Recognition | **关键词**: UniqueShip, Underwater Acoustic Target Recognition, Ship Classification, Data Leakage, Benchmark Dataset, Maritime Acoustics

## 核心痛点
- 水下声学目标识别（UATR）的船舶分类缺乏大规模、多样、公开标注数据集；现有 DeepShip、VTUAD、Oceanship 等数据量和样本多样性不足，模型泛化差。
- 更严重的是数据泄漏：连续水声记录具有强时空自相似性，单船签名持续存在。常规按文件或短片段随机划分 train/test 会让同一船或相邻背景同时出现在训练和测试中，模型可记忆单船特征而非学习类别，导致测试准确率虚高、评估不可靠。

## 方法创新
- 提出 UniqueShip：源自 Ocean Networks Canada（ONC）开放仓库的 UATR 基准数据集，覆盖 2016-05 至 2023-11 的 7 个 deployments，使用两个 icListen AF 水听器（32 kHz 采样，约 100 m 深）。
- 处理流程：修改既有开源 pipeline，采用 2 km 单船 inclusion radius 与 8 km exclusion radius 判定背景；重采样至 20 kHz，切成 5 秒样本。
- 严格防泄漏划分：按船舶 MMSI 分组，保证同一船不跨 train/val/test；背景按天分组；提供显式 80/10/10 划分并重复 5 次。
- 数据规模：2,460 小时船舶辐射音频 + 977 小时背景，共 4,218 艘独特船舶、11 个船舶类 + 1 个背景类、2,779 天、近 250 万个 5 秒样本。发布数据集、代码与易下载 splits 于 uniqueshipdata.org。
- 提供多种 splits：5 Class Balanced、5 Class 5h Each、12 Class 5h Each、5 Class All Data、All 等；重点基准为 5 Class Balanced（背景、拖船、油轮、货船、客船等时长）。

## 实验结果
- 在 DeepShip 和 VTUAD 上复现发现：常规随机划分相比按 MMSI 的谨慎划分，测试准确率虚高 10–48 个百分点，证实数据泄漏会严重高估性能。
- UniqueShip 消融：独特船舶数量翻倍带来 2.4–2.6 个百分点准确率提升；总音频时长翻倍仅提升 0.8–1.3 个百分点。说明船舶多样性比总小时数更重要，数据集构建应以多样性驱动。
- 提供卷积和 transformer backbone（如 Swin）基线；元数据分析表明，个体船舶特征/物理元数据比仅到水听器距离更能预测分类难度。

## 一句话评价
UniqueShip 通过按 MMSI 与按天分组严格消除数据泄漏，构建了当前最大开源 UATR 基准之一，并用实验证明现有基准的随机划分可导致 10–48 个百分点虚高，强调船舶多样性应优先于音频总时长。

---

## 47. Predictive audio representations for early detection and tracking of hidden dynamic objects

**作者**: Katerina Vinciguerra, Moritz Brandes, Danilo Hollosi, Letizia Marchegiani
**链接**: [2609.13595](https://arxiv.org/abs/2609.13595)
**分类**: Audio Perception for Autonomous Driving | **关键词**: Acoustic NLOS perception, Self-supervised audio representation, JEPA, Multi-task learning, Direction of arrival, Vehicle classification, Microphone array, Raw waveform

## 核心痛点
- 自动驾驶安全需要预见尚未可见的交通参与者；被遮挡目标可能过晚进入视野，导致系统没有足够时间感知、规划与安全响应。
- 摄像头和 LiDAR 依赖视线；雷达虽可穿透部分非导电材料，但无法穿透金属车身，仍受限于视野。
- 声音全向传播并编码空间信息，可绕过障碍物，在 T 字路口等非视距场景中具有重要价值。
- 已有声学工作多只处理单车场景，且通常只估计到达方向或车辆类型；声学交通监控系统多部署在固定路侧、分钟级输出，不能直接用于车载实时决策。
- 多车同时存在的 NLOS 场景还面临声源分离困难，检测和解析多个同时频谱特征仍是开放问题。

## 方法创新
- 提出两阶段车载声学感知框架：JEPA 启发的自监督预训练 + 监督多任务微调。
- 自监督预训练直接作用于 8 通道原始波形，无需频谱变换；在线编码器 fθ 与 EMA 目标编码器 fθ_bar 配合，轻量 MLP predictor 从过去帧 x_{n-2} 预测未来帧 x_n 的潜在表示，并刻意排除中间帧 x_{n-1}，迫使模型学习更长程声学动态。
- 编码器由 3 个 strided 1D 卷积块（kernel 9、stride 2，通道 64/128/256）+ BatchNorm + ReLU + 全局平均池化 + 线性投影组成，潜空间维度 D=256。
- 微调阶段使用 3 秒窗口，逐帧编码后由单层双向 LSTM（每方向 H=128，拼接后 256）聚合，再经共享 MLP 映射到 128 维并施加 dropout 0.4，最后接三个分类头：方向 5 类（left, front, right, none, both/back）、数量 3 类（0,1,2）、类型 4 类（car, van, car+van, none）。
- 总损失为方向、数量、类型三个交叉熵损失的加权和，方向损失权重 λ=5；微调先冻结编码器 warm-up 5 个 epoch，再联合优化，编码器学习率 1e-5，头学习率 1e-3，共训练 20 个 epoch。
- 贡献点：首个车载声学系统同时估计多个 NLOS 车辆的方向、数量和类型，具备 1 秒延迟；并证明 JEPA 式原始波形时序预测可学到比监督模型更好的可迁移表示。

## 实验结果
- 因无合适公开数据集，作者自建 NLOS 多交通代理同时出现的数据集：三台 MER2-503-36U3C 相机安装在车顶，正下方为八边形 8 麦克风阵列，并配有 GPS。
- 实验 1：多任务模型与当前最优方法比较，结果显示优于 SOTA。
- 实验 2：通过消融研究验证设计选择的合理性。
- 实验 3：验证模型可泛化到未见且显著不同的驾驶场景，并保持合理且稳定的性能。
- 片段未给出具体数值结果，但明确指出自监督预训练表示稳健、可迁移，且方法不依赖声源分离，可处理最多 2 辆车同时出现的情形，作为多车场景 proof-of-concept 基线。

## 一句话评价
该工作将 JEPA 式自监督音频表示学习引入车载多任务声学 NLOS 感知，在自建多车数据集上同时实现方向、数量与类型估计，展示了原始波形预训练在自动驾驶声学感知中的潜力和跨场景泛化能力。

---

## 48. CVSS-X: A Multilingual Speech-to-Speech Translation Corpus for 28 Languages

**作者**: Lucas Rafael Stefanel Gris, Alef Iury Siqueira Ferreira, Frederico Santos de Oliveira, Augusto Seben da Rosa, Alexandre Costa Ferro Filho, Arlindo Rodrigues Galvão Filho, Anderson da Silva Soares
**链接**: [2609.13413](https://arxiv.org/abs/2609.13413)
**分类**: Speech-to-Speech Translation | **关键词**: Speech-to-Speech Translation, Multilingual Speech Corpus, Voice Cloning, Text-to-Speech, Synthetic Speech Data

# CVSS-X: A Multilingual Speech-to-Speech Translation Corpus for 28 Languages

## 核心痛点
- 语音到语音翻译（S2ST）依赖大规模平行语音语料，但这类语料仍然稀缺，收集对齐话语成本极高。
- CVSS 是首个大规模公开 S2ST 语料，但只支持 21 种源语言到英语的多对一（X→EN）翻译，限制了英语→X 以及非英语语言对的研究。
- SpeechMatrix 规模大（418K 小时），但仅覆盖 17 种欧洲语言，自动挖掘对齐质量近似；SeamlessAlign 覆盖 37 种语言，但只公开元数据，需要从 Common Crawl 重建。
- 因此，需要一种可完全下载、方向互补、覆盖多语言、具备句级精确对齐的 S2ST 语料。

## 方法创新
- 提出 CVSS-X，逆转 CVSS 的翻译方向，实现英语→28 种目标语言（EN→X）的大规模合成 S2ST 语料，覆盖 12 个语系、归并为 7 个宏观类别。
- 数据来源：使用 Common Voice v17 英语源语音，并通过归一化文本匹配与 CVSS/CoVoST 2 使用的 Common Voice v4 对齐，恢复 240,192/264,037（91.0%）原始英语话语；dev 因匹配样本仅 871 条，从训练集随机补充至 10,000 条。最终每目标语言划分为 train 222,349、dev 10,000、test 7,843。
- 文本翻译：使用蒸馏 NLLB-200（600M），在闭集评测中对比 7 个候选翻译模型，并通过 LLM-as-a-judge 对 100 个 EN→PT 样本按准确性、流畅性、术语保持进行 1–10 分评分后选定。
- 语音合成：使用 OmniVoice，一个 SOTA 多语言 TTS 系统，具备零样本跨语言语音克隆能力。
- 两个变体：
  - CVSS-X-C（Canonical）：每语言两个固定参考音色（男/女），由 ElevenLabs voice design 生成，中性口音；按源说话人性别选择，男 81.4%、女 18.6%，音色多样性相比 CVSS-C 单音色翻倍。
  - CVSS-X-T（Transferred/Timbre-transferred）：以源英语音频为条件进行零样本语音克隆，保留说话人特征；约 3.4% 样本因信号不足被跳过。
- 规模：约 240,000 个平行语音对/语言；总翻译对 6,725,376；CVSS-X-C 约 6,730 小时，CVSS-X-T 约 9,340 小时，总计约 16,070 小时，是 CVSS 的 8 倍。与 CVSS 结合可支持双向翻译，并以英语为枢轴实现任意 X→Y 翻译。

## 实验结果
- 评估设置：每语言从 dev 集分层随机抽样 200 条（每变体 5,600 条），经 power analysis 确定样本量；使用 Whisper large-v3 ASR 计算 WER/CER 和 ASR-BLEU（TTS-to-ASR 往返保真度），UTMOS 评估自然度，ECAPA-TDNN 评估说话人相似度；对 CVSS 用相同模型和样本量重新评估。
- 总体对比：
  - CVSS-X-C：UTMOS 3.55，ASR-BLEU 82.4，WER/CER 12.1%。
  - CVSS-X-T：UTMOS 3.21，ASR-BLEU 79.4，WER/CER 14.1%，说话人相似度 0.607。
  - CVSS-C：UTMOS 4.43，ASR-BLEU 94.2，WER/CER 3.5%；CVSS-T：UTMOS 3.61，ASR-BLEU 93.8，WER/CER 4.0%。
- 按语系：Romance 和 Slavic 表现最好（ASR-BLEU 88–90，WER 低于 8%）；Indo-Iranian 和 Other 较低（60–65），主要受非拉丁文字（希伯来语 ASR-BLEU=46.1）和泰语声调影响。使用语言特定分词器后，泰语 word-tokenized BLEU 为 49.1(C)/47.8(T)，中文为 87.6/70.4，日文为 88.9/85.7。Other 家族 WER 24.8%，主要由泰语 77.0% 和希伯来语 37.4% 驱动。
- 分析：CVSS-X-C 的 UTMOS 低于 CVSS-C，原因是 CVSS 仅合成英语且使用高质量 LibriTTS 训练的 PnG NAT，而 CVSS-X 用单一多语言模型合成 28 种类型学差异大的语言；OmniVoice 质量在各语系较均匀（3.48–3.62）。语音克隆质量良好但自然度略降，日耳曼语系相似度 0.648 高于斯拉夫语系 0.567，可能与英语语音接近性有关。

## 一句话评价
CVSS-X 通过反向扩展 CVSS 构建了目前规模最大、可完全下载的英语→28 语种合成 S2ST 语料，显著提升多语言和双向语音翻译的数据覆盖；尽管合成自然度不及 CVSS 且翻译质量受 NLLB-200 限制，但它为更包容的多语言 S2ST 研究提供了重要基础设施。

---

## 49. ScorePrompts: Natural-Language Exploration of Symbolic Music Scores through Analysis

**作者**: Emmanouil Karystinaios, Gerhard Widmer
**链接**: [2609.13291](https://arxiv.org/abs/2609.13291)
**分类**: Music Information Retrieval (Symbolic Music Analysis) | **关键词**: symbolic music, MusicXML, music information retrieval, natural language generation, score analysis, large language models

# ScorePrompts: Natural-Language Exploration of Symbolic Music Scores through Analysis

## 核心痛点
- 符号乐谱（尤其是 MusicXML）中蕴含音高拼写、同时性、声部、拍号与曲式结构等丰富信息，但一旦被展平为 token 序列或暴露为原始 XML，这些关系就容易被遮蔽，用户难以阅读和检索。
- 单纯依赖 LLM 直接从乐谱标记推断音乐结构不可靠：缺少可追溯的证据，容易产生幻觉，且用户无法检查中间分析结果与不同分析层级之间的冲突。
- 现有自然语言音乐接口常把分析过程隐藏在自由文本回答背后，无法让用户核验“这句话对应乐谱的哪些小节、哪些分析层”。

## 方法创新
- **先分析、后生成（analyze-before-generating）**：不把记谱标记直接交给语言模型，而是先用 MIR 模型和确定性描述子构建类型化、与乐谱对齐的表示，再让语言生成与问答在此基础上进行，同时保留中间分析可检查。
- **专家分析与证据对齐**：Partitura 读入 MusicXML；AnalysisGNN 估计和声、调性、终止式、乐句、段落与音符级角色；确定性后处理重建罗马数字并聚合到节拍/小节级；AlgoMus 织体描述子、jSymbolic 风格特征（经 music21 计算）与乐谱元数据提供互补上下文。音符/节拍/小节/乐曲四级视图通过小节引用与音符 ID 对齐，整首乐谱表示为带字段定义、类别码本和局部分析行的交叠小节块序列，并维护乐曲级证据索引以支持全局轨迹访问。
- **受 schema 约束的语言生成**：将分析行转化为规范小节事实，与乐曲级轨迹组织成三种技术细化度递增的描述；每个块可独立编译并并入乐曲级计划；语言阶段产生的引用会与证据索引核对，格式异常则重试或回退为确定性摘要；语言组件模型无关、无需音乐专门微调。
- **确定性乐谱问答**：支持的问题绕过额外 LLM 调用，由确定性路由器解析显式小节/范围以及和声、终止式、曲式等术语，从完整块索引中选择相关字段，必要时加入节拍/音符级行；回答分为简洁结论、引用小节、支撑层、注意事项和结构化分析引用，并主动暴露分析层级间的分歧。
- **记谱关联检查**：保留原始记谱，用 Verovio 渲染并叠加重建罗马数字标签；选中音符即可看到与证据索引一致的标识符、音高、时序、和声与结构标签及置信度，形成从自然语言解释回到乐谱区域的闭环。

## 实验结果
- 本文为 Late-Breaking Demo 扩展摘要，**未报告用户研究或定量实验**。
- 演示页 https://hf.co/spaces/manoskary/scoreprompts 展示完整流程：上传乐谱 → 分析 → 自然语言描述 → 定向提问（如“What changes in measures 14–18?”）→ 在五线谱中检查被引用小节与音符属性。
- 界面可对比音符、节拍、小节、乐曲级表格，支持下载 CSV 及全局 JSON 摘要；分析中的缺失与冲突信息会被显式报告而非隐藏。

## 局限与未来方向
- 受限范围：仅面向机器可读的西方调性乐谱，继承上游 MIR 组件的曲目与标注假设；系统只做分析解释，不编辑乐谱，且尚未开展用户研究。
- 作者明确不声称每句生成文本都与证据字段语义绑定，也不保证上游预测在音乐学上正确。
- 未来工作包括：陈述忠实性检查、整首乐谱描述聚合、面向问答的 RAG 增强检索以及面向音乐家的任务型评估。

## 一句话评价
ScorePrompts 通过模块化的“先分析、后生成”架构，把可核查的 MIR 分析结果作为证据层，让 LLM 只承担受约束的语言表达，从而为符号乐谱分析提供了一条可追溯、可检查的自然语言交互路径。

---

## 50. From Masking to Merging: Rethinking SpecAugment for Efficient Audio Spectrogram Transformer

**作者**: Minhee Park, Hyowon Ahn, Chanwoo Kim
**链接**: [2609.13260](https://arxiv.org/abs/2609.13260)
**分类**: Audio Classification | **关键词**: SpecAugment, Audio Spectrogram Transformer, Token Merging, Patch Merging, Audio Classification

# 论文总结：From Masking to Merging: Rethinking SpecAugment for Efficient Audio Spectrogram Transformer

## 核心痛点
- AST 等音频频谱图 Transformer 依赖 SpecAugment 等强增强来提升泛化能力，但 SpecAugment 随机遮蔽的时间/频率区域本身语义信息有限。
- 这些被遮蔽区域对应的 embedding token 仍会完整送入 Transformer encoder，带来不必要的计算开销；而 Transformer 自注意力对 token 数量呈二次复杂度。
- 现有 token reduction 方法（如 PaSST 的 Patchout、ToMe/FastAST）通常需要额外模块、相似度计算或随机丢弃，较少直接利用数据增强产生的掩码结构信息。

## 方法创新
- 提出 SpecAugment-Patch Merging：将 SpecAugment 产生的 masked patches 视为 token 合并机会，而不是单纯的信息损失。
- SpecAugment-Patch：在 patch embedding 之前，按 16×16 patch 网格（stride 10）进行时间/频率掩码，使每个 patch 要么完全被掩码、要么完全保留；并用 k_t^max、k_f^max 控制掩码强度，以匹配或略超原 SpecAugment 的最大时间/频率掩码跨度。掩码后生成二值候选矩阵 M，完全零化的 patch 成为合并候选。
- Merging：在 patch embedding 和 positional embedding 之后、Transformer encoder 之前，随机选取 2r 个不同的候选 masked patches，组成 r 个不相交 patch 对；对每对 token 采用 dimension-wise max 合并，合并后的 token 覆盖原位置，另一个位置被移除，最终序列长度减少 r。
- 因为合并发生在位置嵌入之后，剩余 token 仍部分保留时频位置线索；当 r=0 时，方法与原 SpecAugment 的 mAP 和吞吐几乎一致，说明增强效果得以保留。

## 实验结果
- 数据集：AudioSet（balanced training set）、ESC-50、Speech Commands V2；任务涵盖多标签/单标签音频分类与关键词识别。
- AudioSet 上，r 从 0 增加到 100 时，mAP 从 34.07 到 34.08 几乎不变，训练吞吐从 43.3 samples/sec 提升到 49.3 samples/sec，相对提升约 13.9%。
- ESC-50 和 Speech Commands V2 也呈现相似趋势：吞吐随 r 增加稳步提升，准确率仅有微小变化。
- Table 1 显示 r=0 时 SpecAugment-Patch 与原始 SpecAugment 性能接近：mAP 34.07±0.18 vs 34.11±0.35，吞吐均为 43.3 S/s。
- Table 2 在 r=90 下比较 max、mean、sum 合并与随机丢弃，各策略差异较小；最终选择 dimension-wise max，兼顾经验性能与稳定性，并在所有数据集中一致使用。
- 与 PaSST-U 在相同 token reduction ratio 下比较，所提方法实现更高训练吞吐，同时保持有竞争力的准确率，体现了增强感知型 token merging 的效率优势。

## 一句话评价
- 该工作将数据增强产生的掩码区域从“信息损失”重新定义为“可合并冗余”，以极低架构改动实现了 AST 训练效率的稳定提升，是增强感知型 token reduction 的实用方案。

---

## 51. Machine Unlearning for Speech Question Answering in Large Audio-Language Models

**作者**: Zhe Liu
**链接**: [2609.13195](https://arxiv.org/abs/2609.13195)
**分类**: Machine Unlearning for Speech Question Answering | **关键词**: Large Audio-Language Models, Speech Question Answering, Machine Unlearning, Privacy Preservation, Gradient Ascent, Task Arithmetic, Safety Alignment

## 核心痛点
- LALMs 在语音理解与问答上表现强大，但会继承大规模训练数据中的隐私风险，可能无意记忆敏感信息；在数据删除请求（RTBF）下，重训练代价高昂，需要机器遗忘技术。
- 相比文本 LLM 或 ASR，语音问答的遗忘更具挑战：声学感知与事实知识紧密耦合；私有与非私有问题在表示空间中特征方向高度纠缠，难以进行外科手术式擦除。
- ASR 遗忘通常针对词汇或音素映射，而语音 QA 需要切断实体与敏感事实之间的语义链接，同时不破坏语音解析与连贯回答能力。

## 方法创新
- 首次系统研究 LALMs 中的无意记忆问题及数据删除请求下的遗忘算法，并将语音 QA 遗忘与 ASR 遗忘区分开。
- 提出并评估多种遗忘策略：
  1. **Gradient Ascent**：在私有遗忘集上最大化自回归语言建模损失，反转训练梯度方向，使模型输出远离记忆的私有响应。
  2. **Task Arithmetic**：在基座模型上仅用私有数据微调得到任务向量 τ_pri = θ_pri - θ_base，再通过 θ_unlearn = θ_deployed - λ·τ_pri 擦除私有知识；λ 控制擦除强度，遗忘阶段无需梯度。
  3. **Safety Supervised Fine-Tuning**：将私有 QA 中的泄露答案替换为安全拒绝响应，通过标准梯度下降微调，将私有查询映射到安全回答，覆盖原始问答映射。
  4. **Safety Direct Preference Optimization**：构造偏好对，chosen 为安全拒绝，rejected 为原始泄露答案，针对冻结参考模型优化，同时提升安全响应概率并降低泄露响应概率。
- 将参数级方法（梯度上升、任务算术）与行为级对齐方法（Safety SFT、Safety DPO）纳入统一遗忘框架，以推理时防止隐私泄露为实用目标。

## 实验结果
- 基座模型为 Qwen2.5-Omni-7B；实验分两阶段：先微调包含私有与非私有 QA 的模型，部署后将私有训练数据作为遗忘集执行遗忘。
- 数据集包括：Pri 私有集（1000 训练/1000 测试，电话、地址、密码、薪水等），NonPri 非私有集（1000 训练/1000 测试，爱好、职业、偏好等），以及 Chat AIR-Bench 通用语音/音频理解基准；训练与测试使用不同 TTS 声音合成相同问题文本。
- 评估三轴：私有信息擦除程度、非私有事实知识保留、通用语音与音频理解能力保持。
- 实验表明，这些遗忘方法可将隐私泄露率最高降低 80%，同时在非私有语音 QA 和通用语音理解基准上保持接近中性的性能。
- 结果揭示了私有信息擦除与非私有知识保留之间的根本性权衡，也表明方法在去除深层记忆知识方面兼具有效性与固有局限。

## 一句话评价
该工作首次系统探索 LALMs 语音问答中的机器遗忘，提出并比较梯度上升、任务算术、安全 SFT 与安全 DPO 等策略，在显著降低隐私泄露的同时保持核心能力，但隐私擦除与知识保留的固有权衡仍是关键挑战。

---

## 52. The Limits of Reference-Free Speech Quality Metrics as Evaluators and Rewards on Modern Text-to-Speech

**作者**: Antonis Asonitis, Juan Pablo Zuluaga Gomez, Francesco Verdini, Aref Farhadipour, Marzieh Razavi, Pierre-Edouard Honnet, Vijeta Avijeet
**链接**: [2609.13150](https://arxiv.org/abs/2609.13150)
**分类**: Text-to-Speech | **关键词**: reference-free speech quality metrics, MOS prediction, human preference evaluation, reward hacking, text-to-speech evaluation

## 核心痛点

**无参考（reference-free）语音质量预测器正被双重使用，但其前提假设在干净语音上失效。**

- UTMOS、UTMOSv2、DNSMOS、SCOREQ 等无参考 MOS 预测器已成为 TTS 与语音转换系统的**事实标准自动评估器**，并越来越多地被用作偏好优化（preference optimization）的**奖励信号**。
- 这两种角色都隐含一个前提：预测分数能够跟随人类偏好。
- 问题在于：语音自然度没有锚点（不像文本有参考、图像有 caption），同一句话有大量同样自然的表达，判断本质上是相对的；而现有预测器几乎都在**以信号退化为主导变化**的数据上训练（很多是「干净语音 vs. 其退化副本」的分离设定），因此其训练信号被伪影（artifact）主导。
- 一旦现代 TTS 系统变得足够干净、两个候选片段都无缺陷，这些指标就会**从接近人类上限跌落到随机水平**，甚至在最干净的商业系统上不如「盲选更长片段」这种与内容无关的基线。

## 方法创新

1. **成对偏好基准（Benchmark）**：在 6 个人工评分语料上构建同文本、跨系统的成对比较任务，按可听合成质量从「伪影丰富」到「无缺陷」排序：
   - BVCC（artifact-rich, 187 systems, 27.8k pairs, 目标 ΔMOS）
   - SOMOS（artifact-rich, 200 systems, 89k pairs, ΔMOS）
   - SingMOS（歌唱合成, 37.7k pairs, ΔMOS）
   - SpeechJudge（defect-free, 7.6k pairs, 多数投票）
   - TTS-Arena（defect-free, 5.2k pairs, 多数投票）
   - TTS-HP（defect-free, 4 个商业系统 18 个音色, 2.7k pairs, 每对 15 次强制选择投票）
2. **人类可靠性上限（human ceiling）**：报告在「明确多数」对子上听众与多数意见一致的比例（BVCC 0.887；TTS-HP 0.764），作为所有预测器的上界参照，并揭示干净音频上**听众自身的一致性也接近随机**。
3. **大规模预测器与特征对比**：评估 13 个无参考预测器家族（33 个分数变体）、13 个 Praat 韵律描述符（F0 动态、停顿、jitter、shimmer、HNR、CPPS）以及 18 个经典信号处理描述符；所有音频在打分前统一响度归一化到 −23 LUFS，排除音量干扰。
4. **受控干预实验（Controls）**：通过注入伪影与改变表达方式，验证预测器对人为操作仍然敏感，说明干净音频上的「随机水平跨片段准确率」**不是灵敏度 bug**，而是反映了干净音频上人类偏好本身信噪比极低。
5. **留一语料测试（leave-one-corpus-out）**：证明复合评估器**必须做域内校准**，跨域校准无效。
6. **奖励压力测试（Reward stress-test）**：把指标直接当作 RL 奖励做策略优化，观察 reward hacking 现象。
7. **两种不同构造的「混合」方案**：
   - 作为**评估器**：在少量域内样本（≤1000 对）上拟合的**校准复合器（calibrated composite）**，优于从同一数据中挑出的最佳单一指标；
   - 作为**奖励**：在线优化没有标签可用，此时即便是**等权复合（equal-weight ensemble）**也能抵抗 reward hacking。

## 实验结果

- **质量梯度上的崩塌**：在伪影丰富的 BVCC 上，指标逼近人类上限（SCOREQ 0.909、UTMOS 0.892、UTMOSv2 0.899，人类上限 0.887）；在无缺陷的 TTS-HP 上几乎全部塌回随机水平（UTMOS 0.510、SCOREQ 0.502、DNSMOS 0.516，人类上限 0.764）。
- **内容盲基线打平最强指标**：在最干净的商业语料 TTS-HP 上，「偏好更长片段」的基线达 0.524，与最佳单一预测器 UTMOSv2 的 0.528 基本持平。
- **经典 DSP 统计量全程接近随机**（如 spectral flux、crest factor、HF energy ratio），CPPS、F0 std 等韵律特征也大多在 0.5 附近。
- **训练过的成对判别器也失效**：SpeechJudge 自身在其域外语料上表现平平（BVCC 0.507、TTS-Arena 0.463、TTS-HP 0.450）。
- **复合评估器最优但仍有差距**：域内校准复合器在 BVCC 达 0.92、在 TTS-HP 约 0.52（接近随机），在**每个语料上都优于最佳单一分数**，但在最干净系统上只弥补了「随机→人类上限」差距的一小部分。
- **奖励侧**：优化单一分数会把指标推到其最优点，而独立留出评判器与人类听测同时恶化（典型 reward hacking）；等权复合奖励能抵抗该行为并倾向于真正改善模型。
- **结论性诊断**：干净语音上携带偏好的信号是**真实但微弱、分散于众多弱线索、且具有语料特异性**的，因此最优评估器不是固定的通用分数，而是**针对域拟合的互补信号复合器**。

## 一句话评价

本文用统一的成对偏好协议、人类可靠性上限、因果干预与奖励压力测试，系统性地证明并诊断了无参考语音质量指标在干净现代 TTS 上从「接近人类」崩塌到「不如盲选时长基线」的失效现象，并指出单一分数作奖励会诱发 reward hacking，为 TTS 评估与后训练实践给出了重要警示与方法论框架。

---


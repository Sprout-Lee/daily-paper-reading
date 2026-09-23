# Arxiv Daily Deep Report - 2026-09-23

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 43
---

## 1. Not Quite My Tempo: Voice Activity-aware Speech Synthesis for Lip-Synchronous Dubbing

**作者**: Alejandro Pérez-González-de-Martos, Florian Lux, Angelina Elizarova, Milana Shkhanukova, Andreas Kellner, Mattia Antonino Di Gangi
**链接**: [2609.26486](https://arxiv.org/abs/2609.26486)
**分类**: Text-to-Speech | **关键词**: speech synthesis, voice activity detection, prosody cloning, automatic dubbing, lip-synchronous dubbing, flow matching, inpainting-based TTS

## 核心痛点
自动唇同步配音（lip-synchronous dubbing）要求目标语言的语音合成模型能够精确复现源视频中「有声/静音」交替的时间模式，以保证视听一致性。然而：
- 现有方法多依赖视频信号中提取的唇部运动（lip movements）作为条件，需要成对的视频数据，训练成本高；
- 唇部检测与建模在卡通、动漫、多说话人等场景下非常脆弱（brittle），常需专用编码器；
- 严格的唇同步约束在真实影视中其实很少被满足（据大规模研究仅约 12% 时间存在对齐），对未适配的翻译（如普通 MT 输出）强行对齐反而可能损害音质。

## 方法创新
1. **VAD 条件化（核心创新）**：不依赖视频，仅用帧级二值「语音活动检测（VAD）」掩码作为时间条件。该信号表示每帧是否有语音，被嵌入后加到编码器表示上，为 Diffusion Transformer（DiT）Flow Matching 解码器提供显式的时间语音活动线索。由于 inpainting 范式在固定长度画布上工作，源语言与目标语言帧数一致，二值模式可无缝传播，仅约束时间结构，语言内容的分配由模型端到端学习。
2. **可选条件（随机掩码）**：训练时随机掩码部分真值 VAD 嵌入，使该特征在推理时完全可选；编辑人员可依据需求强制或放松唇同步约束。完全掩码即等价于不使用 VAD 条件。
3. **基础 TTS 架构改进**（基于 F5-TTS）：
   - 用 ZipVoice 的平均上采样替代 filler-token 上采样，增强近似对角时间对齐的归纳偏置；
   - 采用显式说话人嵌入 + Global Style Tokens（GST）实现零样本音色/风格迁移，替代 acoustic prompt 条件化，提升音色、风格与口音的解耦；
   - 采用预训练修改版 SoundStream 声码器（16 kHz 波形 → 32 维标量量化隐码，输出 48 kHz 高保真音频）。
4. 无需视频配对数据，也不依赖主说话人脸检测与唇部动力学建模。

## 实验结果
- **数据**：核心英文模型在 LibriTTS-R 上训练（保证可复现），另有基于公开+专有数据的多语言模型；评测使用 mTEDx 子集，共 291 条 7–15 秒、至少含一个 >500 ms 停顿的样本，覆盖希腊语、法语、葡萄牙语、俄语；主观评测随机抽取 25 条。
- **对齐一致性**：帧级 VAD 准确率从无条件的约 73%（偶然重叠）提升到条件化后约 **96%（LibriTTS 模型）**；多语言模型约 **91.59%**（希 91.28%、法 92.21%、葡 91.67%、俄 91.14%），略低归因于多语言数据中 hesitation、笑声、喊叫、耳语等非语音事件增多。
- **跨 VAD 系统验证**：使用 Pyannote、TEN、Silero 三个 SOTA VAD 测量输出，条件化合成在全部三个系统上均一致取得更高准确率。
- **静音边界时序**：条件化时静音起止偏移紧密集中在 0 附近，说明时间精度高；无 VAD 条件时偏差分布明显更宽。
- **韵律自然性**：尽管未显式约束停顿位置，模型仍学会在语言学合理的边界处放置停顿，保持自然韵律；主观与客观评测均支持这一点。

## 一句话评价
该工作提出一种轻量且优雅的「VAD 二值掩码 + inpainting 式流匹配 TTS」方案，仅用音频-文本数据即可实现高精度的唇同步配音时间对齐，并通过训练期随机掩码实现了推理时可控（可选）的同步强度，兼顾了时序精度与韵律自然度。

---

## 2. Persistent Delivery Optimization for Streaming Speech-to-Text Translation with Revisions

**作者**: Zixiang Wan, Delin Chen, Wei Shi, Haihua Xu, Youxi Xie, Yuexian Zou
**链接**: [2609.26427](https://arxiv.org/abs/2609.26427)
**分类**: Streaming Speech-to-Text Translation (Speech Translation) | **关键词**: streaming speech translation, revision-capable translation, persistent delivery, reinforcement learning, latency, process reward / credit assignment

## 论文总结：Persistent Delivery Optimization for Streaming Speech-to-Text Translation with Revisions

### 一、核心痛点
在**支持修订（revision-capable）的流式语音到文本翻译（streaming S2TT）**中，系统可以随着更多源语音到达而更新此前已显示的草稿。这带来了一个新的信用分配（credit assignment）问题：

- **可见性 ≠ 交付性**：传统单调流式翻译中已输出内容不可撤回，当前可见草稿即最终承诺内容；但在可修订场景下，被显示过的文本可能随后被改写或删除。
- 因此，**基于当前可见草稿计算的过程奖励（process reward）会把“早期输出信用”错误地分配给那些最终被撤回的临时内容**，即使这些内容并未保留到最终译文。
- 已有工作（如 Hibiki-Zero、HPO）用中间翻译质量奖励或在无界语音上联合优化质量与延迟，但都没有针对“修订后被撤销的可见文本仍获早期奖励”这一修订特有的失效模式。

### 二、方法创新

**1. 提出 PDO（Persistent Delivery Optimization，持续交付优化）**
一个**轨迹级（trajectory-level）目标**：只奖励“出现得早且在后续所有修订中保持不变”的内容，最终翻译质量单独评分。

- 对更新时刻 t，取当前草稿与所有后续草稿的**最长公共前缀（LCP）**作为“存续内容”：
  `p_t = LCP(d̄_t, d̄_{t+1}, ..., d̄_T)`，且满足前缀单调性 `p_t ⪯ p_{t+1}`。
- 效用函数：`J_PD(τ) = Σ_{t=1}^{T-1} Δ_t · q_p(p_t, ȳ) + H · q_s(d̄_T, ȳ)`，其中 `q_p` 为持续前缀的词法覆盖率（ROUGE-L recall），`q_s` 为归一化有效阶句级 BLEU，`H>0` 加权终端质量；Δ_t 为源时间间隔，**越早稳定下来的内容获得越多源时间信用**。
- 文本单元化：丢弃外围标点但保留词内撇号/连字符；中文/日文按汉字/假名 + 连续非 CJK 字母数字串，其他语言按 Unicode 词切分。
- 单调输出时退化为 `p_t = d̄_t`。

**2. 轨迹信用回传**
定义 `Φ_t` 与回报 `G_t = Φ_T − Φ_{t-1} = Σ_{t'=t}^{T} r_{t'}`，使**后续修订能够影响对早期输出的信用分配**（全轨迹回报）。回报在完整 rollout 后计算，推理仍保持因果性。

**3. 策略优化（PPO + 组相对标准化）**
- 每轮冻结当前策略为近端快照 π_prox，用温度调整的行为分布 π_b 采样 K 条全新闭环轨迹（每条草稿做为下一次更新的历史）。
- 组内标准化回报：`w_t = (G_t − μ_t)/(σ_t + ε_num)`，近零方差组权重置零。
- 损失：`L_PDO = −(1/|B|) Σ c_{t,j} · min[ρ_{t,j} w_t, clip(ρ_{t,j},1−ε,1+ε) w_t]`，其中 ρ = π_θ/π_prox 约束相对轮初快照的更新，c = min(c_max, π_prox/π_b) 为温度采样带来的截断修正；**同一草稿内所有 token 共享事件权重，而比率与修正为 token 级**；损失按轨迹数而非 token 数归一化。

**4. 系统实现（History-conditioned end-to-end 流式 S2TT）**
- 基于 **Qwen3-ASR-1.7B**，冻结预训练骨干，训练目标任务 **LoRA φ** 与 **历史模块 η**；η 通过**零初始化门控交叉注意力**注入上层解码器。
- 训练流程：文本翻译 → 全音频 S2TT → **源文本条件消融**（全量/损坏/前缀/空 以 0.4/0.3/0.2/0.1 混合，空条件提供直接语音→目标监督）→ 流式 SFT（完整翻译锚点 + Hibiki 风格上下文对齐产生的累积草稿，等权、按语言方向平均、共享录音方向等权）→ **History-SFT**（闭环 rollout 缓存模型自生成历史，仅训练 η，并施加一阶投影约束，防止历史模块更新增大冻结父策略的续写损失）。
- **推理时无中间源转写文本**（Direct 模式），也不使用源-目标对齐（仅用于构造流式监督）。

### 三、实验结果

**数据与基线**：仅用 FLEURS En→Zh/De/Es/Ja/Fr 适配（TRAIN/DEV/TEST 为 2602/394/647 条共享英语录音，7.49/1.05/1.77 h；流式阶段用 2600 条 TRAIN）。基线含 SeamlessStreaming、SimulStreaming、EASiST、Hikari-medium、AlignAtt4LLM、SimulS2ST-Omni，以及匹配骨干的全上下文 Qwen3-ASR→Hy-MT2。PDO 模型 2.35B 参数，仅更新 15.9M 参数。

**主要结果（FLEURS TEST，三 seed 平均）**：
- 在 **5 个方向中的 4 个取得最优 BLEU**，并在**全部 5 个方向上 COMET 高于所有外部流式基线**。
- 五方向宏平均：BLEU **31.58**（History-SFT 30.77）、COMET **85.37**（外部最佳 SeamlessStreaming 80.71）、chrF++ **44.67**（History-SFT 44.07）。
- 相对 History-SFT 初始化：**finalization-aware 延迟 mean/P90 降低 10.8%/11.3%**（LAAL_CU 3.05/5.66 vs 3.42/6.38），**归一化擦除（normalized erasure）降低 15.8%**，同时在**首个允许的 2 s 更新即输出**（FTL = 2.00 s，未靠延迟来换取稳定性），且宏平均 BLEU 提升。
- 分语言亮点：Zh BLEU 38.16、Ja 28.66（History-SFT 28.30）、De 29.57、Es 23.35、Fr 38.16；COMET 在 De/Ja 略低于 History-SFT，体现质量—稳定性权衡。

**零样本跨域验证**：在 Europarl-ST v1.1（En→De/Es/Fr，原始切分）和 CoVoST 2（En→Zh/De/Ja）上评估，确认收益**不局限于 FLEURS 训练域**，也不是通过推迟首次响应得到的。

### 四、一句话评价
PDO 精准识别并修复了“可修订流式翻译中可见文本信用与最终交付不一致”这一被忽视的信用分配缺陷，用“最长公共前缀 + 全程轨迹回报 + PPO/组相对标准化”的简洁公式，在不增加推理延迟、不依赖源转写的前提下同时提升翻译质量、降低擦除率与 finalization-aware 延迟，是一项方法论清晰、实验充分（含零样本跨域）的扎实贡献。

---

## 3. A Hybrid Classical-Learning Framework for Adaptive Decision Directed Speech Enhancement

**作者**: Ali Rajabi, Xiangwei Zhou
**链接**: [2609.26183](https://arxiv.org/abs/2609.26183)
**分类**: Speech Enhancement | **关键词**: Speech Enhancement, Decision-Directed Estimation, Spectral Subtraction, Adaptive Beta Constraint, Multilayer Perceptron, VoiceBank-DEMAND

## 核心痛点
- 经典谱减法（Spectral Subtraction）与判决引导（Decision-Directed, DD）增强方法具有可解释性强、计算复杂度低等优点，但在低信噪比（SNR）条件下容易产生音乐噪声，或过度衰减微弱语音成分。
- 传统 DD 增益在低 SNR 区域可能变得过小，导致弱语音被过度抑制。
- 在包含多说话人、多语句、多噪声条件的大规模数据集上，人工调节 beta 参数不切实际。

## 方法创新
1. **自适应 Beta 约束的判决引导（ABCDD）框架**：在传统 DD 增益基础上引入与帧相关的下界约束，定义为 `G_ABCDD(k,m) = max(G_DD(k,m), β_m)`，其中 `β_m ∈ [0,1]`。该参数控制噪声抑制与语音保留之间的权衡：较小的 beta 允许更强抑制但可能损伤弱语音，较大的 beta 保留更多语音但可能残留噪声。
2. **轻量级 MLP 参数预测策略**：为避免人工选择 beta，提出一个轻量级多层感知机（MLP）模型，从带噪语音特征中直接预测帧级 beta 值。
3. **混合式设计思路**：保留经典 DD 增强的可解释性与高效结构，同时利用数据驱动的参数自适应提升鲁棒性。

## 实验结果
- 在代表性语音样本上，ABCDD 在 SNR、对数谱距离（LSD）、均方根误差（RMSE）、相关系数以及尺度不变信噪比（SI-SDR）等多个客观指标上优于传统谱减法和经典 DD。
- 在 100 个未见过的 VoiceBank-DEMAND 测试文件上，所提出的 MLP-beta ABCD D 方法将平均尺度对齐 SNR 从 9.41 dB 提升至 13.82 dB，平均增益为 4.41 dB。

## 一句话评价
该工作提出了一种可解释、轻量且有效的经典-学习混合语音增强框架，通过帧级自适应 beta 约束和 MLP 参数预测，在抑制噪声与保留弱语音之间取得更好的平衡，并在大规模测试中验证了其实际有效性。

---

## 4. SE-MSB: End-to-End Unpaired Speech Enhancement using Mamba Schrödinger Bridges

**作者**: Andreas Bagge, Andreas Nymand, Michael Riis Andersen, Bjørn Sand Jensen
**链接**: [2609.26000](https://arxiv.org/abs/2609.26000)
**分类**: Speech Enhancement | **关键词**: Unpaired Speech Enhancement, Schrödinger Bridge, Mamba, Diffusion Models, End-to-End Waveform Processing, Optimal Transport

## 核心痛点
传统语音增强（SE）通常依赖成对的干净/退化语音进行监督学习，退化数据多由人工模拟（加噪、削波等），难以覆盖真实环境中的未知声学特性、Lombard 效应、历史录音修复等场景，大规模配对数据采集不可行甚至不可能。现有非配对方法多基于频谱图，受固定时频分辨率、相位丢失、需要退化算子或额外声码器等限制；且扩散/薛定谔桥训练常需在每步模拟微分方程，计算昂贵，推理速度慢。

## 方法创新
本文提出 SE-MSB（Speech Enhancement Mamba Schrödinger Bridges），首个完全非配对、端到端、直接处理原始波形的语音增强框架。核心是将 Diffusion Schrödinger Bridges（DSB）与 Mamba 选择性状态空间模型结合：
- 用 DSB 学习干净分布 p_clean 与退化分布 p_noisy 之间的随机传输过程，可仅用独立非配对样本训练。
- 将前向/反向 SDE 的漂移项用同一个网络 v_θ(X_t,t,s) 参数化，s∈{0,1} 指示方向；用 Euler-Maruyama 离散模拟。
- 采用 DSB Matching 两阶段算法：预训练阶段使用随机耦合（非配对），微调阶段用当前模型模拟得到的耦合；理论上可收敛到 Schrödinger Bridge。当 β=0 时退化为 Reflow，可得到“直线流”，利于少步扩散采样。
- 提出面向原始波形的 Mamba Diffusion Model，利用 Mamba 的线性序列长度缩放和常数推理状态，解决原始波形高维长序列建模问题。
- 方法任务灵活，可统一处理降噪、去削波、去混响及复合退化，支持真实场景/个性化适配。

## 实验结果
根据片段，作者与当前最先进的配对和非配对语音增强方法以及经典信号处理算法进行比较。结论：SE-MSB 在性能上达到或优于基线，同时推理速度快数个数量级；这既得益于 Mamba 架构效率，也得益于少步扩散不牺牲性能。文中表 1 显示 SE-MSB 是唯一同时满足非配对、端到端、任务灵活的方法，而 GFB、BUDDy、A2ASB 各有局限：GFB 虽处理原始音频但内部使用 STFT/ISTFT，BUDDy 非任务灵活，A2ASB 需要配对数据。片段未给出具体指标数值，需查阅全文实验部分。

## 一句话评价
SE-MSB 将 Schrödinger Bridge 的非配对分布传输能力与 Mamba 的高效波形建模结合，为真实场景语音增强提供了有前景的端到端、任务通用且推理高效的解决方案，但其实际增益和泛化性仍需完整实验与消融验证。

---

## 5. HRTF Upsampling Across Varying Measurement Configurations with Geometry-Aware Query-Conditioned Aggregation

**作者**: Xingyu Chen, Hanwen Bi, Sipei Zhao, Fei Ma, Eva Cheng, Ian S. Burnett
**链接**: [2609.25995](https://arxiv.org/abs/2609.25995)
**分类**: Spatial Audio / HRTF Upsampling | **关键词**: HRTF upsampling, spatial audio, cross-attention, variable-context, Conformer

## 论文信息
- 标题：HRTF Upsampling Across Varying Measurement Configurations with Geometry-Aware Query-Conditioned Aggregation
- 作者/机构：Xingyu Chen, Hanwen Bi, Sipei Zhao, Fei Ma, Eva Cheng, Ian S. Burnett；University of Technology Sydney / Monash University
- 领域：空间音频、HRTF上采样、个性化头相关传递函数

## 核心痛点
- 个性化HRTF对空间音频渲染至关重要，但密集测量个体HRTF成本高、耗时长。
- 现有学习式HRTF上采样方法多绑定于预定义测量配置，即固定测量数量或固定测量方向，难以适应实际采集中的可变测量配置。
- 实际场景中可用测量可能在数量和空间分布上变化，例如采集约束、测量缺失、自适应采样等，因此需要一种可变上下文HRTF上采样方法。

## 方法创新
- 提出GeoAtt，将HRTF上采样显式解耦为查询条件空间聚合与频域建模。
- 空间聚合：以目标方向q作为cross-attention的query，以可用测量作为key/value，并在每个频率bin上独立进行聚合。
- 几何感知：借鉴Point Transformer的相对位置编码，定义r_{q,i}=[q-d_i, q^T d_i, arccos(q^T d_i)]，分别表示头中心相对笛卡尔位移、角度相似性和测地距离，并将其作为加性注意力偏置注入注意力矩阵。
- 频谱特征构造：对每个测量在每个频点构造s_{i,f}=[H_{L,i,f}, H_{R,i,f}, H_{L,i,f}-H_{R,i,f}]，结合多尺度正弦方向编码，经共享MLP投影后形成上下文特征。
- 频域建模：将逐频点聚合特征沿频率轴堆叠，加入可学习频率位置编码，再通过堆叠Conformer blocks建模长程频率依赖与局部频谱结构，最终共享线性投影输出双耳对数幅度HRTF。
- 训练目标：采用对数谱失真LSD与谱梯度损失SGL联合监督。
- 关键能力：单一训练模型可处理无序、变数量、变空间分布的测量上下文，实现跨测量配置的HRTF上采样。

## 实验与结果
- 数据集：SONICOM，包含200名听者、793个方向；保留187.5 Hz到19.875 kHz，F=106个频点；前180名听者训练，后20名测试。
- 训练策略：每个样本采样一个context set与query directions；以0.5概率从LAP四种规范配置M∈{3,5,19,100}中选择，否则M从{3,...,100}均匀采样，方向随机无放回选取；每个context set采样Q=64个查询方向。
- 模型配置：4个Conformer blocks，特征维度128，前馈维度256，8个注意力头，卷积核7，多尺度正弦编码B=4，dropout=0.1；AdamW，lr=1e-3，weight decay=1e-4，batch size=8，训练440 epochs。
- 对比方法：RANF与IOA3D作为配置特定基线，分别为LAP挑战赛第一、第二；SConvCNP作为可变上下文基线。
- 主要结果：单一训练GeoAtt模型在四个LAP规范配置下均取得最低平均LSD；相比最佳配置特定基线，在M=3、5、19、100时LSD分别降低0.50、0.38、0.14、0.19 dB。
- 泛化能力：GeoAtt可泛化到训练中未显式包含的测量配置，说明其跨测量数量与空间分布的灵活性。
- 评价指标：LSD与ILD误差，单位dB。

## 一句话评价
GeoAtt通过几何感知的查询条件跨注意力与Conformer频域建模，使单一模型能够在可变测量配置下完成HRTF上采样，在SONICOM上优于配置特定和可变上下文基线，并展现出良好的配置泛化能力。

---

## 6. Interactive TTS: Dynamic Speaking Style Adaptation for Expressive Speech Synthesis

**作者**: Wenjie Tian, Kangxiang Xia, Jingbin Hu, Xinfa Zhu, HangRui Hu, Ziyue Jiang, Kexin Huang, Ting He, Lei Xie, Jin Xu
**链接**: [2609.25707](https://arxiv.org/abs/2609.25707)
**分类**: Text-to-Speech (Interactive/Context-Aware Expressive TTS) | **关键词**: Interactive TTS, Dynamic Speaking Style Adaptation, Context-to-Instruction, Instruction-Conditioned TTS, Context-Aware Direct Preference Optimization, Iterative Rejection Sampling Fine-Tuning

# 论文总结：Interactive TTS: Dynamic Speaking Style Adaptation for Expressive Speech Synthesis

## 核心痛点
- 多轮多模态交互中，TTS 需要根据用户意图、对话状态和环境动态调整说话风格，同时保持说话人身份一致。
- 现有 context-aware TTS（CTTS）通常采用端到端隐式映射，把对话历史直接映射到语音，导致上下文风格决策难以监督、解释和控制。
- 训练目标主要优化与 ground-truth 语音的对齐，而非生成的表达是否上下文适当或是否遵循指令，可能产生“听起来自然但态度/情绪/紧迫感错误”的语音。
- 说话风格与语言内容、说话人身份在端到端范式中高度纠缠，频繁且强烈的风格变化会引发跨轮说话人身份或音色漂移。
- 多模态交互中的风格线索往往稀疏、间接，既可能来自显式指令（如“说得慢一点”），也可能需要从语言语义、声学韵律、视觉场景等隐式上下文推断。

## 方法创新
- 提出 Interactive TTS，将任务解耦为 perception 与 expression：先显式做出上下文风格决策，再据此实现声学生成。
- Context-to-Instruction（C2I）模块：基于 Qwen-2.5omni-7B 的 thinker，先产生 rationale Rt 聚合风格相关证据，再生成可执行、人类可读的风格指令 It。指令可描述情绪、情绪强度、语速、音量、语气/态度等副语言属性组合，比固定类别风格空间更灵活。
- C2I 训练与监督：由于缺少配对 context-instruction 数据，使用 Gemini-2.5-Pro 构造 (Ct, Xt, Rt, It) 初始监督数据；训练时拼接 rationale 与 instruction 作为目标序列，最小化自回归负对数似然。
- On-Policy Self-Distillation（OPSD）：教师额外观察音频/视频字幕 Tpriv,t，学生仅条件于 (Ct, Xt)；沿学生采样轨迹最小化教师与学生 token 级 KL 散度，以缓解多模态推理能力退化并提升风格预测稳定性。推理时 C2I 无需额外字幕，仅将 It 传给语音生成器。
- 生成框架：基于 Qwen3-TTS-CustomVoice，参考语音置于 system-prompt 段以提供持续说话人条件；生成语音表示为离散语音 token 序列。
- 多目标后训练：
  - Iterative Rejection Sampling Fine-Tuning（Iterative RSFT）：利用 evaluator 选择的模型 rollout 提升风格指令遵循，同时约束说话人相似度、保留说话人身份。
  - Context-Aware Direct Preference Optimization（CADPO）：将原始交互上下文纳入偏好学习，鼓励生成语音不仅遵循风格指令，还符合当前对话情境。
- 整体优化覆盖三个维度：instruction faithfulness、speaker consistency、contextual appropriateness。

## 实验结果
- 摘要指出，大量实验表明 Interactive TTS 在 VStyle 和 SpeechParaling-Bench 上优于 state-of-the-art 模型。
- 论文贡献列表称，在多个 perception 和 end-to-end benchmark 上取得优于强开源与商业基线的表现。
- 提供 demo 页面：https://wjtian-wonderful.github.io/InteractiveTTS/。
- 由于给定片段截断，未提供具体数值结果；完整实验可能包含 VStyle、SpeechParaling-Bench 等基准上的客观/主观对比。

## 一句话评价
Interactive TTS 将隐式的上下文风格决策显式化为可执行指令，并通过 C2I、OPSD、Iterative RSFT 和 CADPO 联合优化指令遵循与说话人一致性，为多轮多模态交互式语音合成提供了更可控、可监督的新范式。

---

## 7. SRF-SVB: Style-Consistent Singing Voice Beautifying via Rectified Flow

**作者**: Wenhui Li, Biao Dong, Liwei Hu, Jiqing Han, Yongjun He
**链接**: [2609.25610](https://arxiv.org/abs/2609.25610)
**分类**: Singing Voice Beautifying | **关键词**: Singing Voice Beautifying, Rectified Flow, Diffusion Transformer, Style Consistency, Mel-Spectrogram Inpainting, Pitch Correction

## 核心痛点
- **任务目标**：Singing Voice Beautifying (SVB) 需在修正业余演唱的音高与节奏的同时提升音质，并保留歌词和歌手音色。
- **现有方法不足**：生成质量与效率有限，且往往忽视歌手个人风格的保留。
- **相关任务局限**：Automatic Pitch Correction (APC) 类方法如 KaraTuner、Diff-Pitcher 主要关注音高，忽略节奏与表现力；StylePitcher 侧重风格跟随的音高曲线生成；NSVB 首次形式化定义 SVB，但依赖严格配对的业余-专业演唱数据，数据采集困难；CONTUNER 探索非平行数据的扩散式 SVB，但难以兼顾高质量生成与高效推理。
- **风格丢失问题**：过度追求专业音质会削弱业余歌手独特音色与表达模式，导致美化结果缺乏辨识度和真实感。

## 方法创新
- **首个基于 Rectified Flow 的 SVB 框架 SRF-SVB**：利用 rectified flow 构建从噪声到数据分布的直线 ODE 路径，提高训练稳定性与推理效率，同时保持高质量生成。
- **声学特征解耦**：分别提取音高特征、音色特征和内容特征，并引入有效帧掩码，将四类特征在通道维度拼接、归一化并映射到统一隐藏维度，形成声学条件，用于独立控制不同声学属性。
- **上下文引导的掩码梅尔谱修补机制**：随机选择起始时间位置并掩蔽长度为 L=α·T 的连续帧（α 控制掩蔽比例），生成二值掩码；将掩码梅尔谱与掩码向量拼接为掩码感知条件；训练损失仅计算在掩蔽区域，使模型在声学条件和周围频谱上下文引导下重建缺失内容，从而保持业余歌手的音色与表达风格一致性。
- **Rectified Flow 与 DiT 主干**：以 Diffusion Transformer (DiT) 结合旋转位置编码参数化速度场；时间步经 MLP 编码并通过自适应层归一化调制 DiT 层；训练目标为条件流匹配损失，仅在掩蔽区域计算。
- **推理流程**：输入同一内容的业余与专业演唱片段。前 Ta 帧作为上下文，使用业余歌手的音高、音色、内容特征和有效帧掩码；后续 Tp 帧作为生成区域，使用专业音高和有效帧掩码引导旋律轮廓；通过 DTW 对齐业余与专业音高曲线，将内容特征映射到专业时间轴以修正节奏；保留业余歌手音色特征。构造掩码梅尔谱与二值掩码后，从高斯噪声开始用 Euler 法求解 ODE，迭代至 t=1，取最后 Tp 帧作为美化后的梅尔谱，再经预训练神经声码器合成波形。

## 实验结果
- **训练数据**：使用 PopBuTFy、GTSinger、OpenSinger、Opencpop、PopCS、M4Singer 等多个公开中英文歌唱数据集，总计约 160 小时高质量演唱片段。
- **测试数据**：英文测试集来自 PopBuTFy，包含 617 对配对片段及歌词标签；中文测试集包含 874 对配对片段，通过 CCMusic 业余演唱与专业歌曲干声配对，以及自行录制业余版本与 Opencpop/OpenSinger 专业片段配对构建。
- **基线模型**：Diff-Pitcher（基于扩散的自动音高修正）和 NSVB（基于 CVAE 的生成式 SVB，需平行数据）。
- **评价指标**：客观指标包括 Raw Pitch Accuracy (RPA) 等，同时进行主观评价。
- **主要结果**：在英文和中文测试集上，SRF-SVB 在大多数客观与主观指标上优于基线模型，在音高准确度、音色相似度和整体质量方面取得更优或可比表现。
- **实现细节**：单张 NVIDIA GeForce RTX 4090 24GB GPU 训练 500k 步；AdamW 优化器；前 10k 步线性预热至 2.5×10^-4，随后指数衰减至 1×10^-4；掩蔽比例 α=0.5；音高提取器 RMVPE，内容特征为 Conformer 预训练的 PPG，音色嵌入为 CAM++；音频 22050 Hz、帧长 1024、帧移 128、80 维梅尔；声码器 NSF-HiFiGAN；DiT 含 12 个 Transformer 块、隐藏维度 512、每层 8 个注意力头；推理使用 Euler 法 10 步采样。

## 一句话评价
SRF-SVB 是首个将 rectified flow 引入 SVB 的框架，通过风格一致的掩码梅尔谱修补与声学特征解耦，在音高/节奏校正、音色保持和推理效率之间取得了较好的平衡，但其对专业音高与 DTW 对齐的依赖以及完整实验细节在片段中未完全展开，泛化能力仍需进一步验证。

---

## 8. Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis

**作者**: Biel Tura Vecino, Yoach Lacombe, Julian Weber, Zbigniew Łatka, Haitong Zhang, Logan Hart, Eren Gölge
**链接**: [2609.25411](https://arxiv.org/abs/2609.25411)
**分类**: Text-to-Speech (Controllable Speech Synthesis / Classifier-Free Guidance) | **关键词**: Text-to-Speech, Classifier-Free Guidance, Learnable Null Embeddings, Controllable Speech Synthesis, Decoupled Guidance

# 论文总结：Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis

## 核心痛点
- 现有 TTS 中 CFG 常用固定空表示（如零向量）作为无条件参考，但该做法存在两个主要问题：
  1. 单一无条件向量无法区分不同条件模态。TTS 中说话人身份与文本内容通常是正交信号，分别控制语音的不同方面。
  2. 预定义无条件向量可能位于模型输入训练分布之外，导致训练不稳定（大梯度），零向量还可能带来推理期数值不稳定。
- 使用自定义动态 attention mask 替代 fixed token 虽可保留因果 attention 并避免编译开销，但可能触发重复重编译或阻碍 backbone 优化。

## 方法创新
- 提出可学习 null embedding：为每个条件模态学习一个无条件嵌入，替代固定零向量。说话人条件用 s_bar，文本条件用 t_bar。
- 无条件隐状态变为：h_bar_i = g_theta(z_:i-1, s_bar, t_bar)。
- 训练时按概率独立替换条件信号，使 null embedding 与模型端到端联合优化，收敛到稳定、有意义的域内无条件基线，并支持跨条件轴的隐式梯度共享。
- 解耦属性 CFG：定义模态特定无条件隐状态 h_bar^s_i = g_theta(z_:i-1, s_bar, t) 和 h_bar^t_i = g_theta(z_:i-1, s, t_bar)，并扩展 CFG 公式，使 speaker guidance 权重 w_s 与 text guidance 权重 w_t 可独立控制。
- 模型架构：Qwen3-based 0.6B AR GPT backbone + lightweight diffusion heads，采用 next-token diffusion 范式；causal transformer VAE 将语音编码为 64-dim latent z；speaker latents 由 Perceiver encoder 编码参考 mel-spectrogram 得到；文本使用 BPE tokens。

## 实验结果
- 训练两个同架构、同步数、同 seeded 数据子集的模型：固定零向量 vs 可学习 null embedding。条件独立 dropout 概率为 0.1。可学习嵌入由标准正态初始化并联合优化。
- 评估集：65 个未见 expressive proprietary speaker references，每 speaker 合成 2 句，共 130 个生成样本；并对比开源 SOTA TTS：无 CFG 的 Moss-TTS Local、Qwen3-TTS 0.6B，以及带 CFG 的 VibeVoice 1.5B、VoxCPM v2、dots.tts、IndexTTS v2.5。
- 客观指标包括：CER（Whisper v3-large）衡量 speech stability；SECS（ECAPA2）、PRO（WavLM-based prosody embedding）、PMR 衡量 speaker similarity；PQ、UTMOS 衡量 speech quality；Pitch Std、SRR 衡量 speech dynamics。
- 主观评估：CMOS 多模型 pairwise 比较，90 名标注者评估 20 个 case，对比 fixed zero embedding 与两种 learnable null embedding（static 和 tuned guidance）。
- 关键结论：
  - 固定零向量对 guidance scale 更敏感，w > 0.8 后生成质量急剧下降，表现为 PQ/UTMOS 和 speaker similarity 降低。
  - 小 guidance 值下，固定零向量也能提升所有指标，说明传统 CFG 有效。
  - 可学习 null embedding 在低 guidance 下表现相似，但在 w >= 1.0 时达到稳定质量平台，对更大 guidance scale 更鲁棒。
  - 在 speaker similarity 指标（SECS、PRO SECS）上，可学习 null embedding 的平台持续超过固定零向量的峰值，说明学习到的无条件基线提供了更强、更稳定的参考。
  - 与固定零向量在 w = 0.8 的最优设置相比，可学习 null embedding 在 SECS、PRO、PMR 上全面更优；CER 相当；Pitch Std 更高，说明同等稳定性下生成语音更具表现力。
  - 解耦 CFG 可独立控制 speaker 和 text guidance，揭示 similarity/quality 与 stability/expressiveness 之间的 trade-off，实现细粒度属性控制。

## 一句话评价
该论文用按模态区分的可学习 null embedding 替代 CFG 中固定零向量，在几乎不增加推理复杂度的前提下提升 TTS 的说话人相似度、鲁棒性与可控性，并为多条件解耦控制提供了简洁有效的方案。

---

## 9. SPADE: A Multilingual Dataset for Speech Partial Deepfake Detection and Localization

**作者**: Yuan Tseng, Aishwarya Fursule, Andrew Zijun Ma, Vamshi Nallaguntla, Anderson Avila, Shruti Kshirsagar, David Harwath
**链接**: [2609.25197](https://arxiv.org/abs/2609.25197)
**分类**: Speech Deepfake Detection and Localization | **关键词**: partial deepfake, speech deepfake detection, localization, multilingual, speech synthesis, speech editing, anti-spoofing, dataset

## 核心痛点

- 语音克隆与语音生成系统快速发展，恶意滥用风险上升。
- 现有语音深度伪造检测多聚焦完全合成语音，而真实场景中更常见的是仅部分片段被编辑的部分深度伪造（partial deepfake），检测与定位更困难。
- 已有部分深度伪造数据集多为单语言，或仅覆盖一两个生成系统，难以评估跨语言、跨生成系统和跨声学环境的泛化能力。

## 方法创新

- 提出 SPADE：一个面向部分语音深度伪造检测与定位的多语言数据集，覆盖 12 种语言（英语、中文、日语、韩语、俄语、荷兰语、法语、德语、意大利语、波兰语、葡萄牙语、西班牙语）。
- 每种语言最多使用 5 种语音合成/语音编辑系统，包括 F5-TTS、SSR-SPEECH、VoiceCraft、VoiceCraft-X、XTTSv2；同时包含语音合成与语音编辑两类生成方式。
- 数据集同时包含内容改变（transcript 被修改）和内容未改变（transcript 保持不变）的部分深度伪造，各占一半，以提升定位器对长编辑片段的鲁棒性。
- 三阶段构建流程：数据准备（Montreal Forced Aligner 进行词级对齐）、用 Llama 3.1 8B Instruct 自动修改转录文本、用合成/编辑模型生成部分伪造；编辑模型在 latent space 或原始波形层面拼接。
- 支持三类任务：二分类检测（波形是否被修改）、深度伪造定位（哪些区域被修改）、生成模型识别（由哪个系统生成）。
- 数据集包含训练集与评测基准，并已在 HuggingFace 公开。

## 实验结果

- 作者基于现有架构训练定位模型，系统研究三种 out-of-domain 泛化：跨未见语音生成系统、跨未见语言、跨未见声学环境。
- 跨生成系统泛化最困难：定位模型几乎总是无法泛化到训练中未见系统编辑的语音。
- 跨语言泛化相对较好，但性能仍会下降。
- 跨声学环境泛化：在测试集中加入噪声后，定位性能显著下降。
- 在 PartialSpoof 等旧数据集上训练的模型在 SPADE 测试集上表现极具挑战。
- 表 II 表明，在多个短编辑上训练的定位器测试单个较长编辑时性能明显变差，例如 English-English 从 0.68 变为 1.49，Spanish-Spanish 从 2.17 变为 7.00，English-Spanish 从 5.86 变为 27.48。
- 总体结论：现有深度伪造语音检测方法不足以在各种训练时未见场景下可靠检测基于编辑的语音深度伪造。

## 一句话评价

SPADE 是一个多语言、多生成系统的部分语音深度伪造检测与定位基准，系统揭示了现有模型在跨系统、跨语言与跨声学环境下的泛化瓶颈，为更通用的反欺骗检测研究提供了重要数据与评测平台。

---

## 10. Qwen-Audio-Agent Technical Report

**作者**: Chong Deng, Yunjie Ji, Yuxiang Kong, Xiangang Li, Xu Li, Binbin Zhang, Haina Zhu, Jianheng Zhuo
**链接**: [2609.25195](https://arxiv.org/abs/2609.25195)
**分类**: Full-Duplex Voice Agents | **关键词**: full-duplex voice interaction, asynchronous task execution, voice agent orchestration, foreground-background architecture, tool delegation

# Qwen-Audio-Agent 技术报告总结

## 核心痛点
- 语音智能体越来越多地需要跨多轮对话完成复杂任务：用户可能在搜索进行中修改请求、在事务处理过程中补充缺失的约束条件，或询问仍在处理中的文档；智能体必须在回应新输入的同时保持任务状态。
- 全双工语音场景下，对话、任务执行与结果交付运行在不同的时间尺度上，必须被协调一致。
- **语音打断不应隐式取消正在执行的任务**；**任务完成时用户可能正在说话，结果必须被保留到合适的对话时机再交付**。
- 现有系统（OpenAI gpt-realtime、GPT-Live、Thinking Machines Lab 的 Interaction Models、Gemini Live）虽已探索异步函数调用与后台推理/工具使用，但缺少一个通用的协调层来集成不同前端模型与后端执行系统，且大多不开源、不支持跨供应商前端、缺少任务生命周期管理与可扩展环境事件。

## 方法创新
1. **前后台（Foreground–Background）架构**
   - **Frontend Agent**：低延迟对话循环，解释流式输入、维护全双工对话，并选择直接工具调用还是后台委派。
   - **Backend Agent**：在独立上下文、工具与工作区中执行被委派任务（plan-act-observe-refine）。
   - **Orchestration Runtime**：维护任务状态、路由进度更新/用户输入/结果，区分“执行状态”与“交付状态”。
   - **客户端**：采集输入、播放语音、展示产物并执行支持的本地动作。
2. **异步任务协调**
   - 通过 `spawn_thinking` 工具调用发起委派；前端提交自包含目标（含约束与输入引用），因为前端对话历史与记忆不会自动传给后端。
   - 任务记录包含目标、状态、进度、输出与待处理请求；生命周期区分 queued/running 与终态 completed/failed/cancelled。
   - 机制解耦：**语音打断 ≠ 任务取消**，**任务完成 ≠ 结果交付**。结果在用户说话或前端响应进行中暂存；同一收集窗口内的结果合并为一次响应请求；交付失败可重试而不重复已完成的工作。
   - 后端适配器支持 ACP、A2A 或自定义接口，并声明其可选控制能力（取消、请求补充用户输入等）；前端适配器翻译流式事件与工具调用。
3. **环境感知与统一事件协议**
   - 客户端上报视觉观察、应用/设备状态；每种事件类型定义 schema、保留规则与响应策略。
   - 运行时校验事件后可直接处理、静默更新前端上下文、调度响应，或打断当前响应并要求重新生成；协议与前端供应商无关（对比 IrisTK 的多模态事件协调）。
4. **记忆与用户上下文**
   - 会话上下文 = 核心交互规则 + 助手画像 + 显式用户偏好 + 长期用户记忆；前端使用有界记忆快照构建上下文，远程检索与整合可异步进行。
   - 任务记录与参考文档与个人记忆分离；默认实现支持对话中显式编辑与会话边界的事实抽取；可选学习过程仅在跨会话存在一致证据时加入推断偏好。
   - 优先级：当前用户请求 > 存储偏好，显式偏好 > 推断偏好；版本检查防止延迟的后台更新覆盖较新的更正；被用户拒绝的偏好不会被自动再次添加。
5. **多场景落地**：桌面助手（文档编辑、代码执行与验证跨轮进行）、智能座舱（前端工具、后端工具与 GUI 共享同一业务状态与执行逻辑，状态变化以环境事件返回）、语音客服（策略解读、业务记录访问、特定步骤的用户决策）。
6. **开源**：https://github.com/QwenAudio/qwen-audio-agent。

## 实验结果
- 座舱内部基准，共 134 个案例：
  - **混合执行（mixed）任务成功率 91.04%**，显著优于纯直接执行 72.39% 与全委派 80.60%。
  - 在匹配成功轮次的延迟评估中，混合执行相较上述两个基线分别降低平均任务执行延迟 **26.73%** 与 **30.91%**。
- 结论：直接工具调用适合即时操作，后台委派适合多步任务，两者互补。
- Table 1 能力对比显示，Qwen-Audio-Agent 在直接前端工具使用、执行期间保持对话、跨供应商前端支持、可扩展后端智能体、后台任务生命周期管理、可扩展环境事件、持久跨会话记忆与开源编排运行时方面均优于或区别于 gpt-realtime、GPT-Live 与 Gemini Live。

## 一句话评价
Qwen-Audio-Agent 以“前后台分离 + 编排运行时”的 harness 设计，将全双工语音对话与异步后台任务执行彻底解耦（打断≠取消、完成≠交付），在座舱基准上以 91.04% 的任务成功率和显著更低的执行延迟验证了“直接调用 + 后台委派”混合路由的有效性，并提供了支持 ACP/A2A 适配器与持久记忆的开源实现。

---

## 11. Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction

**作者**: Lujia Bao, Qian Chen, Luyao Cheng, Chong Deng, Yuxiang Kong, Xiangang Li, Xu Li, Jiaqing Liu, Chao-Hong Tan, Haoyu Wang, Wen Wang, Xilou Wang, Junhao Xu, Liang Yi, Binbin Zhang, Qinglin Zhang, Qiquan Zhang
**链接**: [2609.25176](https://arxiv.org/abs/2609.25176)
**分类**: Spoken Dialogue Systems / Voice Agents | **关键词**: Real-time Voice Assistant, Agentic Voice Interaction, Full-Duplex Speech Interaction, On-Policy Distillation, GRPO, Tool Use

## 核心痛点
实时语音助手不仅需要低延迟，还要在请求不断变化时进行推理、执行动作并遵守对话规则。现有系统多停留在实时听说，难以可靠完成多轮约束保持、工具调用、反馈解释、状态验证、长时任务与说话/行动时机控制。

## 方法创新
论文围绕三层组织 Qwen-Audio-3.1-Realtime：
- **Think**：以 Core-Cocktail 监督微调为冷启动，结合 Multimodality OPD 与 Multi-Teacher OPD 组成的 M2-OPD，将源文本大模型的语言能力迁移到音频模型，同时发展原生音频技能。训练四阶段：Core-Cocktail SFT → Multimodality OPD → 领域 GRPO 专家 → Multi-Teacher OPD 整合。约使用百万小时级成对音频-文本数据。
- **Act**：构建可执行环境，包含工具、共享数据库、业务策略、任务和验证器；任务合法结局包括策略合规写操作、有依据拒绝、声明请求不支持。通过静态门、rollout 门、难度门筛选任务，并用自演化智能体修复环境、加难已解任务、保留前沿样例。以多粒度 rollout（对话级、里程碑级、轮次级）进行 GRPO，学习工具使用、状态验证、长程任务完成、适当拒绝与进展沟通。
- **Speak and Coordinate**：把口语交互建模为对话策略，决定如何、何时、是否说话或行动，并对齐说话/行动时机。
- **架构**：全双工决策模型与语音转文本模型均采用 Audio Encoder + LLM；上下文感知语音渲染器结合对话历史、语音线索和声学上下文生成流式语音。
- **Voice Harness 原型**：以 Qwen-Audio-3.0-Realtime 为前台，通过前台-后台协调与记忆将口语交互扩展到持续任务。

## 实验结果
- 在半双工 τ-Voice 的语音转文本适配任务上，相比 Qwen-Audio-3.0-Realtime，整体任务成功率从 78.4% 提升到 82.0%。
- 在语音到语音的 Full-Duplex-Bench v1.5 上，对背景语音的响应率从 73.0% 降到 13.0%，说明全双工交互中对背景人声的误响应显著减少。
- 评测覆盖音频推理、多语言理解、工具使用、对话行为、全双工交互和安全等维度。

## 一句话评价
该报告系统性地把实时语音助手从低延迟听说推进到可靠智能体式语音交互，提出 Think/Act/Speak and Coordinate 框架与 M2-OPD、自演化可执行环境等训练方案，并在任务成功率和全双工背景语音抑制上给出明显提升，但所给片段尚未展示全部评测细节。

---

## 12. Beyond Short Segments : Expanding Speaker Embeddings with Vector Archives

**作者**: Hyunku Kang, Minkyu Cho, Chanwoo Kim
**链接**: [2609.25007](https://arxiv.org/abs/2609.25007)
**分类**: Speaker Verification | **关键词**: Speaker Verification, Short Utterance, Vector Archive, WavLM, ECAPA-TDNN

## 论文总结

**标题**：Beyond Short Segments: Expanding Speaker Embeddings with Vector Archives

**作者**：Hyunku Kang、Minkyu Cho、Chanwoo Kim（Korea University）

### 核心痛点
当前 SOTA 说话人验证（SV）系统在短语音（尤其是 3 秒以下、甚至 1-2 秒）上性能严重下降。原因是短片段缺乏长时语音中丰富的协同发音线索和韵律轮廓，难以提取稳定且有判别力的说话人嵌入。这一限制直接影响语音激活设备（命令通常 <2 秒）和电话认证（1-3 秒）等真实部署场景。

### 方法创新
论文提出 **VAM-ECAPA**（Vector Archive Mapping ECAPA），核心是 **TVAMSP** 模块（Transformer-based Vector Archive Mapping with Statistical Pooling），在 WavLM+ECAPA-TDNN 强基线中插入该模块：
1. **WavLM 特征提取**：按 SUPERB 方法对各层表示加权求和，得到帧级特征 f。
2. **Transformer 层**：对 f 做自注意力，建模帧间时序依赖，得到上下文感知表示 O1。
3. **Vector Archive Mapping**：使用可学习的 Vector Archive / Library（G 个 Archive，每个含 l2 个向量）作为固定模型参数提供 Keys 和 Values，与输入 Queries 做类 cross-attention 映射。与标准 cross-attention 不同，其参考不依赖当前短输入，而是编码训练语料中的稳定典型说话人特质。实现上先将 G 个 archive 的 K/V 聚合，再计算注意力并残差加到 O1 上，得到 O2。关键设置：l2=149（对应 WavLM 特征率下 3 秒语音）、G=4。
4. **Attentive Statistics Pooling 特征增强**：用 ASP 计算 utterance 级加权均值 μ 和标准差 σ，拼接投影后得到 summary s，再广播加回帧级序列，得到 O3 = O2 + s，使每帧融入全局上下文。
5. **ECAPA-TDNN 后端**：将 O3 编码为 192 维说话人嵌入，L2 归一化后用于余弦相似度打分。

该方法在推理时不需要额外输入，也不要求多条语音，而是直接在帧级特征提取阶段补偿短语音的信息稀缺。

### 实验结果
- 训练：仅使用 VoxCeleb2 开发集；评估：VoxCeleb1 官方测试集（Vox1-O、Vox1-E、Vox1-H），报告 EER 和 MinDCF（P_target=0.05）。
- 全长度测试中，WavLM+ECAPA-TDNN 优于 Wav2Vec 2.0 和 HuBERT 后端。
- 短语音测试中，VAM-ECAPA 在 1 秒片段上取得 **8.334% EER**（Vox1-O），相对传统训练基线 **18.437% EER** 实现 **54.8% 相对错误率下降**。
- 2 秒 Vox1-O EER 从 5.242% 降至 4.175%；1 秒 Vox1-E 从 18.059% 降至 8.511%；1 秒 Vox1-H 从 20.449% 降至 14.571%。
- 在 3 秒 Vox1-O 上，VAM-ECAPA 的 EER 为 3.185%，略高于基线 2.393%，说明方法主要收益集中在更短时长，长时长上存在一定权衡。

### 一句话评价
论文通过可学习的 Vector Archive 在帧级特征提取阶段为短语音补全典型说话人信息，在 1 秒 VoxCeleb1 上大幅降低 EER，为短时说话人验证提供了不依赖额外推理输入的有效思路。

---

## 13. ROAM-ASD: Robust Open-World Active Speaker Detection with Flexible Multimodal Fusion

**作者**: Pu Wang, Yujun Wang, Hugo Van hamme
**链接**: [2609.26648](https://arxiv.org/abs/2609.26648)
**分类**: Active Speaker Detection | **关键词**: Active Speaker Detection, Audio-Visual Fusion, Joint Self-Attention, Modality Dropout, Zero-Shot Cross-Dataset Generalization

## 核心痛点
- 现有主动说话人检测（ASD）方法主要在 AVA-ActiveSpeaker 等相对清晰的电影场景上开发和评估，在真实野外场景（如 WASD、UniTalk）中性能显著下降。
- 多数方法主要依赖全脸视觉特征，容易受到非语音面部动作、张嘴、遮挡、背景干扰人声等影响。
- 主流跨模态融合多为成对的 cross-attention（如 TalkNet、TS-Talk），需要预先定义音频-视觉等特定模态对，扩展到更多输入流时不灵活，也难以应对模态缺失。

## 方法创新
- 提出 ROAM-ASD，一个面向开放世界/野外条件的鲁棒音视频 ASD 框架。
- 同时建模三类输入流：音频、全脸、细粒度嘴部区域；嘴部区域直接从检测到的人脸中裁剪，无需额外标注。
- 采用统一联合自注意力融合：将音频 token、全脸 token、嘴部 token 与模态无关的 query token 拼接为一个联合序列，让所有可用 token 直接交互，避免预定义成对融合路径。
- 使用模态 dropout 训练，随机丢弃某些输入流，使模型在推理时对缺失模态更鲁棒。
- 音频编码器使用冻结的 Whisper-large-v3；人脸编码器为 3D Conv + ResNet-18 + V-TCN；嘴部编码器使用 Auto-AVSR 预训练视觉语音识别编码器，并通过 rank-8 LoRA 微调注意力投影。
- 融合层为 4 层 pre-norm Transformer，256 维、4 头自注意力，FFN 维度 1024；使用 RoPE 和 ALiBi 风格偏置编码时间信息。
- 融合后的 query 表示与各模态 skip 特征拼接，经时间建模头和线性层输出逐帧说话概率。

## 实验结果
- 在五个 ASD 基准上达到 SOTA：WASD 98.8% mAP、UniTalk 87.9%、AVA 96.5%、ASW 99.3%、Talkies 98.2%。
- 相比此前最佳系统分别提升 +5.1、+4.7、+0.9、+1.0、+2.1 mAP 点。
- 在零样本跨数据集泛化上显著提升，并对缺失观测保持鲁棒；在持续丢失单个输入流时仍维持可用性能。

## 一句话评价
ROAM-ASD 通过引入细粒度嘴部表征和模态无关的联合自注意力融合，有效缓解了野外 ASD 中视觉歧义与模态缺失问题，在多个困难基准上取得显著领先并展现出更强的泛化与鲁棒性。

---

## 14. Transcribe, Translate, and Optimize: Joint Reward Learning for Speech Translation

**作者**: Yanghe Dong, Wanting Huang, Weiran Wang
**链接**: [2609.26536](https://arxiv.org/abs/2609.26536)
**分类**: Speech Translation | **关键词**: Speech Translation, Chain-of-Thought, GRPO, Reinforcement Fine-tuning, Joint Reward Learning, ASR, Qwen2.5-Omni

## 核心痛点
- 在基于 LLM 的语音翻译中，CoT ST（先转录后翻译）在推理时翻译依赖模型自己生成的转录，而 SFT 训练时翻译前缀是参考转录，造成训练-推理不匹配（prefix mismatch）。
- 模型即便有音频输入，仍强烈依赖转录；模型生成转录可能含错误，导致翻译性能下降。
- 直接 ST（Direct ST）虽稳定但峰值性能低于 CoT；需要一种能同时优化识别与翻译、并在模型生成转录条件下优化翻译的方法。

## 方法创新
- 提出联合 ASR-ST 奖励优化：在 GRPO 中对同一响应中的转录和翻译分别打分，翻译奖励基于模型生成的转录（而非参考转录），从而缓解训练-推理不匹配。
- 奖励设计：ST 奖励使用 BLEU 或 chrF++ 并归一化；ASR 奖励为 1 - WER（经 Whisper 英文归一化后），并使用格式门控 g_fmt 要求响应包含一个非空转录和一个非空翻译。联合奖励 R_J = g_fmt (r_ST + λ r_ASR)。
- 比较三种 token advantage 分配策略：Fully Coupled（所有 token 用联合 advantage）、Asymmetric（转录 token 用联合 advantage，翻译 token 用 ST advantage）、Decoupled（转录 token 用 ASR advantage，翻译 token 用 ST advantage）。
- 使用 DAPO 变体 GRPO，非对称裁剪、无 KL 正则；并探索 Reference-Aware Training（在 rollout 组中加入参考响应）。
- 对比 Direct ST 与 CoT ST 两种协议，CoT 协议要求输出 <transcription> 和 <translation> 标签。

## 实验设置
- 基座模型 Qwen2.5-Omni-3B，训练集 CoVoST 2，覆盖阿拉伯语、中文、德语、日语四个目标语言。
- 训练集平衡后 289,412 条，430.12 小时，每语言 72,353 条；CoVoST 2 val/test 每语言 15,531/15,530 条；FLEURS 仅评估，val 1,509 对、test 2,403 对。
- 全参数微调，ms-swift，8×NVIDIA RTX PRO 6000，AdamW。SFT 全局 batch 128，lr 1e-5，cosine decay，5% warmup；GRPO 常数 lr 1e-6，DAPO clip ε_low=0.2, ε_high=0.28。默认 G=4 无参考，rollout 32 prompts（128 policy responses，G=5 时 160），temperature 1.0，top-p 1.0，每次 rollout 一次优化更新，训练一遍。
- 评估：贪心解码，SacreBLEU BLEU/chrF++，英文 WER 经 Whisper 归一化。

## 主要结果
- CoT GRPO 分别比 Direct ST GRPO 在 CoVoST 2 和 FLEURS 上平均 BLEU 高 1.77 和 0.83。
- 相比 CoT SFT，GRPO 在 CoVoST 2 和 FLEURS 上 BLEU 提升 0.82 和 0.67，WER 相对降低 8.8% 和 7.2%。
- 验证集消融：保留 chrF++ 奖励（WER 更低）；保留 G=4 无参考；ASR 权重 λ=0.75 时 CoVoST 2 WER 5.45、BLEU 34.15、chrF++ 43.70，FLEURS WER 5.42、BLEU 28.76、chrF++ 40.56（Fully Coupled）。
- Advantage 分配对比：CoVoST 2 上 Fully Coupled BLEU 最高（34.15），Asymmetric chrF++ 最高（44.29），Decoupled WER 最低（5.35）；FLEURS 上 Fully Coupled 整体最佳（WER 5.42、BLEU 28.76、chrF++ 40.56）。
- 结论：强化微调能有效缓解训练-推理不匹配，并同时改进识别与翻译。

## 一句话评价
- 该工作把 GRPO 引入 CoT 语音翻译，以联合 ASR-ST 奖励在模型生成转录条件下优化翻译，是缓解 CoT 训练-推理不匹配、协同提升识别与翻译的实用方案。

---

## 15. Spoken Language Models that Think Aloud

**作者**: Junyi Ao, Kainan Peng, Mingbo Ma, Shun Zhang, Zhenyu Tang, Xutai Ma, Xiang Li, Yinghao Li, Yuancheng Wang, Zhizheng Wu, Haizhou Li, Qing He, Xubo Liu
**链接**: [2609.26488](https://arxiv.org/abs/2609.26488)
**分类**: Spoken Language Models | **关键词**: Spoken Language Model, Chain-of-Thought, Think-Aloud, Thinker-Talker, Real-time Spoken Interaction

## 核心痛点
基于思维链（Chain-of-Thought, CoT）推理的 Spoken Language Models（SLMs）若直接采用串行“先想后说”（think-then-speak）范式，会在内部推理期间产生长时间无声间隔，即 **unmasked silence**。这种用户可感知的“死气”会破坏对话轮转、削弱交互同步性，使系统在复杂查询下显得无响应。

## 方法创新
论文提出一种面向推理型 SLM 的**异步 think-aloud 框架**，基于 Thinker-Talker 架构，将推理流与说话流解耦并运行时协调：
- **推理 Thinker**：作为认知核心，接收系统提示与音频表示，生成内部推理轨迹，并在用户输入后及推理里程碑位置预测 `<TA_trigger>` token，触发 think-aloud 模块。
- **轻量 Think-Aloud 模块**：一个 0.5B LLM，用于生成简短、任务相关的进度话语。首次响应在用户输入后立即触发，桥接启动静默；后续响应在推理里程碑触发，输入融合用户表示、历史 think-aloud 话语和累计推理隐状态。
- **统一 Talker**：采用 CosyVoice 2.0 流式模式，将文本嵌入与隐状态投影相加。推理阶段使用 think-aloud 模块隐状态合成进度语音；最终响应阶段切换到 thinker 隐状态合成答案。
- **动态平衡策略**：运行时决定何时触发额外 think-aloud 语音、何时取消待生成话语，从而在出现静默时及时补话、在最终响应就绪后避免冗余发音。

## 实验结果
在口语推理与问答基准上，该方法显著减少用户可感知的推理期间静默时长，同时答案准确率与串行“先想后说”基线保持可比。结果表明异步 think-aloud 能在不暴露完整推理链的前提下提升 SLM 的响应交互性。

## 一句话评价
该工作将认知心理学中的“出声思维”转化为异步口语交互机制，有效缓解推理型 SLM 的静默延迟问题，为实时语音助手提供了兼顾准确性与响应性的新范式。

---

## 16. Enriching Speech Emotion Representations with Conversational Context

**作者**: Arthur Peuvot, Romaric Besançon, Gaël de Chalendar, Bianca Vieru, Ioana Vasilescu
**链接**: [2609.26422](https://arxiv.org/abs/2609.26422)
**分类**: Speech Emotion Recognition | **关键词**: Speech Emotion Recognition, Conversational Context, Self-Supervised Learning, Emotion Representation, Context-Aware Modeling

## 核心痛点

当前语音情感识别（SER）研究大多在**话语级（utterance-level）**进行情感预测，忽略了对话上下文、情感流变以及说话人之间的互动。这导致模型难以捕捉真实人类交互中情感随对话动态演化的特性。现有一些尝试引入上下文的方法仍有局限：例如 CHAN 仅使用紧邻的前一条话语作为上下文，ESA CRF 则在话语级预测序列上建模转移关系，而非在底层音频表示上建模；多模态方法又依赖文本或多说话人信息，并非在所有场景下可用。

## 方法创新

论文提出 **ACERT（Averaged Contextual Emotion Representation through Time）** 模块，用于将灵活长度的对话上下文融入目标话语的音频表示中。其核心设计包括：

- **上下文定义**：给定固定时间窗口 t，将目标话语与其之前 t 秒内的话语拼接，构成输入音频片段。上下文窗口长度 t 是超参数，不包括目标话语本身。
- **上下文设计选择**：初步实验表明，使用前文上下文与同时使用前后文效果相当，因此仅采用前文上下文，避免实时场景中等待未来话语的延迟。同时，说话人相关上下文（真实说话人标签或 k-means 说话人日志）与说话人无关上下文没有统计显著差异，因此采用说话人无关设计，避免日志错误传播，也便于跨数据集一致评估。
- **特征提取**：输入片段经特征提取器处理后，通过带 ReLU 的可学习线性层得到帧级表示 H。
- **增强机制**：将帧级特征分为目标帧 H_t 和上下文帧 H_c；对上下文帧进行时间均值池化得到向量 c：
  - c = (1/|H_c|) * sum(h in H_c) h
- **融合与分类**：将池化向量 c 加到每个目标帧上，再经过带残差连接和 LayerNorm 的前馈网络：
  - H'_t = LN(H_t + c)
  - H''_t = LN(H'_t + FFN(H'_t))
  其中 FFN 是两层 ReLU 前馈网络。随后对 H''_t 做时间平均池化，得到话语级表示，并送入分类头（ReLU + 线性层）预测情感类别。

ACERT 可作为一个通用模块叠加在任意特征提取器之上，包括自监督学习（SSL）模型或其他 SOTA SER 方法。论文使用 HuBERT-large 作为特征编码器。

## 实验设置与结果

- **数据集**：IEMOCAP（双人剧本/即兴对话）、MELD（Friends 电视剧多人对话）、SAFE（电影中强烈情感互动）。三者都几乎无缺失话语，保证上下文连续性。
- **评估协议**：IEMOCAP 和 SAFE 采用说话人无关 5 折交叉验证；MELD 采用标准训练/验证/测试划分。每次实验运行 5 次。
- **评价指标**：Unweighted Accuracy (UA)、Weighted Accuracy (WA)、Macro-F1、Weighted-F1 及其标准差。
- **主要结果**：ACERT 在 IEMOCAP 上超越当前 SOTA；在 SAFE 上建立了首个上下文感知基准；在 MELD 上于 unweighted、class-balanced 指标上取得强劲结果。
- **上下文窗口影响**：随着上下文窗口长度增加，性能显著提升，随后趋于平台期。仅加入 t = 5 秒上下文，UA 就从无上下文基线的 68.38% 提升到 76.40%，提升 8.02 个百分点。

## 消融分析

论文在 IEMOCAP 上以最优上下文窗口 t = 25 秒设计了三组消融实验：

1. **同 session、连续上下文**：用同一 session（同说话人、同录音条件）中另一段连续对话片段替换真实前文，保留轮替但内容无关。
2. **同 session、随机上下文**：用同一 session 中其他对话的随机混合话语替换，无时间或对话连续性。
3. **同对话、打乱顺序**：保留前文但随机打乱话语顺序，隔离时间顺序的作用。

结果表明，ACERT 的增益来自**情感与对话连续性**，而非说话人身份或声学条件。

## 一句话评价

ACERT 通过简单有效的时间均值池化与残差融合，在纯音频、说话人无关设定下将对话上下文注入话语级情感表示，显著提升 SER 性能，并为多风格交互场景提供了可扩展的上下文感知建模方案。

---

## 17. Boundary and Intra-Segment Learning for Partial Audio Deepfake Localization

**作者**: Zhe Ye, Xiangui Kang, Minhua Huang, Kai Wu, Kong Aik Lee, Chng Eng Siong
**链接**: [2609.25822](https://arxiv.org/abs/2609.25822)
**分类**: Audio Deepfake Localization | **关键词**: Partial Audio Deepfake Localization, Boundary Learning, Intra-Segment Learning, WavLM, Speech Anti-Spoofing

## 核心痛点
- 部分音频深度伪造（partial audio deepfake）仅篡改语音中的部分区域，真实与伪造内容共存于同一句话中，需在帧级别进行定位，难度较大。
- 现有基于边界线索的方法主要关注边界位置识别，而未充分建模真实性与伪造性切换时产生的特征变化；同时，连续真实段与伪造段的内部整体特征也未被充分挖掘。
- 相邻帧特征变化可能来自音素内容或声学条件变化，不一定代表伪造边界，因此需要区分“真实性切换”与“一般声学变化”。

## 方法创新
- 提出 Boundary and Intra-Segment Learning（BISL），联合学习帧级、边界级与段级信息，用于细粒度部分音频深度伪造定位。
- **边界学习（Boundary Learning）**：计算相邻帧特征差 d_t = h_{t+1} - h_t，并根据相邻帧真实性标签是否变化生成边界标签 b_t，通过边界分类损失 L_bd 引导模型区分真实性切换与一般声学变化。
- **段内学习（Intra-Segment Learning）**：依据真实帧级标签将语音划分为连续的真实段和伪造段；排除每段首尾帧以降低边界影响，对内部帧特征计算均值与标准差并拼接为段级表示 s_i = [Mean(h); Std(h)]，输入段分类头进行段级真实性分类，损失为 L_seg^cls。
- **段内紧凑性损失（Intra-Segment Compactness Loss）**：计算每个段内帧特征与段中心 c_i 的余弦距离，鼓励同段帧特征向段中心聚集，增强段内特征一致性，损失为 L_seg^com。
- **多任务训练目标**：L = L_frame + λ_cls L_seg^cls + λ_com L_seg^com + λ_bd L_bd；其中 L_frame 为帧级交叉熵。
- **模型结构**：WavLM-Large 作为声学编码器，通过可学习加权和融合各层表示，再经两层 Conformer 进行时序建模；帧、边界、段三个分类头均采用相同两层 MLP（隐藏层 256 维）。边界头和段头仅在训练时使用。

## 实验结果
- 数据集：PartialSpoof（PS）、Half-truth Audio Detection（HAD）用于域内评估；LlamaPartialSpoof（LPS）用于跨域评估。
- 在 PS 上：BISL 达到 EER 2.52%、F1 97.40%，优于 BAM（3.58%/96.09%）、BFC-Net（2.73%/96.69%）、SAL（3.07%/97.06%）等基线。
- 在 HAD 上：BISL 达到 EER 0.07%、F1 99.97%，与 SAL 等保持竞争力。
- 在 LPS 跨域评估中：BISL 获得 EER 37.10%、F1 53.61%，表现出改进的跨数据集泛化能力。
- 实现细节：16 kHz 采样，训练时填充/截断至 4 秒，评估使用完整语音；PS 时间分辨率 160 ms，HAD/LPS 为 20 ms；使用 RawBoost 增强（概率 0.2）；Adam 优化器，最多 50 epochs，初始学习率 1e-5，权重衰减 1e-4，StepLR 每 10 epochs 衰减 0.1；λ_cls=0.2、λ_com=0.5、λ_bd=1.0；早停 patience=5；单张 RTX 3090。

## 一句话评价
BISL 通过边界学习与段内学习为帧级部分音频深度伪造定位提供互补的多层级监督，在 PartialSpoof 上取得领先性能，并验证了边界与段级建模对细粒度定位的有效性。

---

## 18. Synthesis and editing of multi-instrument audio mixtures using scalar-quantised latents with MIDI Span conditioning

**作者**: Sungkyun Chang, Keshav Bhandari, Simon Dixon, Emmanouil Benetos
**链接**: [2609.25546](https://arxiv.org/abs/2609.25546)
**分类**: Music Generation (MIDI-to-Audio Synthesis and Editing) | **关键词**: MIDI-to-audio, multi-instrument synthesis, audio editing, flow matching, scalar-quantised latents, MIDI Span, note representation

## 核心痛点
音乐创作具有迭代精修需求：在保留其余内容的同时增删改个别音符或乐器。现有自然语言音乐编辑难以做到细粒度；MIDI 可显式控制音高、时值、力度与乐器，但多乐器混音中声音重叠，渲染目标音符变化时需不破坏并发音符及其音色。此外，低帧率表示会损失帧内时间精度，传统钢琴卷帘量化时序，音符序列又会串行化并发音符。

## 方法创新
论文提出 **SpanSynth-Edit**，一个基于 flow matching 的 MIDI 引导多乐器音频混音合成与编辑模型。
- **音频表示**：使用冻结 HeartCodec 编解码器，将 48 kHz 单声道音频编码为 25 Hz、128 维的标量量化(SQ) latent；逐坐标 Q(x)=round(9x)/9，得到 [-1,1] 内 19 级离散码。低帧率使序列更短，训练/推理高效。
- **MIDI Span 音符表示**：将每个带乐器标签的音符生命周期表示为帧对齐事件集，事件状态为 ONSET/OFFSET/SUSTAIN，属性包括类别属性(事件状态、乐器类)和四个实值属性(音高、力度、边界位置、剩余时长)，归一化到 [-1,1]；边界位置可保留帧内时间。每帧事件集合无序、补齐至 128 槽，经 Deep Sets 式置换不变编码器(1 个 sum + 5 个 sigmoid 门控 sum，RMS 归一化，并加入对数缩放的事件计数)池化为 768 维条件向量，按音频帧堆叠成 MIDI 条件 M。
- **上下文与编辑**：模型可利用目标区域前后的上下文音频及可选对齐上下文 MIDI 进行音色引导；编辑时仅根据修订后的 MIDI 重合成目标区域，无需额外训练。上下文音频既进入加噪 Z_t，也以固定干净 A 形式进入模型，只对目标帧计算损失。
- **生成模型**：条件 flow matching，Z_t=(1-t)ε+tZ，目标向量场 V*=Z-ε；生成器为 480.8M 参数的 25 层 DiT(width 1024)，输入拼接 [Z_t||M||B] 与 A 的独立投影，B 为二值掩码(目标区域/上下文 MIDI)。推理用 Euler 积分(32 步)，最终 latent 裁剪、重量化并解码；可选地将 FlowEdit 从图像编辑迁移到 MIDI 引导音频编辑，训练-free。

## 实验结果
- **合成任务**：在 Slakh、MusicNet、URMP、GuitarSet、MAESTRO Piano V3 等单/多乐器基准上评估音频质量(MuQ eval、PQ)、音频相似度(MERT-FAD、MuQ/CLAP 余弦、Smooth MSS)与音符遵循度(YourMT3+ 转谱，50 ms 容差，F_On、F_P37、F_P13、OpenMIC)。SpanSynth-Edit 在多个基准上取得有竞争力或最佳表现，例如 Slakh+drums: MuQ 4.65、PQ 8.08、FAD 1.33、MERT 0.89、MuQ cos 0.90；MusicNet: PQ 7.60、MERT 0.92；GuitarSet: MuQ 8.40、MuQ cos 0.91；MAESTRO: MERT 0.96。
- **编辑任务**：构造成对原始/修订 MIDI 与真值音频，Slakh 668 对，POP909 882 对(钢琴 Salamander 音色，含干声与混响)。评估请求增删的召回 R_add 与未变音符保持 F_keep，以衡量在改变目标内容时对未改音符和音色的保持。
- **效率与训练**：在 17 个公开器乐数据集、660 小时表演 MIDI + 48 kHz 单声道音频上训练，Adam 125k 步，有效 batch 80，峰值学习率 1e-4。GH200 上 MIDI-only 生成 20.48 s 音频约 0.93 s，峰值显存约 3.37 GiB。
- **基线**：CTD、P-MUSE、TokenSynth、FlowSynth、SpecDiff、MAC、U-MusT、MIDI-VALLE，以及适配的 FlowEdit。
- 论文还讨论了基于转谱的音符遵循度评估的局限。

## 一句话评价
SpanSynth-Edit 通过低帧率标量量化 latent 与保帧内时序的 MIDI Span 条件，在统一 flow-matching 框架下实现了多乐器混音的 MIDI 引导合成与免训练区域编辑，在音质、相似度与音符遵循度上表现有竞争力，并为细粒度音乐音频编辑提供了可复现基准。

---

## 19. XSQ-AST: An Explainable Audio Spectrogram Transformer Framework for Localising Synthetic Speech Artifacts

**作者**: Ben Heritage, Luca Resti, Mónica Villanueva Aylagas, Timothy Mehlenbacher, Konrad Tollmar, James Alfred Walker
**链接**: [2609.24770](https://arxiv.org/abs/2609.24770)
**分类**: Text-to-Speech (Speech Quality Assessment / Explainable AI) | **关键词**: XSQ-AST, Audio Spectrogram Transformer, synthetic speech artifacts, saliency detection, speech quality assessment, WhisperX, phoneme alignment, KDE

# XSQ-AST 论文总结

## 核心痛点
- 合成语音（TTS）中的局部伪影定位困难。
- 传统评估依赖 MOS 或全局客观估计，只有整体质量分数，可解释性差。
- 随着零样本神经编解码模型和扩散模型接近人类语音，全局自然度分数趋于饱和，但局部瞬态不连续、局部失真、韵律漂移等仍待解决。
- 现有细粒度方法如 Kuhlmann 等需要修改训练目标或分段一致性约束，依赖帧级质量标注或专门训练目标。

## 方法创新
- 提出 XSQ-AST，将 SQ-AST 语音质量模型与 WhisperX 音素对齐及多种显著性方法结合，无需重新训练即可生成时间局部化的伪影诊断。
- 支持在 MOS、Noisiness、Discontinuity、Colouration、Loudness 五个感知维度上分析。
- 输入预处理：音频需大于 2 秒，多声道拆分为单声道，重采样至 48 kHz，对超过 10 秒音频按 1.5 秒重叠分段；使用 Mel 滤波器组特征提取并归一化。
- 显著性提取：Raw Attention、Attention Rollout、Attention Flow 以及适配回归任务的 GradCAM；GradCAM 对最后一层 Transformer 梯度取平均，并以得分 1 作为回归置信度代理。输出时频块显著性图，缩放、裁剪并插值到 Mel 特征尺寸。
- ASR 与音素对齐：将低于阈值样本降采样至 16 kHz，加 1 秒静音拼接，用 WhisperX 检测语言、转写、置信度与音素对齐，获得 PPG，用于 PDSM。
- 语句级报告：通过 sum、mean、median、max、ℓ1、ℓ2 池化得到 PDSM，默认突出显示 top 10% 问题音素；用 KDE 将显著性映射为时间与频率上的平滑分布，并与波形和转写对齐展示；绘制 ASR 置信度；输出 KDE 平坦度指标以区分局部问题与整体质量伪影。
- 系统级报告：输出 TSV 分数、排序 TSV、小提琴图与柱状图、系统级频率 KDE、维度相关性热图、ASR 置信度分布、问题音素对直方图等。

## 实验与结果
- 听测：40 名参与者，其中 20 女、19 男、1 其他；平均年龄 32.8 岁，SD=8.1，范围 24-55；无确诊听力障碍。
- 刺激：从 VoiceMOS 2022 数据集手工挑选 30 个具有局部时间伪影、低 KDE 平坦度且合成方法和评分有差异的样本。
- 流程：参与者标注转写波形中对应维度有问题的区域，聚合归一化后与模型 KDE 比较；离散数据用于 PDSM。
- SQ-AST 分数验证：感知影响均值与 SQ-AST MOS 显著负相关（Spearman ρ=-0.638，p=0.0001）；维度特定分数较弱（ρ=-0.373，p=0.042）。
- 时间定位：比较各显著性方法 KDE 与听测 KDE。整体中位 Spearman ρ 最高为 Attention Rollout（0.444），其次 GradCAM+（0.403）和 Attention Flow（0.378）。Rollout 与 Flow 相对 Raw attention 和 GradCAM- 显著更高（p<0.001）；GradCAM+ 类似（p≤0.001）。GradCAM+ 在 MOS（0.649）和 Loudness（0.625）上最高。
- PDSM 最佳组合：Overall 为 GradCAM+（ℓ1 norm, sum）ρ=0.634；MOS 为 Rollout（ℓ2 norm）0.469；Noisiness 为 Rollout（median）0.806；Discontinuity 为 Flow（ℓ2 norm）0.560；Colouration 为 Flow（ℓ2 norm）0.474；Loudness 为 Rollout（median）0.806。
- AUC-ROC 分析确认模型区分度高于随机。不同显著性方法适合不同伪影类型。

## 一句话评价
XSQ-AST 提供了一个无需重训练、可解释且能时间与音素级定位合成语音伪影的实用框架，并通过 40 人听测验证了其与人类感知定位的一致性，但性能依赖阈值设置、预训练模型和特定数据集，跨语言、跨系统与实时部署仍需进一步验证。

---

## 20. Morpho-VITS: Variational Inference with Morphological Modeling for End-to-End Speech Synthesis of a Tonal Bantu Language

**作者**: Antoine Nzeyimana
**链接**: [2609.24310](https://arxiv.org/abs/2609.24310)
**分类**: Text-to-Speech | **关键词**: Text-to-Speech, Bantu tone, Morphological modeling, Kinyarwanda, VITS, Variational Inference, Phoneme-to-morpheme cross-attention

# Morpho-VITS 论文总结

## 基本信息
- 标题：Morpho-VITS: Variational Inference with Morphological Modeling for End-to-End Speech Synthesis of a Tonal Bantu Language
- 作者：Antoine Nzeyimana（University of Massachusetts Amherst, USA）
- 领域：端到端语音合成（TTS）、声调语言建模

## 核心痛点
- 班图（Bantu）声调语言的 TTS 质量长期偏低，主要因为声调系统同时受词汇（词、词干、词缀）和语法（形态句法）影响。
- 标准正字法通常省略声调符号和音节时长信息，读者需要依赖上下文消歧；这使非母语者和 TTS 系统都难以产生正确声调，合成语音常被感知为“非母语口音”。
- 以基尼亚卢旺达语（Kinyarwanda）为例，声调既由词汇过程也由语法过程产生，且具有自主音段性质；声调与形态之间存在双向关系：声调有助于形态消歧，形态也有助于预测声调。

## 方法创新
- 提出 Morpho-VITS：在 VITS/VITS2 架构中，用形态句法先验增强文本编码。
- 替换标准音素编码器为两个模块：
  1. 词素序列编码器（morpheme encoder）；
  2. 音素到词素的交叉编码器（phoneme-to-morpheme cross-encoder）。
- 每个音素通过交叉注意力关注同一词内词素的隐藏表示，从而同时捕获词汇与形态句法模式，以预测正确声调。
- 前端处理：使用音节分词器得到元音和辅音簇作为音素序列，同时用形态分析器把词切分为词素序列。
- 交叉编码器借鉴机器翻译 Transformer 解码器，但改为双向；包含音素自注意力（MHA1）和音素到词素交叉注意力（MHA2），并加入相对位置偏置；交叉注意力通过 stk(i,j) 限制在同一词/token 内。
- 整体仍基于 VITS 的条件 VAE、ELBO、MAS、flow、时长预测器、说话人编码器与轻量波形解码器。

## 实验结果
- 数据：多说话人 Kinyarwanda TTS 语料，包括 Mbaza NLP 6 小时新闻朗读（1 说话人）、农业 TTS 数据 20 小时（4 说话人）、此前语音-文本对齐项目 38.5 小时。
- 形态分析器：基于二层次形态学、Rust 实现，使用词干数据消解动词形式，HMM 词性标注与双向解码，在 AfriSUD POS 基准上达到 85% 准确率。
- 模型：PyTorch 2.7.1；音素隐藏维度 192，8 层音素编码器/交叉编码器，第 3 层加入说话人条件；词素编码器 8 层、768 维。基线 VITS 约 97M 参数，Morpho-VITS 约 268M 参数（其中 169M 为词素编码器）。
- 训练：1M 梯度更新步，batch size 32，峰值学习率 1e-4，4 张 RTX 5090，基线约 96 小时，Morpho-VITS 约 149 小时。
- 评估：用 ASR 评估可懂度，从新闻语料收集 10,000 句 Kinyarwanda 句子，每句 6-12 词，剔除含人名的句子。
- 结果：摘要指出形态建模带来显著 TTS 改进，具体提升自然度、语调与可懂度；表 1 给出 VITS baseline 与 Morpho-VITS 的 ASR 可懂度对比（片段截断，未展示完整数值）。

## 一句话评价
Morpho-VITS 通过显式词素建模和音素-词素交叉注意力，为声调班图语言的端到端 TTS 提供了一种有语言学依据的方案，初步实验显示能提升自然度、语调和可懂度，但完整结果与更广泛语言验证仍需进一步考察。

---

## 21. StreamTN: A Low-Latency Streaming Chinese Text Normalization Model for Streaming TTS in Dialogue Systems

**作者**: Wenhao Li, Jinrui Liang, Haoyu Zhang, Jingbin Hu, Xiaming Ren, Hanke Xie, Huakang Chen, Chengyou Wang, Dake Guo, Linhan Ma, Su Feng, Houdun Liu, Yunxiang Chen, Lei Xie
**链接**: [2609.24267](https://arxiv.org/abs/2609.24267)
**分类**: Text-to-Speech (Text Normalization for Streaming TTS) | **关键词**: Chinese Text Normalization, Streaming TTS, Spoken Dialogue Systems, Low-Latency Inference, Dual-Track Streaming, Large Language Models, Non-Standard Words, Qwen3-0.6B

# StreamTN：面向对话系统流式 TTS 的低延迟中文文本归一化模型

## 核心痛点
- 在 LLM 中心的级联口语对话系统（SDS）中，LLM 生成回复常包含非标准词（NSW），如数字、日期、时间、电话、单位、化学式、数学表达式等，直接送入 TTS 会导致误读、韵律异常甚至合成失败。
- 传统工业 TN 依赖手工规则、正则和 WFST 语法，可控性强但需要大量语言特定工程，对未见模式泛化差。
- 纯神经 TN 可能产生罕见但严重的不可恢复错误，对 TTS 尤其危险。
- 基于 prompt 的 LLM TN 通常需要等待足够或完整上下文，首 token 延迟高，并存在幻觉、格式不稳定等风险；若将核心 LLM 专门微调用于 TN，还可能损害其通用智能与推理能力。
- 流式对话场景要求 TN 模块增量处理 LLM 的部分输出，并以可控的首包延迟向 TTS 提供规范化文本。
- 现有 TN 数据集与评估多聚焦离线句子级归一化或多语言 TTS 归一化，缺少面向 LLM 对话回复分布、多样性及流式延迟要求的基准。

## 方法创新
- 提出 StreamTN：一个轻量级、基于 LLM 的中文流式文本归一化模型，构建在 Qwen3-0.6B 之上。
- 引入双轨流式架构：原始文本输入 token 与规范化输出 token 被放入两个并行轨道，两轨嵌入融合后送入 Transformer backbone。
- 输入轨提供当前可用的原始文本上下文，输出轨携带延迟的规范化文本历史，使模型能够在消费上游新 token 的同时自回归生成规范化 token。
- 使用 token-delay 参数 d 控制首包延迟与可观察输入前缀长度：等待更多原始上下文有助于消歧，但会增加延迟；等待过少则可能产生错误读音。
- 对齐符号 <delay> 与 <pad> 作为概念性对齐符号，实现为零向量；两轨共享 Qwen3-0.6B 的 token embedding 空间，并通过逐元素相加融合。
- 训练时移除最后一个融合位置，使每个规范化目标由因果前序状态预测；输入流结束后对输入轨进行 padding，并继续基于输出历史生成，直到 EOS。
- 通过任务特定微调学习结构化归一化模式，不依赖复杂 prompt，降低幻觉风险。
- 构建面向中文对话场景的 TN benchmark，覆盖 14 个类别，包括数字、日期、时间、电话、单位等常见 NSW，以及化学式、数学公式等复杂科学表达。
- 作者计划在发表后开源训练好的 StreamTN 模型和配套 benchmark，并提供在线演示。

## 实验结果
- 摘要声明实验验证了 StreamTN 在准确率和推理延迟方面的有效性。
- 与规则系统和通用 LLM 相比，任务特定微调带来更优的 TN 性能和更少幻觉。
- 在低首包延迟下取得有竞争力的归一化质量，并且当可获得额外上下文时，性能进一步提升。
- 但所提供的论文片段在实验细节之前被截断，未包含具体数据集规模、准确率、延迟数值、消融实验或基线对比数据；因此无法依据当前片段核实量化收益。
- 论文承诺发布模型、benchmark 和在线演示，便于复现与后续研究。

## 一句话评价
StreamTN 将轻量 LLM 与双轨延迟流式建模引入中文 TTS 前端文本归一化，针对级联口语对话系统的低延迟、流式输入输出需求给出实用架构，并补充了对话场景 TN 基准；其核心价值在于把 TN 从离线预处理重构为可控制首包延迟的流式模块，但仍需完整实验数据验证其泛化性、鲁棒性与实际部署收益。

---

## 22. Listen, Critique, and Refine: RL-Based Self-Refinement for Instruction-Following Speech Synthesis

**作者**: Chee-En Yu, Yi-Cheng Lin, Sung-Feng Huang, Yun-Shao Tsai, Ho-Lam Chung, Xuanjun Chen, Hung-yi Lee
**链接**: [2609.24163](https://arxiv.org/abs/2609.24163)
**分类**: Instruction-Following Text-to-Speech / Speech Synthesis | **关键词**: Large Audio Language Models, Instruction-Following TTS, Reinforcement Learning, GRPO, Self-Refinement, Audio-Token Reasoning, Speech Synthesis

# Listen, Critique, and Refine: RL-Based Self-Refinement for Instruction-Following Speech Synthesis

## 核心痛点
- 大型音频语言模型（LALMs）虽能根据自然语言指令合成指定风格的语音，但复杂指令要求同时控制音高动态、语速和情感语调时，单次生成往往只能满足部分声学属性。
- 文本 LLM 中的自反思（self-refinement）已被证明能提升生成质量，但该范式在音频生成中尚未探索；音频生成不仅需要生成，还需要模型“听”自己的合成语音并进行批评。
- 已有音频推理工作主要集中在音频理解任务，推理轨迹本身仍是文本 token，音频仅作为输入；而语音生成任务需要模型批评并修正自己的声学输出。
- 现有基于 RL 的 Instruct TTS 方法虽使用情绪准确率、说话人相似度、LALM-as-a-judge 等奖励，但未利用模型自身的推理能力。

## 方法创新
- 首次将推理范式扩展到音频 token 生成，训练单个 LALM 在文本和音频两种模态上推理，形成统一的“生成—批评—精炼”闭环。
- 两跳推理流程：
  1. Pass 1：根据风格指令 s 和文本内容 t 生成初稿语音 token v1，作为音频 token 空间中的初始推理。
  2. Critique：模型“听” v1，并结合 s 与 t，生成文本批评 c，指出初稿语音与指令之间的声学不匹配。
  3. Pass 2：以 s、t、v1 和 c 为条件，生成精炼后的语音 v2。
- 使用 GRPO 进行 RL 训练。对每个训练 prompt 采样 G 个 rollout，每个 rollout 生成 v2，并用奖励函数评分，组内归一化计算优势。
- 引入 refinement-aware reward：除绝对风格奖励 CLSP(v2,s) 外，还加入改进项 Δ = CLSP(v2,s) - CLSP(v1,s)。由于 GRPO 中组内所有 rollout 共享同一 v1，线性 Δ 中的 CLSP(v1,s) 会在组均值减法中抵消，因此作者用 tanh 非线性变换保留相对改进信号：tanh(α·Δ) 在减去组均值后不会像线性项那样完全抵消。
- 奖励函数还包含 WER 惩罚项 max(0, WER(v2,t) - WER(v1,t))，防止风格提升以牺牲内容准确率为代价。
- 训练时对策略模型应用 LoRA，基础模型冻结为参考分布 pref，以便高效计算 KL 正则项；推理时使用参考说话人池缓解参考说话人条件带来的性别不匹配问题。
- 音频反 tokenization 时，若指令包含性别关键词则选择对应性别参考说话人，否则选择 CLSP 分数最高的参考语音。

## 实验结果
- 训练数据：使用 ParaSpeechCaps，随机采样 1000 条英语语音与描述性 caption，过滤初稿 WER 超过 0.10 的样本；每个样本包含风格指令 s、参考文本 t、预计算初稿音频 token v1 以及奖励函数所需的 CLSP(v1,s) 与 WER(v1,t)。
- 评测基准：InstructTTSEval，包含 3000 个指令—语音对，覆盖 Acoustic-Parameter Specification（APS）、Descriptive-Style 等三类任务。
- 主要结果：经 RL 训练后的两跳精炼输出在 InstructTTSEval 上取得 7.15% 的相对提升，验证了模型的反思能力。
- 相比零样本设置，精炼输出在平均 CLSP 上相对提升 6.5%，在 LALM-judge 风格一致性上相对提升 7.2%。
- 精炼输出优于零样本基线和经过 RL 训练的一跳基线，说明 critique-refine 机制带来了超越单纯 RL 微调的额外收益。
- 代码链接：https://github.com/CheeEn-Yu/ReflectTTS

## 一句话评价
本文首次将推理范式扩展到音频 token 生成，通过 RL 让单个 LALM 自听、自评、自改，在指令跟随 TTS 上取得可验证提升，但当前证据主要基于截断的实验设置，仍需进一步关注泛化性、计算开销与评价可靠性。

---

## 23. P2Flow: Phoneme-aware Progressive Flow Matching for Extreme Speech Super-Resolution

**作者**: Ningyuan Yang, Yize Li, Pu Zhao, Diego A. Cuji, Kanad Sarkar, Ryan M. Corey, Xue Lin, Andrew C. Singer
**链接**: [2609.24138](https://arxiv.org/abs/2609.24138)
**分类**: Speech Super-Resolution | **关键词**: Extreme Speech Super-Resolution, Flow Matching, Phoneme-aware, Progressive Frequency Modeling, Vocoder Post-training, Generative Models

# P2Flow: Phoneme-aware Progressive Flow Matching for Extreme Speech Super-Resolution 论文总结

## 1. 核心痛点
- 现有语音超分辨率（SSR）研究多关注标准或通用配置，例如 8 kHz→16 kHz 或任意输入采样率→48 kHz；极端 SSR（1 kHz/2 kHz→16 kHz）研究明显不足。
- 极端条件下输入频谱信息严重缺失，现有方法性能显著下降。图1显示，随着上采样比例从 2× 增加到 16×，感知得分明显下降，说明高频恢复在声学和音素线索不足时非常困难。
- 该问题在骨传导传感等实际应用中具有重要意义，因此需要专门针对极端 SSR 的解决方案。

## 2. 方法创新
P2Flow 基于 few-step flow matching，提出三项核心策略：

### (1) 音素引导 Phoneme Guidance
- 训练一个 HuBERT 编码器加线性头的帧级音素分类器，采用 TIMIT 61-to-39 音素映射。
- 分类器在同样退化的 SSR 输入上训练；LR 信号先重采样到 16 kHz 并归一化，再将 HuBERT 特征从 20 ms 步长插值到 16 ms 的 mel 帧步长。
- 输出帧级音素后验 p_ph ∈ R^{B×39×T}。在 SSR 训练时冻结分类器，用 p_ph 作为语言条件，引导高频频谱重建。

### (2) 渐进式频率建模 Progressive Design
- 将缺失频带重建分解为三个频段：0–2 kHz、2–4 kHz、4–8 kHz，实现分层恢复。
- Flow matching 路径：μ_t = t m_H + (1-t) m_L，σ_t = 1-(1-σ_min)t，m_t = μ_t + σ_t ε，目标速度 u_t = (m_H-m_L) - (1-σ_min)ε。
- 将流状态 m_t、LR 条件 m_L、音素后验 p_ph 拼接并线性投影为 h0；随后由三个 Transformer 模块 M1/M2/M3 依次精炼，层数分别为 4/2/2，隐藏维 1024。
- 每个 Transformer 层包含时间条件自适应 RMSNorm、16 头自注意力（每头 64 维）、query-key RMSNorm、旋转位置编码，以及带残差的 GEGLU 前馈网络。
- 采用倒金字塔设计：M1 容量更大，因为第一模块需要从最有限的信息中推断频谱结构，后续模块受益于逐渐丰富的特征。
- 每个 M_k 后接轻量速度头 H_k，分别预测低频、中频、高频 mel 区域的速度；三个预测组成完整 80-bin 速度场，损失为各频段速度均方误差之和。
- 推理时从 m0 = m_L + σ ε 初始化，沿 ODE 从 t=0 积分到 t=1，估计 HR mel。

### (3) 声码器后训练 Vocoder Post-training
- 采用 SpeechBrain HiFi-GAN 声码器进行 mel 到波形合成。由于声码器在自然 mel 上预训练，而 FM 估计的 mel 存在分布不匹配，需要后训练。
- 固定 FM 模型，在固定 mel 估计上后训练生成器，并联合训练判别器；损失包括对抗损失、特征匹配损失和多分辨率 STFT 损失。
- 权重设置为 (λ_adv, λ_feat, λ_STFT) = (1,10,1)，使用三种 MR-STFT 分辨率：(512,128,512)、(1024,256,1024)、(2048,512,2048)。
- 整体训练分三步：音素分类器训练 → 冻结其他模块训练 FM → 声码器后训练。

## 3. 实验结果
### 数据集与设置
- 使用 TIMIT 官方 train/test 划分，以及 VCTK 的 100/8 说话人 train/test 划分。
- 极端 SSR 设置：1 kHz→16 kHz 和 2 kHz→16 kHz。
- LR 输入由 16 kHz 真值经 Chebyshev Type-I 低通滤波后下采样生成。
- 使用 80-bin mel 频谱，帧长 1024，帧移 256。
- 音素分类器训练 20 epochs；FM 模型训练 400k iterations，batch size 128，学习率 3e-4；声码器微调 20 epochs；FM 默认使用 5 步采样。
- VCTK 音素标签由 Montreal Forced Aligner 生成，并映射到 TIMIT 39 音素集。

### 评价指标
- LSD↓、LSD-LF↓、LSD-HF↓、ViSQOL↑、STOI↑。

### 主要结果
- TIMIT 表1：P2Flow 在 1 kHz→16 kHz 下取得 LSD 1.026、LSD-HF 1.041、ViSQOL 3.434、STOI 0.849；在 2 kHz→16 kHz 下取得 LSD 0.935、LSD-HF 0.997、ViSQOL 3.954、STOI 0.908，多项指标达到最优。
- 对比基线包括 AudioUNet、NU-Wave 2、UDM+、AERO、EBEN、AP-BWE、FLowHigh、UniverSR。
- 图1显示，在 VCTK 固定 16 kHz 目标下，随着上采样比例 2×/4×/8×/16× 增加，P2Flow 的感知得分优于标准与极端设置中的代表性方法。
- 图3的 2 kHz→16 kHz 频谱图对比表明，P2Flow 的高频恢复更接近参考。
- 消融研究验证了音素引导、渐进式频率建模和声码器后训练各自的贡献。

### 局限与待补充
- 由于输入片段被截断，未包含完整 VCTK 结果表、全部消融细节和推理效率分析。
- 方法主要面向 16 kHz 目标，依赖音素标签和声码器后训练。

## 4. 一句话评价
P2Flow 通过音素引导、分频段渐进式 flow matching 与声码器后训练，在 1/2 kHz→16 kHz 极端语音超分辨率任务上于 TIMIT/VCTK 取得多项指标 SOTA，是极端 SSR 场景下兼顾感知质量与可懂度的有效方案。

---

## 24. The design of an optomechanical microphone using a photonic waveguide interferometer

**作者**: Xiaoyu Niu, Yuqi Meng, Zihuan Liu, Ehsan Vatankhah, Neal Hall
**链接**: [2609.24073](https://arxiv.org/abs/2609.24073)
**分类**: Optomechanical MEMS Microphone / Integrated Photonic Acoustic Sensing | **关键词**: optomechanical microphone, photonic waveguide interferometer, Mach–Zehnder interferometer, MEMS microphone, signal-to-noise ratio, dynamic range, minimum detectable pressure, acoustic overload pressure

## 论文总结

### 核心痛点
- 商用MEMS麦克风主要依赖电容或压电读出，噪声主要来自背板、后腔和ASIC；高压输入阻抗放大还会引入电子噪声。
- 已有光栅/自由空间光学麦克风可降低背板热机械噪声并规避ASIC噪声，但仍需评估光电探测与后续电子噪声、散粒噪声。
- 已有光波导麦克风被演示，但其关键品质因数（SNR、AOP、DR、MDP等）未被细致讨论；本文旨在从MEMS麦克风视角系统分析，并判断该光机架构在常规应用中是否优于SOTA。

### 方法创新
- 提出**隔膜集成光子波导Mach–Zehnder干涉仪（MZI）**光机麦克风：声压使MEMS隔膜变形，在传感波导中引入应变，改变光程长度；参考MZI臂位于衬底，传感MZI臂位于膜上。
- 使用片上MMI分束/合束；输出光功率随瞬时位移变化，可表示为 L = L0/2[1+cos(2πh/λ)]，光电探测器电流 i = Rop·ME·L。
- 光学灵敏度 Sop = π/λ·√(ME·Rop·L0)，最小可探测位移 MDD = λ/π·√(q/(ME·Rop·L0))，动态范围 DR = 65%·π/2·√(ME·Rop·L0/q)，AOP由10% THD定义，对应65%·λ/2光程差摆幅。
- 架构无需背板和高压输入阻抗ASIC，有望降低背板热机械噪声与ASIC噪声；但仍需纳入散粒噪声、光电探测器噪声和后续电路噪声。
- 支持异质集成：可将波导、激光器、光电探测器集成在单芯片上；边缘发射激光器比VECSEL更适合异质集成。

### 实验结果/设计分析
- 论文分析光学与机械换能机制及关键FOM：SNR、动态范围、声学过载压力、最小可探测压力。
- 考虑两个设计案例：MEMS麦克风与测量麦克风。
- 结果：在常规应用中具有竞争力，但相较当前SOTA麦克风没有显著整体优势；可能优势在于高温和其他恶劣环境传感。
- 与2014年光栅光学麦克风对比：封装尺寸4.14 mm × 4.15 mm × 1.38 mm，噪声底22.00 dBA，SNR 72 dB；注意如今SOTA电容MEMS已显著改善。
- 概念噪声对比：波导麦克风可消除背板与ASIC噪声；但仍需评估光电探测器、后续电子噪声与散粒噪声。

### 一句话评价
本文系统评估了隔膜集成光波导MZI光机麦克风的FOM，证明其在常规音频应用中未必超越SOTA，但在高温/恶劣环境与集成光子集成方面具有潜在价值。

### 备注
- 论文片段截至动态范围与输入参考噪声讨论附近，后续机械灵敏度与完整实验结果未包含。

---

## 25. AURA: Uncertainty-Routed Activation Editing for Acoustic Grounding in Speech Foundation Models

**作者**: Natarajan Balaji Shankar, Zilai Wang, Zihan Wang, Mohan Shi, Kaiyuan Zhang, Abeer Alwan
**链接**: [2609.23979](https://arxiv.org/abs/2609.23979)
**分类**: Speech Recognition | **关键词**: Speech Foundation Models, Automatic Speech Recognition, Hallucination Mitigation, Representation Editing, Parameter-Efficient Fine-Tuning, Uncertainty Routing

### 论文信息
- 标题：AURA: Uncertainty-Routed Activation Editing for Acoustic Grounding in Speech Foundation Models
- 作者：Natarajan Balaji Shankar, Zilai Wang, Zihan Wang, Mohan Shi, Kaiyuan Zhang, Abeer Alwan
- 机构：加州大学洛杉矶分校电子与计算机工程系
- 代码：https://github.com/balaji1312/aura

### 核心痛点
- 注意力编码器-解码器（AED）语音基础模型在干净 ASR 上表现强，但在无语音、弱声学证据、不可靠转写或 underrepresented 说话人/领域等输入下，会生成声学上不被支持的流畅文本，即幻觉。
- 根因是 AED 自回归解码器依赖内部语言模型先验；当 cross-attention 弥散、过度集中或非单调时，声学 grounding 失败。
- 现有 PEFT 如 LoRA 仍引入百万级可训练参数；表示编辑方法如 JoLA 使用静态门控，每个解码步施加相同编辑，无法处理幻觉的局部性。
- 目标是在超高效 PEFT 预算内，针对解码器 cross-attention head 的局部 grounding 失败进行动态干预。

### 方法创新
- 提出 AURA（Activation-editing with Uncertainty-Routed Adaptation），冻结预训练 AED 模型，仅在 decoder cross-attention heads 上应用稀疏 scale-and-shift 激活编辑。
- 每个 head 引入乘性尺度 A_h 与加性偏置 v_h；门控为零时可精确恢复冻结输出，允许加性、乘性、联合或不干预。
- 静态 Hard-Concrete gate 做稀疏 head 选择，由 L0 正则驱动，决定哪些 head 可被编辑；位置参数初始化接近未承诺状态。
- 动态不确定性路由门从 cross-attention 分布提取三个因果特征：Max-Prob（过度集中/attention sink）、Entropy（弥散、弱 grounding）、Shift（相邻解码步 attended frame 突变）。每 head 仅增加 4 个可训练标量，使用单层投影且权重初始化为零。
- 有效门为静态 head 选择门与动态 uncertainty 门的乘积，分离“在哪里编辑”和“何时编辑”：静态选 head，动态在声学不确定步增强编辑，在自信对齐时保持休眠。
- 不需要预先识别 hallucination head，直接插入 cross-attention 模块。

### 实验结果
- 在四个数据集上评估，覆盖非语音幻觉和语音 grounding stressors，包括 imperfect-label 儿童语音、imperfect-label 成人语音与 disfluent speech。
- 非语音音频上，幻觉率从 89.18% 降至 1.94%，且无需先验 hallucination-head identification。
- 在 imperfect-label 语料上，AURA 接近 LoRA 的 WER，同时可训练参数约少 500 倍。
- 与 LoRA、full fine-tuning、BitFit、RED、LoReFT、JoLA 等比较，是首个系统探索表示编辑作为 ASR 超高效 PEFT 的工作。
- 敏感性分析、特征消融和 cross-attention 可视化与 AURA 的不确定性路由对齐编辑行为一致；保持 clean-speech accuracy，同时揭示 accuracy-hallucination 权衡。
- 支持动态激活编辑作为 AED 语音模型 grounding 的实用路径。

### 一句话评价
AURA 通过仅在 cross-attention 不确定时对少量 decoder head 做动态 scale-and-shift 编辑，以约 500 倍少于 LoRA 的参数显著抑制非语音幻觉，是超高效 PEFT 与声学 grounding 结合的有前景方案。

---

## 26. Synthetic speech detection in Brazilian Portuguese through accent-related features

**作者**: Pedro H. L. Leite, Pedro Benevenuto Valadares, Luiz Wagner Pereira Biscainho
**链接**: [2609.23807](https://arxiv.org/abs/2609.23807)
**分类**: Speech Anti-Spoofing | **关键词**: Brazilian Portuguese, Synthetic Speech Detection, Accent-related Features, Anti-Spoofing, Phonetic Feature Extraction

## 核心痛点
- 主流商业与开源 TTS 模型难以模拟巴西葡萄牙语（pt-BR）的区域语音多样性，常将不同方言聚合为单一训练分布，生成“稀释”口音，产生音韵模糊，与自然社会语音实现脱节。
- 语音合成快速发展带来音频深伪、社交工程、金融欺诈和绕过 ASV 等安全威胁；现有 anti-spoofing 基准在未见生成模型上存在泛化差距，且在 pt-BR 上性能下降，因为缺乏大规模口音标注数据。

## 方法创新
- 提出一种基于“口音实现一致性”的语音深伪检测方法，将 TTS 训练流程中的音韵不一致性作为反欺骗声学线索。
- 构建定制数据集：自然侧 364 名说话人，来自多个语料库，覆盖多方言和多种录音链；合成侧 57 个 TTS 声音，来自 8 个提供商（商业：Azure、Google、OpenAI、ElevenLabs；开源：F5-TTS、Qwen3-TTS、Piper、Kokoro），均合成相同的 50 个句子。
- 特征提取：使用 ZIPA 作为时间戳提取/对齐器并提供音素实现 logits，结合 PhoneticXeus 进行集成分类；对辅音消歧，对元音评估共振峰空间，关注 /o/ 和 /e/ 的开口度及外语元音污染。
- 说话人级建模：跨多条话语聚合音韵特征，构建说话人语音画像，而非仅做话语级深伪检测；辅音特征为 40 维 ZIPA logits 向量加 6 个谱矩。
- 使用无监督核密度估计（KDE）基于特征分布差距区分自然与合成语音，特征可解释、轻量、低维。

## 实验结果
- 分析表明，在所提取的音素级特征上，自然语音与合成语音的分布差距足以通过无监督 KDE 进行区分，无需监督分类即可实现高精度可分离特征空间。
- 在 pt-BR anti-spoofing 数据集上的评估显示，这些可解释、轻量、低维特征能够提升基础模型在该任务上的性能，并在跨数据集 leave-one-out 设置中表现出泛化能力。
- 论文还进行了特征可解释性分析，从多个角度展示现代 TTS 在复现真实口音实现时可能失败的地方，并与传统口音分类和 anti-spoofing 数据集进行了基准比较。

## 一句话评价
该工作创新性地将 pt-BR 方言不一致性作为可解释、轻量级的音韵特征用于合成语音检测，为低资源语言的反欺骗检测提供了新视角，但尚需更大规模跨域实验验证其鲁棒性。

---

## 27. Generative Learning for Ambisonic Upscaling

**作者**: Amit Milstein, Nir Shlezinger, Boaz Rafaely
**链接**: [2609.23479](https://arxiv.org/abs/2609.23479)
**分类**: Ambisonic Upscaling | **关键词**: Ambisonics Upscaling, Generative Modeling, Flow Matching, Score-based Generative Model, Reverberant Speech, Spatial Audio

# 论文总结：Generative Learning for Ambisonic Upscaling

## 基本信息
- 标题：Generative Learning for Ambisonic Upscaling
- 作者：Amit Milstein, Nir Shlezinger, Boaz Rafaely
- 任务：Ambisonics Upscaling (AU)，即从低阶 Ambisonic 观测估计高阶 Ambisonic (HOA) 分量，以提升声场空间分辨率。
- 关键词领域：空间音频、Ambisonics、生成模型、混响环境。

## 核心痛点
- HOA 能提供更精细的空间细节，但采集 HOA 通常需要大型、昂贵且多传感器的麦克风阵列，限制实际部署。
- 传统 AU 方法多为模型驱动，例如平面波分解 (PWD) 加压缩感知 (CS)，依赖方向稀疏、少量声源、自由场或低噪声等假设。在真实混响场景中，晚期反射形成空间复杂、类扩散声场，违反稀疏假设，性能显著下降。
- 判别式深度学习方法通常学习低阶到高阶的确定性映射，难以刻画混响引入的随机空间结构，容易产生空间模糊的重建，丢失高频空间细节并降低感知沉浸感。
- 生成式方法此前在 AU 中应用很少，早期工作仅用 GAN 处理特定方向的单音信号。

## 方法创新
- 将 AU 重新定义为生成任务，而非确定性重建：给定观测到的低阶 Ambisonic 信号，建模缺失高阶空间分量的条件分布，从而应对混响声场中的固有歧义和随机性。
- 引入两类主流连续时间生成范式：Score-based Generative Model (SGM) 与 Flow Matching (FM)。SGM 通过 score 估计驱动反向扩散来重建目标分布；FM 学习确定性向量场，将样本从噪声先验传输到目标 HOA 分布，具有更好的训练稳定性和采样效率。
- 提出目标性重建策略：保留已测量的低阶 Ambisonic 分量，仅让生成模型合成缺失的高阶通道。该设计既利用观测数据的物理可靠性，又将生成能力集中在欠定的空间细节上。
- 结合灵活的分层架构与物理启发的重建约束，生成空间一致的 HOA 表示。

## 实验与结果
- 论文进行了广泛的数值研究，在多种声学场景下与当前最优基线方法进行比较。
- 还开展了主观听音测试，评估所提生成框架在不同混响场景中的感知质量和空间准确度。
- 核心结论：Flow Matching 在所有混响设置中持续优于判别式对应方法和基于扩散的生成范式 (SGM)。
- 由于提供的论文片段只包含摘要与引言，具体实验配置、数值指标和消融细节未完整给出。

## 一句话评价
该工作将 Ambisonic 上采样从确定性反问题转向条件生成问题，并使用 Flow Matching 在混响场景中取得更优的空间重建表现，是空间音频生成方向具有潜力的研究。

---

## 28. Long-Tail Rebalancing for Non-Verbal Vocalization-Aware ASR: A Track~1 System for the NVVSpeech Challenge

**作者**: Shangyue Jia, Jingru Ma, Yangzhuo Li, Daoping Luo, Bowen Tian, Hanchen Lu, Wenze Ren, Yunxiang Chen, Houdun Liu, Shuo Feng, Lei Xie, Liumeng Xue
**链接**: [2609.23462](https://arxiv.org/abs/2609.23462)
**分类**: Speech Recognition | **关键词**: Non-Verbal Vocalization, NVV-Aware ASR, Long-Tail Rebalancing, Cross-Dataset Label Harmonization, Category Sampling, Qwen3-ASR, NVVSpeech Challenge

### 论文信息
- **标题**：Long-Tail Rebalancing for Non-Verbal Vocalization-Aware ASR: A Track 1 System for the NVVSpeech Challenge
- **任务**：ISCSLP NVVSpeech Challenge Track 1，要求联合转写词汇内容与 16 类非语言发声（NVV）
- **作者/机构**：Shangyue Jia 等；南京大学、吉林大学、北京理工大学、台湾大学、深圳市派美科技、西北工业大学等

### 核心痛点
- 传统 ASR 主要关注词汇转写，常常忽略笑声、咳嗽、呼吸、哭泣等非语言发声，而 NVV 携带说话人状态、情感和对话动态等副语言信息。
- NVVSpeech Challenge 要求同时识别词汇与 16 类 NVV，但监督数据有限且类别分布严重长尾。
- 多源 NVV 数据集在事件清单、标注粒度、语言和采集流程上不一致，直接合并会造成标签语义混淆并放大类别不平衡；而完全展平类别分布也不一定能提升总体分数。

### 方法创新
1. **跨数据集标签统一（Label Harmonization）**：以官方 Track 1 的 16 类标签为共同目标空间，将源标签映射到官方类别；仅保留精确对应或人工验证过的近似映射，无法可靠映射的样本被排除。多事件 utterance 中每个事件标签独立归一化，但保留完整词汇-NVV 序列和原始事件顺序。
2. **基于幂次采样的类别重平衡（Power-based Category Sampling）**：在固定骨干、目标函数和输出格式的前提下，只改变样本分布 q。对类别 c 定义采样概率 p_c(α)=n_c^α / Σ_k n_k^α，α∈[0,1]。α=1 等价于自然/实例均匀采样，α=0.5 为平方根采样，α=0 为类别均匀采样。每个 utterance 以目标序列中第一个有效 NVV 标签作为采样类别键；仅 5.30%（1413/26648）训练样本含多个有效 NVV 标签。
3. **两阶段采样训练计划**：Stage 1 使用平方根类别采样对 Qwen3-ASR 1.7B 进行全参数微调，适度增加尾部类别曝光；Stage 2 从 Stage 1 checkpoint 继续，使用类别均匀采样微调，强化尾部类别。骨干、目标函数、目标序列化与词汇-NVV 序列格式保持不变。

### 实验与结果
- **骨干**：Qwen3-ASR 1.7B，全参数 SFT；bfloat16，global batch size 64，学习率 2e-5 线性衰减，warmup ratio 0.02，梯度裁剪 1.0；Stage 1 和 Stage 2 各训练 5 个 epoch；推理使用官方 Qwen3-ASR 实现与贪心解码。
- **数据**：共归一化 26,648 条 / 70.48 小时训练数据，来自 NonverbalSpeech38K、MNV-17、Burp data、NonverbalTTS、SMIIP-NV、SynParaSpeech、Emilia-NV、WESR-Bench，覆盖中英文。
- **验证集**：固定本地验证集 214 条（147 中文、67 英文，覆盖全部 16 类），来自 NonverbalSpeech38K 108 条、MNV-17 86 条、Burp data 20 条；另有官方测试集提交与 MNV-17 测试子集用于跨说话人泛化评估。
- **指标**：中文 CER、英文 WER、NVV 识别 F1、multi-event normalized tag distance (mNTD)、tagged-transcript error (Err.)；MNV-17 上报告 joint CER 与 NVV accuracy。
- **主要结果**：在固定本地验证集上，平方根类别采样在测试的单阶段设置中表现最佳；更强的重平衡并不单调更好。最终两阶段系统在官方 Track 1 获得 63.86 分，排名第四；但单阶段平方根模型在本地验证集上分数更高。

### 一句话评价
该工作从数据侧出发，通过跨数据集标签统一与“平方根采样 + 类别均匀微调”的两阶段策略，在有限且长尾的 NVV 监督下实现词汇与 16 类非语言发声的联合识别，验证了适度重平衡优于自然采样和完全均匀采样，并在 NVVSpeech Challenge Track 1 取得第四名。

---

## 29. Reducing Speaker Residual by Considering Pinhole Effect in Voice Anonymization

**作者**: Zeyan Liu, Weili Jiang, Liping Chen, Kong Aik Lee, Boyu Zhao, Kai Gao, Zhenhua Ling
**链接**: [2609.23433](https://arxiv.org/abs/2609.23433)
**分类**: Voice Anonymization | **关键词**: Voice Anonymization, Speaker Residual, Pinhole Effect, Linkability, Fine-tuning, Disentanglement, Speech Privacy

# 论文总结：Reducing Speaker Residual by Considering Pinhole Effect in Voice Anonymization

## 核心痛点
- 语音匿名化目标是在抑制说话人身份的同时保留语言内容与韵律，实现去标识化。
- 现有基于表示解耦的匿名化框架中，身份属性无法完美分离，会泄漏到内容与韵律表示中，形成“残余说话人属性”（residual speaker attributes），匿名化后仍可支持说话人识别或链接攻击（linkability）。
- 消除残余泄漏困难：说话人属性分布在多个特征流中，并与语音实现和韵律模式紧密耦合；更强的抑制容易损害可懂度、自然度和韵律保真度。
- 现有方法（codec-based、prosody-oriented、content-based、factorized distillation 等）往往只优化部分因子或依赖隐式瓶颈，缺少一个全局、显式、可优化的目标来一致地降低跨特征流的残余说话人属性。

## 方法创新
- 从“针孔效应”（pinhole effect）视角重新审视残余说话人属性：将匿名化视为把源说话人映射到共享伪说话人（针孔）的函数。残余属性表现为同一源说话人的匿名语音的聚类强度，聚类越强则链接性越高、隐私保护越弱。
- 提出 pinhole loss，用于对已训练好的语音匿名化框架进行微调：
  - 微调时对所有输入语音使用共享伪说话人特征，使残余说话人属性更直接地体现。
  - 对匿名语音提取说话人嵌入 e_{s,n}，计算全局均值 μ 和每个源说话人的均值 μ_s。
  - 定义类内散度 Rw 和类间散度 Rb。
  - Pinhole loss 定义为 L_Pinhole = tr(W^T Rb W) / tr(W^T Rw W)，其中 W 由广义特征方程 Rb w = λ Rw w 的前 k 个特征向量组成。
  - 该损失衡量不同源说话人匿名语音之间的相对可分性；最小化它即降低跨源说话人的可分性，从而抑制残余说话人属性、降低链接性。
- 微调策略：仅更新内容编码器、韵律编码器和波形生成器；用于损失计算的说话人编码器保持冻结。这一设计针对残余泄漏的主要路径——内容与韵律表示中的说话人信息，以及波形生成器在合成波形中表达的残余信息。微调时与原始生成目标联合优化，以维持合成质量和效用。

## 实验结果
- 评估遵循 VPC2024 配方：ASV EER 衡量隐私保护，ASR WER 衡量内容保留，SER UAR 衡量情感保留。
- 在三种匿名化框架上评估：x-vector based、ASRBN、ASRBN-GST。
- 评估多种伪说话人生成策略：Any-to-one (a2o)、Random selection (RS)、GAN-based (GAN)、Identity mapping with Diffusion (IDMap-Diff)。
- 数据集：LibriTTS train-clean-100/360/other-500 用于训练与微调；LibriSpeech dev/test 用于 ASV 与 ASR；IEMOCAP 子集用于 SER。
- 说话人编码器采用在 VoxCeleb2 上预训练的 ECAPA-TDNN，用于 ASRBN 与 ASRBN-GST 框架及微调过程。
- 微调时每批选择 S=6 个说话人、每个说话人 N_s=6 条语音，共 36 条。a2o 的伪说话人向量为 LibriTTS train-clean-100 中所有说话人向量的平均；RS 候选池来自该子集。
- 结果表明：在多种匿名化框架、伪说话人生成方法和数据集上，隐私保护一致提升，同时保持有竞争力的效用。

## 一句话评价
该论文从针孔效应出发，提出一种仅需微调已训练匿名化框架的 pinhole loss，以全局、显式的方式抑制跨特征流的残余说话人属性，在多个框架和数据集上实现了隐私与效用更好的权衡，为语音匿名化提供了一种通用且轻量的后处理式增强方案。

---

## 30. Low-Rank Frequency Convolution and Noise-Range Augmentation for Real-Time Pitch Estimation on Edge Devices

**作者**: Venkat Suprabath Bitra, Homayoon Beigi
**链接**: [2609.23340](https://arxiv.org/abs/2609.23340)
**分类**: Pitch Estimation | **关键词**: Pitch estimation, Low-rank convolution, Noise-range augmentation, Edge deployment, Frequency Convolution Network, TDNN-F

## 核心痛点
边缘设备上的单音高估计同时受三大约束：模型必须小、输入含噪时精度不能崩塌、必须在10 ms帧周期内产出结果。大型模型如CREPE、PESTO精度高但非为此场景设计。现有FrCN基线仅17,787参数，但仍有压缩空间，且噪声鲁棒性来源未被充分理解。评估划分更严格，按歌曲/说话人/歌手分组，域内指标低于此前轨道级划分，不可直接比较。

## 方法创新
1. **输入表示**：单帧VQT，16 kHz，hop 160（10 ms），269 bin，A0 27.5 Hz起，36 bin/octave，覆盖约7.4 octave至4790 Hz；四通道视图：原始幅度、log(1+αx)（α可学习）、除以帧和、除以帧RMS。
2. **低秩频率卷积**：将FrCN中H->H的膨胀卷积替换为瓶颈秩M的一对卷积（B: H->M，核5，同膨胀；A: M->H，核1）。块结构为 u=RMSNorm(x), z=RMSNorm(B*u), y=σ(A*z)+0.66x。H=18时M=9最优。参数从17,787降至11,397，减少35.9%，MACs减少39.5%。BatchNorm被两个沿通道轴的RMSNorm替代。TDNN-F的半正交约束被证明与瓶颈内归一化冗余，同时使用会降低精度。
3. **噪声范围增强**：在变换域加噪，C' = C + β sqrt(P_C/P_Cn) C_n，β~U(0,β_max)，对应SNR=-20log10β dB。训练噪声下限（β_max对应最差SNR）比架构更主导鲁棒性。
4. **边缘部署**：手写C kernel，仅需83 kB磁盘、仅依赖libc和libm。

## 实验结果
- 在MDB-stem-synth、PTDB-TUG、MIR-1K三个语料上，低秩分解后精度保持在RPA50的0.15个点以内；其中两个语料为未训练语料。
- 训练噪声下限从+6.02 dB降到-20 dB时，干净RPA50仅损失0.35个点，但-20 dB下RPA50从2.44提升到22.41，该效应比任何架构变化约大两个数量级。最佳设置位于部署预期条件约低一档处，而非越低越好。
- 运行时：eager PyTorch中低秩模型慢45%，编译kernel中快15%；C kernel在四个CPU上均快于OpenBLAS，比ONNX Runtime快3.8倍，比PyTorch快13倍。输出与PyTorch在每模型271,893个保留帧上逐帧核对，音高bin完全一致。
- 失败的探索：半监督学习、残差路径重参数化、CPU整数运算。

## 一句话评价
该工作通过低秩频率卷积在几乎不损精度的前提下压缩FrCN，并系统证明训练噪声范围而非架构是噪声鲁棒性的主导因素，配合极轻量C kernel实现了边缘端实时音高估计。

---

## 31. Signal-Informed Temporal Routing for Vinyl Defect Regime Detection

**作者**: Yi-Hung Kan, Homayoon Beigi
**链接**: [2609.23164](https://arxiv.org/abs/2609.23164)
**分类**: Audio Restoration | **关键词**: vinyl defect detection, audio restoration, temporal routing, expert ensemble, Viterbi decoding, regime classification, signal-informed features

# 论文总结：Signal-Informed Temporal Routing for Vinyl Defect Regime Detection

## 核心痛点
- 黑胶与档案音频修复中，退化并非单一噪声过程：包含孤立 click、宽 pop、短 scratch、密集 crackle、低频扰动和重叠损伤，不同缺陷对应不同修复策略（插值、inpainting、去噪或保持不变）。
- 经典 declicking 假设 x[n]=s[n]+c[n] 的稀疏脉冲模型，在微脉冲密集、缺陷重叠、音乐瞬态与损伤混淆时不可靠；单一 declick 分数无法决定区域应插值、inpaint、去噪还是保留。
- 修复前需要按“修复模式/regime”路由，而不仅是检测损伤。

## 方法创新
- 提出两阶段轻量检测器：信号知情前端 + 时间后端路由器。
- 前端：LPC 残差与二阶差分曲率正分量构成 core defect score；局部极大值产生 sparse 候选；帧级特征包括谱平坦度、高频比、谱扩展、倒谱能量、峰值因子、core-score 统计、峰值计数/密度等。三个独立二值 MLP 专家：sparse（候选级）、burst（帧级）、dense（帧级），输出互补证据 p_t=[P_s,P_b,P_d]，而非互斥类别概率。
- 后端：101 维输入 z_t=[p,c,i,u,g]，包含专家概率/置信度、成对差异/一致性、局部时间统计、原始帧描述子和候选密度滞后/超前；时间窗为 ±4 帧（非因果最多约 46 ms，适合离线修复前处理）。
- 分层路由：不直接五分类，而是分解为三个 softmax 阶段：clean vs defective；defect type τ∈{impulsive,dense,mixed}；impulsive 再分 sparse/burst。使用类别平衡交叉熵和每类子采样，避免 clean/dense 多数类主导 macro 目标。
- Mixed 校准：将 mixed 视为重叠状态，在 dense 证据不足或脉冲证据不足时抑制 mixed 后验；两轮阈值固定于验证集。
- 序列解码：Viterbi 最小化发射负对数似然 + 转移惩罚 C + 每帧类别偏置 B，抑制孤立低置信度翻转。参数采用 tune-then-refit：在 418 fitting + 70 validation 上选惩罚和 mixed gate，再在 488 development cases 上重拟合层级，冻结解码器后才读取 held-out 标签。

## 实验与结果
- 数据：受控合成 benchmark，来自干净音乐录音，按源录音划分，44.1 kHz、非重叠 15 s 片段。18 个 development recordings 产生 488 realizations（418 fitting + 70 validation），3 个 held-out recordings 产生 109，总计 597 段。五种注入配方：narrow clicks、wide pops、short scratches、dense crackle、mixed damage。挑战：真实转录无法提供样本级精确标签。
- 专家冻结结果：narrow clicks sparse F1 0.605；wide pops sparse 0.927、burst 0.899；short scratches burst 0.634；dense crackle dense 0.986；mixed damage sparse 0.577、burst 0.378、dense 0.975。表中 0 表示该配方无对应正类。
- 主结果：held-out 五类 pooled macro F1 = 0.730（95% CI 0.694–0.761），比 flat frame-level router 提升 0.043（paired bootstrap p=0.001）。clean 和 dense 帧高度可靠，sparse、burst、mixed 帧仍更模糊。四类视图合并 impulsive，匹配修复阶段消费。
- 不确定性：case-level bootstrap 4000 次重采样整段 excerpt；同一重采样 excerpt 上做配对系统比较。
- 消融/分析：贡献声称包括：分层分解 + 验证集选择转移惩罚优于 flat router 和 maximum-likelihood transition matrix；permutation analysis 表明专家证据流而非原始帧描述子承载路由决策；报告逐录音变异和可复现参考实现。

## 一句话评价
该论文把黑胶缺陷分析从单一检测推进为“修复导向的 regime 路由”，用互补专家证据 + 分层时序 Viterbi 解码在合成基准上取得稳定提升，但受限于小规模合成 held-out 集，稀疏、爆裂和混合状态仍是主要瓶颈。

---

## 32. Speech Language Models for Full-Meeting Speaker Diarization: Capabilities and Limitations

**作者**: Jialu Li, Jinchuan Tian, Shinji Watanabe
**链接**: [2609.23114](https://arxiv.org/abs/2609.23114)
**分类**: Speaker Diarization | **关键词**: Speech Language Models, Speaker Diarization, Full-Meeting Diarization, Token-based Diarization, Speaker Linking

# Speech Language Models for Full-Meeting Speaker Diarization: Capabilities and Limitations

## 核心痛点
- **SD 与 ASR 强耦合**：现有基于 SpeechLM 的说话人日志（Speaker Diarization, SD）方法大多与自动语音识别（ASR）紧密绑定，并使用词级（word-level）指标评估，导致无法将 SD 性能从 ASR 准确率中独立剥离出来评估。
- **评估场景受限**：许多 SpeechLM 风格的系统仅在短语音组或定长片段上评估 SD，缺乏对整场会议（full-meeting）场景的考察。
- **全程会议 SD 的特殊要求**：需要精确的活动预测，以及跨多个片段一致的录音级（recording-level）说话人身份，而不仅是局部的说话人分配。
- **依赖外部跟踪机制**：多数全程系统依靠 speaker-cache 或 cache-conditioned 跟踪机制来保证跨块说话人一致性，而非模型自身能力。

## 方法创新
- **任务形式化**：将 SD 建模为**以声学输入为条件的结构化 token 自回归生成**任务，基于开源 **ESPnet-SpeechLM**（decoder-only Transformer）实现，并与 ASR 解耦，直接在全会议 DER 下评估。
- **九流 token 格式**：输入波形被转换为 `x̃ ∈ N^{M×9}`，每帧包含 8 个 codec token + 1 个来自 **XEUS** 的 SSL token（25 ms 窗、10 ms 帧移）；输出 `ỹ ∈ N^{N×9}` 对齐填充为相同多流格式。使用含说话人 ID、时间戳、话轮转换 token、辅助任务标记的紧凑任务输出词表（最多 5 个说话人，时间戳覆盖每个 30 秒片段）。
- **两种输出表示对比**：
  - **Event-based（事件式）**：每个说话人话轮编码为五元组 `<spk1> <bot> <0.0> <2.0> <eot>`，时间戳量化到 0.1 秒；静音为 `<sil> <bot> ... <eot>`。
  - **Frame-based（帧式）**：每 0.1 秒输出一个 token（30 秒输入生成 300 个 token），并显式建模最多 3 人重叠（`<overlap_spk_1_2_3>`），超过 3 人时映射为 `<overlap_spk_4_more>`；引入 `<sc_start>`/`<sc_end>` 转换标记辅助自回归对齐说话人变化。
- **辅助任务注入**：在输出序列中联合建模 **SAD（语音活动检测）**、**OD（重叠语音检测）**、**STC（话轮计数）**，以 coarse-to-fine 方式（如 SAD→SD）为 SD 提供互补线索；这是此前 EEND 类模型探索过、但在 SpeechLM 式 token-based SD 中尚未被研究的。
- **训练/推理设置**：训练时以 30 秒片段、10 秒步长切分，推理时按不重叠 30 秒片段解码；采用 teacher forcing，对非填充的有效目标 token 位置按模态指示词表与任务输出词表加权计算交叉熵损失。
- **说话人链接分析**：显式分离时间维度的 SD 结构与录音级说话人跟踪，分析局部说话人假设与全局身份之间的差异。

## 实验结果
- **数据**：主要在 **AMI（IHM-Mix）** 上研究，并泛化到中文语料 **AISHELL-4** 与 **AliMeeting**（远场麦克风），另使用 3303.8 小时大规模模拟数据（基于 Switchboard-2/ Cellular、NIST SRE 2004–2008，2–5 人、重叠比例匹配真实会议）进行适配。
- **输出长度**：AMI 上 event-based 的 SD token 平均长度 40.0±21.0，而 frame-based 高达 323.2±15.7，后者序列显著更长、更易重复。
- **稳定性**：event-based 表示比 frame-based 表示产生更稳定、更一致的 SD 输出；frame-based 生成随输出序列增长而变得脆弱（brittle）。
- **任务编排**：将 SAD 和 OD 以 coarse-to-fine 方式排在最终 SD 任务之前，可一致地提升 SD 性能。
- **能力与局限**：SpeechLM 生成的输出确实编码了有用的时间维度 SD 结构，但全程会议 SD 仍受限于**录音级说话人跟踪**和**重叠相关漏检**；原始 SpeechLM 说话人符号表现为**局部说话人假设**而非录音级身份，而显式的说话人链接后处理能大幅降低说话人混淆。

## 一句话评价
本文把全程会议说话人日志从 ASR 中解耦出来，系统对比事件式与帧式 token 生成并引入辅助对话线索，证明 SpeechLM 能学到有用的时间结构、但尚不能胜任录音级说话人跟踪与重叠场景，指出了 token-based SD 走向可用所需的关键改进方向。

---

## 33. Adaptive Depth and Expert Refinement for Efficient Speech Enhancement

**作者**: Xikun Lu, Yujian Ma, Yunda Chen, Xianquan Jiang, Jinqiu Sang
**链接**: [2609.22824](https://arxiv.org/abs/2609.22824)
**分类**: Speech Enhancement | **关键词**: Speech Enhancement, Adaptive Computation, Early Exiting, Parameter Sharing, Conditional Expert Routing

# 论文总结：Adaptive Depth and Expert Refinement for Efficient Speech Enhancement

**作者/机构**：Xikun Lu, Yujian Ma, Yunda Chen, Xianquan Jiang, Jinqiu Sang；华东师范大学、深圳大学、Boin Hearing Technology 等。

## 核心痛点
- 多数神经语音增强系统对所有输入采用固定处理深度，即使较少细化步骤已足够，仍会产生不必要计算，推理成本高。
- 现有块复用/参数共享渐进增强方法（如 Kim et al.）通过重复使用同一处理块减少参数，但重复深度在推理时预定义且固定，无法按语句自适应。
- 仅做动态深度/早退仍无法解决全参数共享的灵活性不足：共享块在每轮被重复应用，而潜在表示随细化过程不断演化，需要状态相关的细化操作。
- 训练与自适应推理不匹配：全深度训练主要监督最终输出，中间状态主要靠后续细化间接优化，导致早退时中间输出可靠性不足。

## 方法创新
- 提出 ADER（Adaptive Depth and Expert Refinement），一个参数共享的渐进增强框架，实现输入依赖计算，核心由 ADC、CER、EIS 三部分组成。
- **共享渐进细化骨干**：沿用 MP-SENet 的幅度-相位前端与 TS-Transformer 块作为共享细化块，递归复用 K_max 轮；h0 作为初始状态，并由轻量上下文编码器提取声学上下文 a，供路由和深度控制使用。
- **条件专家路由 CER**：在每轮细化中，根据 h_{k-1}、共享块输出 z_k 和上下文 a 形成路由描述子，经路由器与温度 softmax 得到专家分布；采用 straight-through Gumbel Top-1 从 M 个轻量残差适配器中选择一个执行。适配器由 1×1 瓶颈、depthwise 3×3 卷积、1×1 输出投影和可学习残差尺度构成，主细化块保持共享。训练时用 Switch 风格负载均衡损失避免路由坍缩。
- **自适应深度控制器 ADC**：根据 h_{k-1}、h_k 和 a 预测继续概率 c_k，在 k≥K_min 后若 c_k<τ 则硬早停，使深度 N(x)∈{K_min,...,K_max}。训练目标由重建质量轨迹推导：计算每轮 Q_k，选择最早接近最优质量的迭代 N*，并仅在可达决策上以 BCE 训练 ADC。
- **退出感知中间监督 EIS**：训练时始终展开 K_max 轮，并均匀采样一个中间迭代 d，用完整增强目标直接监督该中间输出，缓解训练-推理不匹配。总损失为 L = L_MP + λ_EIS L_EIS + λ_bal L_bal + λ_ADC L_ADC，其中 λ_EIS=0.1、λ_bal=2.5×10^-4、λ_ADC=0.05。
- **两阶段训练**：前 40 个 epoch 预热，优化增强、中间监督和路由均衡目标，不启用 L_ADC；随后联合优化完整目标。训练时展开全部 K_max=5 轮，硬早退仅在推理时启用。

## 实验结果
- 在标准 VCTK-DEMAND 语料上评测，使用 824 条测试集，音频重采样至 16 kHz，STFT 窗长 400、帧移 100，密集通道维度 64，编码器深度 D=2；ADER 设置 K_min=2、K_max=5，并使用 4 个专家适配器（摘要截断处）。
- 相比 MP-SENet：ADER 将参数量减少 70.4%、平均计算量减少 51.3%，同时达到 WB-PESQ 3.37。
- 实验重点评估自适应计算、细化深度行为以及随迭代变化的专家路由，表明 ADER 能实现输入依赖的渐进细化并减少推理中的冗余计算。

## 一句话评价
ADER 通过共享渐进骨干、自适应深度硬早退、条件专家路由与退出感知中间监督，在显著压缩 MP-SENet 参数和计算量的同时保持有竞争力的语音增强质量，为资源受限场景提供了一种高效的输入依赖推理范式。

---

## 34. Fast Time-Varying Exponentiated Convolution Methods for Generative Direction Dependent Reverberation

**作者**: Yuancheng Luo
**链接**: [2609.24809](https://arxiv.org/abs/2609.24809)
**分类**: Spatial Audio / Room Impulse Response Generation | **关键词**: Exponentiated Convolution, Time-Varying Filtering, Spherical Harmonics, Spatial Room Impulse Response, Direction-Dependent Reverberation, Gaussian Process, Ambisonics, Fast Convolution

# 论文总结：Fast Time-Varying Exponentiated Convolution Methods for Generative Direction Dependent Reverberation

## 核心痛点
- 空间房间脉冲响应（SRIRs）以及 Ambisonics 等球谐（SH）编码声场能够刻画房间响应的方向性，对空间音频重放、双耳/扬声器阵列虚拟听觉化、波束形成、语音增强、声源定位等任务很有价值。
- 但大规模、多样化的 SRIR 数据集获取困难：多麦克风测量和数值模拟成本高昂，限制了下游模型训练与实验评估。
- 现有方法各自解决部分问题：SH 域镜像源法可低成本生成 shoe-box 房间的 SH-RIR；时变平滑核、低通滤波可引入距离相关的大气衰减频谱衰减；SH 滤波器组可改变声场方向性，但缺少统一、快速、可控制方向依赖频谱衰减的生成/增强框架。
- 直接实现时变指数卷积的计算代价可达 O(M^2N)，对长 FIR 来说不可接受。

## 方法创新
1. **时变指数卷积定义**：给定固定 FIR h（长度 M）与时变 FIR g（长度 N），令 g(m) 为 g 的 m 重自卷积：g(m)=g(m-1)⊛g。输出 f[n]=Σ_m h[n-m+1]g(n-m+1)[m]，可把高斯噪声或 RIR 转化为具有目标频率相关衰减率的混响/修正频谱衰减场。
2. **快速递归指数卷积（Algorithm 2）**：在 Z 域中，指数滤波器的传递函数满足 G^m(z)=G(z)^m；输出传递函数 F_M(z)=Σ_{m=0}^{M-1} h_{m+1}z^{-m}G^{m+1}(z)。利用对 h 的二等分递归关系，将问题分解为下、上两半，上核乘以 G^M(z) 和延迟 z^{-M}。每个递归调用可用 FFT 以 O(MNlog(MN)) 完成卷积；总渐近复杂度约为 O(MN((logM)^2+logMlogN))。实际中 N≪M，因为 g 被设计为近似最小相位且其幅度响应产生期望混响时间轮廓。
3. **递归自回归卷积（Algorithm 3/4）**：给出另一种一阶自回归形式的指数卷积，直接实现仍为 O(M^2N)；提出优化递归版本 Algorithm 4，但其分区尺寸为 m 与 M+m(N-2)，不再成比例，最大分区轨迹总代价约为 O(MN^2((logM)^2+logMlogN))，比指数卷积更昂贵。
4. **球谐域方向扩展**：将 f(h_i,g) 应用于多通道 IR 的每个通道，并证明指数卷积与任意线性变换 A 可交换。因此可直接在 Ambisonics B-format、实/复球谐编码通道上调用 Algorithm 2/4，再解码回方向声场。
5. **方向滤波与 GP 建模**：将瞬时声压场 p_C(r,θ,φ)≈Y(θ,φ)C(r) 与方向衰减函数 D(θ,φ)≈Y(θ,φ)D 在有限阶 SH 基上展开，得到方向加权声压场 p_E=D p_C≈Y E，其中 E 的维数为 (L_D+L_C+1)^2；并用非平稳高斯过程（GP）建模平滑的混响时间分布，实现最优滤波器设计。

## 实验结果
- Fig. 1 展示指数滤波效果：用 N=4 的滤波器 g 分别对 M=72000 的高斯噪声与 M=192000 的 RIR 进行频谱衰减整形，证明可实现目标频率相关衰减率。
- Fig. 2 在 Matlab、Mac M1、20 次平均、48 kHz 采样率下比较指数卷积与递归自回归卷积的运行时间：两种方法相对输入 FIR 长度 M 均呈对数线性增长；但只有指数卷积相对滤波器长度 N 也保持对数线性增长。
- 摘要指出实验评估了计算性能，并验证了分布外生成的脉冲响应；Section 4 还包含混响时间采样、滤波器拟合敏感性和 SH-SRIR 生成实验。
- 代码已开源：https://github.com/yluo1/SH-IRT。

## 一句话评价
论文提出两类快速时变指数卷积及球谐域方向扩展，以较低计算代价实现方向依赖的混响频谱衰减生成与数据增强，并用非平稳 GP 建模混响时间，兼顾生成式 IR 合成与空间音频应用潜力。

---

## 35. MECT: Mixture of Experts with CNN-Transformer Network for Speaker verification

**作者**: Yu Zheng, Jinghan Peng, ChangHao Zhang, Jian Liu, Weiqiang Wang
**链接**: [2609.24061](https://arxiv.org/abs/2609.24061)
**分类**: Speaker Verification | **关键词**: Speaker Verification, Mixture-of-Experts, CNN-Transformer, Streaming Inference, ReDimNet

## 核心痛点
- 说话人确认（Speaker Verification, SV）中，Mixture-of-Experts（MoE）此前主要被用于自监督预训练模型的微调，通过自适应组合不同层表示来提升性能，但在完全监督的 SV 模型中尚未被探索。
- 现有 SV 模型需要在性能、参数量、计算复杂度和流式部署之间取得平衡，尤其面向实际工业场景时，低复杂度与流式推理能力非常关键。
- 如何将 MoE 有效融入 CNN-Transformer 说话人确认骨干，并设计合适的专家粒度与路由策略，是本文解决的核心问题。

## 方法创新
- 提出 MECT：首个基于 MoE 的完全监督说话人确认模型，在 CNN-Transformer 骨干中引入 MoE 机制，并基于 ReDimNet 的 reshape dimension 策略重新设计堆叠方案和网络结构。
- 设计四种 MoE 变体：utterance-level Dense MoE、utterance-level Sparse MoE、frame-level Dense MoE、frame-level Sparse MoE，均替换 Transformer feed-forward block 中的第一个线性投影。
- MoE 计算方式：frame-level Dense 使用 `Gt=Softmax(xtWg)`，输出 `yt=Σ Gi_t·f(xtWi_e)`；frame-level Sparse 先用 Top-K 选择专家再 Softmax；utterance-level 先用均值池化得到 `x̄`，产生所有帧共享的门控权重；utterance-level Sparse 同样使用 Top-K 路由。
- 基础模块改进：CNN 残差 shortcut 放在 BatchNorm 和 ReLU 之后；位置编码采用两层 1D 卷积；时间下采样和通道扩展由 ResNet block 内部卷积完成；block 间使用简单 shortcut 替代 ReDimNet 的 dense connection。
- MECT 架构：Head + Stage1 至 Stage4 多层 MECT block + 多阶段加权融合 + ASTP 池化 + Linear 192 投影 + SphereFace2 损失；通过输入通道数 C 和每 block 的 ResBlock 数 M 控制，得到 A1、A2、B1、B2 四种模型规模。
- 流式推理：比较 M1 embedding averaging、M2 feature concatenation、M3 causal retraining 三种策略；M3 将网络因果化，对卷积层只做左侧 padding，对多头注意力使用 causal mask，并缓存 Conv2d/Conv1d 历史、MHA 的 KV 状态以及 ASTP 的帧特征和 attention logits，实现 100ms chunk 的流式说话人嵌入提取。

## 实验结果
- 评估数据集包括 VoxCeleb1-Cleaned 的 Vox1-O、Vox1-E、Vox1-H、Vox21-val，以及 CN-Celeb Test；训练使用 VoxCeleb2、VoxCeleb2+VoxBlink2 或 CN-Celeb1/2 等设置。
- 训练采用两阶段：完整训练 + large-margin fine-tuning（LMF）；输入为 80 维 mean-normalized log Mel filter-bank，25ms 窗、10ms 帧移、20–7600Hz、16kHz。
- 表 2 的 MoE 消融显示：Frame-level Dense MoE with 4 experts 表现最佳，相较无 MoE 基线在所有测试集上均有提升，平均 EER 和 minDCF 相对提升约 4.7% 和 7.8%。
- 论文报告 MECT-B2 在 VoxCeleb1 上达到 state-of-the-art，Vox1-O、Vox1-E、Vox1-H 的 minDCF 分别为 0.012、0.026、0.048，并在 CN-Celeb 上取得强结果，说明跨数据集有效性。
- 路由策略呈现数据依赖：frame-level dense MoE 在 VoxCeleb 上更优，sparse Top-K MoE 在 CN-Celeb 上更优。
- 流式推理：通过 causal retraining，在 chunk size 为 100ms 时仍保持有竞争力的性能。

## 一句话评价
MECT 是首个将 MoE 引入完全监督说话人确认的 CNN-Transformer 方案，通过多粒度、多路由 MoE 与结构优化在低参数量、低计算复杂度下取得 SOTA，并给出了可落地的 100ms 流式推理范式。

---

## 36. Listen Then Reason: Perception-Grounded Test-Time Reinforcement Learning for Large Audio-Language Models

**作者**: Jiaheng Dong, Xiaofeng Yu, Jean Honorio, Abhirup Ghosh, Hong Jia, Ting Dang
**链接**: [2609.23589](https://arxiv.org/abs/2609.23589)
**分类**: Audio-Language Model Reasoning / Test-Time Reinforcement Learning | **关键词**: Large Audio-Language Models, Test-Time Reinforcement Learning, Perceptual Grounding, GRPO, Audio Reasoning

# Listen Then Reason: Perception-Grounded Test-Time Reinforcement Learning for Large Audio-Language Models

## 核心痛点 (Core Pain Points)
- **LALM 中的感知利用不足（perceptual under-utilization）**：现有大型音频-语言模型沿用 VLM 的架构与训练范式（冻结或轻微微调的音频编码器 + 预训练 LLM 主干），跨模态对齐训练以「回答正确性」而非「感知保真度」为目标，导致模型倾向利用语言先验/文本捷径，声学证据对最终答案的贡献被严重绕过。
- **RL 后训练的奖励信号过于结果导向**：现有基于 RL 的后训练方法（如 SARI、SoundMind-RL）使用最终答案正确性作为奖励，无法区分「真正基于听觉感知得到的正确答案」与「靠语言先验猜对的答案」，可能进一步强化语言侧捷径。
- **TTRL 在无标签场景下更易被 Reward Hacking**：TTRL 通过多次采样的多数投票生成伪标签，但多数一致性可能反映的是轨迹间共享的语言偏见而非声学理解；在缺乏真实标签的纠偏信号时，优化方向会偏离多模态真正的瓶颈（感知），加剧感知欠利用。
- **感知能力在 LALM 推理中的作用机制尚未被系统研究**：声学证据如何随层演化、是否可预测任务性能、是否真正因果地贡献于性能，此前基本是开放问题。

## 方法创新 (Method Innovation)
### 1. 感知贡献的层次化量化分析（Perception Grounding Analysis）
- 提出 **Layer-wise Perceptual Reliance（逐层感知依赖度）**：对每个实例，比较两种条件下的文本隐表示——(1) 原始音频输入；(2) 扰动条件，即将文本 token 对音频 token 的注意力置为 −∞（`M_ij = −∞ for i∈T, j∈A`），阻断跨模态注意力。
- 对问题与选项 token 集合 S 做均值池化得到 `h̄^(l)_c`，用两种条件下池化表示的**余弦距离**作为该层的感知依赖度 `r^(l)_{k,n}`，任务级取平均得 `R^(l)_k`。
- 关键发现：**感知依赖度在浅层递增、在中间层达到峰值、随后向输出层递减**，跨任务、模型规模与数据集一致；作者据此定义 **perception–reasoning emphasis boundary** `l* = argmax_l R^(l)_k`，即从「感知主导」过渡到「推理主导」的层，并以峰值 `R^(l*)_k` 作为任务级声学依赖度量。
- 进一步验证：**更强的声学依赖与更高准确率、以及更大的音频输入带来的性能增益相关**；并通过因果分析（RQ3）考察声学证据是否直接贡献于任务性能。

### 2. PG-TTRL（Perception-Grounded TTRL）
- 是**首个把音频感知基础的可靠性引入无标签策略优化的 TTRL 方法**。
- 在 GRPO（Group Relative Policy Optimization）基础上，为每条采样轨迹计算 **trajectory-level grounding score `g_i`**（轨迹级感知接地分数），据此推导 **acoustic grounding margin（声学接地裕度）**，并用它来**校准优势函数（advantage）**，从而在 test-time 更新中奖励「真正结构化地依赖音频输入进行推理」的轨迹，抑制仅靠语言先验的一致性捷径。
- 整体框架（论文 Figure 1）：先对比原始与扰动条件计算实例级逐层感知依赖 → 得到任务级依赖并考察其与准确率、声学因果贡献的关系 → 在 PG-TTRL 中用轨迹级 grounding score 校准 GRPO 优势。

## 实验结果 (Experimental Results)
- 在两个 LALM 与两个音频推理基准（**MMAR、MMAU**）上验证。
- **PG-TTRL 相比基座模型与标准 TTRL 均持续提升推理准确率**：MMAR 上最高 **+4.6 分**，MMAU 上最高 **+4.9 分**。
- 在**几乎所有采样预算下取得最强的 Pass@k 性能**，尤其在**采样预算受限**时优势更明显。

## 一句话评价
该工作先用「注意力屏蔽 + 逐层表示余弦距离」把 LALM 的声学依赖可视化并证明其与性能正相关，再把这一感知接地信号注入无标签的 GRPO 优势估计中，提出了首个感知接地的音频 TTRL 方法 PG-TTRL，在 MMAR/MMAU 上稳定超越基座与标准 TTRL，揭示了「先听、再推理」的多模态测试时优化新范式。

## 作者与机构
Jiaheng Dong、Xiaofeng Yu（共同一作）、Jean Honorio、Abhirup Ghosh、Hong Jia、Ting Dang；The University of Melbourne、University of Auckland、University of Birmingham、ARC OPTIMA。

---

## 37. ArtifactBench: Lineage-Aware Evaluation of AI-Generated Music Detectors under Distribution Shift

**作者**: Heewon Oh
**链接**: [2609.23550](https://arxiv.org/abs/2609.23550)
**分类**: AI-Generated Music Detection | **关键词**: AI-generated music detection, lineage-aware evaluation, benchmark, distribution shift, data leakage, detector robustness, audio forensics

### 论文定位
本文提出 ArtifactBench v2，一个面向 AI 生成音乐检测器的“谱系感知”（lineage-aware）评测协议与基准，作者为 Heewon Oh（Intrect，ORCID 0009-0000-2287-1753）。论文不是提出新检测模型，而是把 AI 音乐检测视为评测治理问题，强调在分布偏移下让每次比较的总体、来源、工作点和失败分母可审计。

### 核心痛点
- 现有检测器常用聚合分数比较，但基准的训练重叠、生成器谱系、来源出处、音频变换历史往往只能部分观测。
- 一个基准名称可能对应多个 manifest，被引用的音频只有一部分仍可用，模型公开训练划分可能与其名义测试集重叠。
- 若每个 adapter 静默跳过不同文件，最终聚合分数并非比较同一总体。
- 高域内准确率可能无法代表对未见生成器或音频变换的鲁棒性；生成器版本、真实音乐域、采集队列偏移会掩盖在总指标中。
- 泄漏状态不是二元“unseen”：需区分精确内容重叠、属于已发布上游 train/val 划分、以及公开训练流程未提供身份映射的 unresolved exposure。

### 方法创新
1. **Lineage-aware 协议**：每条公开 track id 绑定 content digest、source family、generator family/version（若已知）和 lineage id；split 单位是 lineage 而不是文件，防止同一录音的不同编码/容器/变体跨协议划分造成泄漏。
2. **内容身份与谱系分组**：使用密码学内容身份与 lineage group；移除与 ArtifactNet 训练音频精确字节匹配项，以及通过声学指纹发现的两个真实音频变体。
3. **冻结划分**：主队列 828 轨（605 合成 + 223 真实），覆盖 13 个合成 source strata 和两个真实音乐域；按 source strata 内确定性 salt 和 20/10/70 比例划分为 166 calibration（121 AI/45 real）、83 validation（61 AI/22 real）、579 sealed test（423 AI/156 real）。
4. **版本固定 runner**：评估 ArtifactNet v9.4、SpecTTTra-α-120s、公开 Deezer ISMIR 2025 logistic detector、CLAM；固定仓库/模型/特征编码器 revision，ONNX 使用外置数据文件并记录 run manifest；CLAM 记录 checkpoint SHA-256 及 MERT/Wav2Vec2 revision。
5. **统一预处理与可靠性规则**：所有 adapter 接收同一解码单声道波形与选定 track IDs；固定时长基线用 center crop；SpecTTTra 用 120s 输入，CLAM 用确定性 90s crop；ArtifactNet 评估 7 个均匀间隔 4s chunk，当至少 4/7 chunk 有效时取有限 chunk 分数中位数；严格敏感性结果显示任一非有限 chunk 即 track failure，并发布 chunk 级失败日志。
6. **阈值治理**：主操作阈值仅在 calibration 行上选择：在 FPR ≤ 5% 的观测阈值中最大化 TPR，平局取更低阈值，然后冻结用于 validation/test；同时报告原生 0.5 阈值、AUROC、AUPRC，避免把有利校准选择当作表示质量。
7. **失败与缺失分计**：resolution、decode、model inference、non-finite output、out-of-range probability 是不同事件，不转为类别预测，也不从尝试分母中静默丢弃；主表同时显示成功评分 track 与失败；配对比较使用 common successfully scored test-ID intersection，coverage 本身作为模型结果。
8. **统计不确定性**：95% 区间用 2,000 次 label-stratified lineage bootstrap；重采样 lineage 而非文件，避免同一录音的多个编码被视为独立证据。
9. **泄漏与队列审计**：公开 v1.0.1 manifest 有 6,200 行与 2,280 行 test；v1.1 分支有 2,224 行 purged test；本地 post-purge manifest 元数据称 6,183 行但实际 6,014 行；早期八模型比较只 scored 2,104 tracks，因为 120 个引用的 FMA 文件是 HTML 响应而非音频。论文从官方 FMA 归档恢复并验证全部 150 个选定 FMA track。对 SONICS lineage：241 行映射到 train/validation，454 行仅 test，1,541 行 external；对 MoM lineage：200 行到 training，197 行到 test，1,523 行 external，316 个真实行 unresolved（CLAM 训练代码在本地 embedding 可用性过滤后做 seeded random split，未发布实际身份映射）。保守的 828 轨主队列排除所有原生 SONICS/MoM 派生 source families，但作者仍避免称其“universally training-unseen”。

### 实验结果
- 在 562 轨 common-success test intersection 上，ArtifactNet 达到 **0.982 AUROC、0.918 balanced accuracy**；公开 Deezer 检测器为 **0.761/0.776**；SpecTTTra 与 CLAM 在该 shifted cohort 下均低于 **0.30 AUROC**。
- 表 2 配对测试结果（阈值仅由 calibration 选择）：ArtifactNet v9.4 scored 562/579，τ=0.9909，AUROC 0.982，AUPRC 0.994，F1 0.923，BAcc 0.918，TPR 0.865，FPR 0.029，coverage 0.971；SpecTTTra-α scored 579/579，τ=0.9695，AUROC 0.299，AUPRC 0.688，F1 0.159，BAcc 0.526，TPR 0.087，FPR 0.036，coverage 1.000；Deezer ISMIR scored 579/579，τ=0.3165，AUROC 0.761，AUPRC 0.925，F1 0.758，BAcc 0.776，TPR 0.624，FPR 0.072，coverage 1.000；CLAM scored 579/579，τ=1.0000，AUROC 0.284，AUPRC 0.647，F1 0.000，BAcc 0.500，TPR 0.000，FPR 0.000，coverage 1.000。
- 表 3 的 95% lineage-bootstrap 区间：ArtifactNet AUROC 0.971–0.991、AUPRC 0.989–0.997、TPR 0.832–0.898、FPR 0.007–0.058；SpecTTTra-α AUROC 0.245–0.352、AUPRC 0.662–0.714、TPR 0.061–0.116、FPR 0.007–0.072；Deezer ISMIR AUROC 0.723–0.798、AUPRC 0.912–0.938、TPR 0.579–0.671、FPR 0.029–0.115；CLAM AUROC 0.236–0.333、AUPRC 0.623–0.675、TPR 0.000–0.000、FPR 0.000–0.000。
- 结果暴露了聚合分数单独会掩盖的显著 generator 与 real-domain shift，并说明泄漏控制、队列可用性、阈值政策、模型特定缺失性会改变测量性能与模型排名。

### 一句话评价
ArtifactBench v2 把 AI 生成音乐检测从“刷聚合指标”推进为可审计的评测治理框架：它不追求最大训练语料，而是让比较总体、来源谱系、工作点、失败分母和泄漏状态透明，揭示在分布偏移下模型排名可能被协议差异掩盖。

---

## 38. Misrecognition or Abstraction? Rethinking Outputs of Sound Event Recognition

**作者**: Naoya Tomida, Yuki Okamoto, Keisuke Imoto
**链接**: [2609.23411](https://arxiv.org/abs/2609.23411)
**分类**: Sound Event Recognition | **关键词**: Sound Event Recognition, Onomatopoeia, Confidence Score, Language-Audio Model, CLAP, Uncertainty

# 论文总结：Misrecognition or Abstraction? Rethinking Outputs of Sound Event Recognition

## 核心痛点
传统通用声音识别系统通常输出确定性的声音事件标签，隐含假设输入音频中的目标声音类别可以被正确识别。然而在真实聆听场景中，声音事件类别并不总是清晰可辨；人类即使无法确定精确类别，仍可通过拟声词等模糊描述理解周围环境。现有 SER 系统在预测不可靠时仍强行输出离散类别标签，容易造成误导，也较少讨论低置信度或误识别情况下输出应如何重新设计。论文主张：声音识别系统应假设事件类别不一定总能被正确识别，并据此重新设计输出表示。

## 方法创新
论文提出一种新的声音事件识别输出表示：声音事件类别 + 置信度分数 + 声音的拟声词描述。该表示既保留传统基于类别的识别能力，又在类别预测不确定时提供关于声学特征的拟声描述，使低置信度输出仍具信息量。

实现上，采用 CLAP（Contrastive Language-Audio Pretraining）构建音频-文本联合嵌入空间，并联合进行声音事件识别与拟声词检索。由于预训练 CLAP 对拟声文本对齐不足，方法在 CLAP 文本编码器后加入一个 MLP projector，冻结音频和文本编码器，仅训练 projector 来对齐拟声文本与对应音频嵌入，目标为均方误差 Lono。同时训练一个 MLP 分类器从音频嵌入预测声音事件类别，分类损失为交叉熵 Lcls；总损失为 L = Lono + λLcls。推理时，分类器输出预测类别与 margin-based 置信度（top-2 softmax 概率的归一化差），拟声词则从候选集中检索与音频嵌入欧氏距离最小者。最后根据置信度阈值切换输出模板：高置信度时输出类似“That is a dog barking sound, and the sound is like bow wow.”；中等置信度时输出“That sound is like bow wow, and that might be a dog barking sound.”；低置信度时只输出“I heard a bow wow like sound.”。这样可在不可靠时避免断言错误类别，同时保留有用的声学描述。

## 实验与结果
实验使用 ESC-50 和 ESC-50-Onomatopoeia 数据集。MLP 与分类器均为 3 层 dense，单元数为 512、256、128；λ=1.0；优化器 AdamW。结果表明，所提方法在声音识别性能上与传统仅识别系统相当，说明加入拟声词输出没有显著牺牲 SER 精度。此外，LLM-as-a-judge 评估与主观听力实验显示，在支持周围环境理解的任务中，所提输出比基于声音事件标签的传统确定性输出更受偏好，尤其在预测不确定时。这些结果说明，结合类别、置信度与拟声描述的输出表示能让 SER 在不确定性下更具信息性和交流性。

## 一句话评价
论文挑战了 SER 必须输出确定性类别标签的隐含假设，提出用“类别 + 置信度 + 拟声词”表达不确定性，并通过 CLAP 联合识别与拟声检索实现；实验表明该方法在保持识别性能的同时提升了环境理解支持能力，为不确定条件下的声音识别输出设计提供了新视角。

## 其他关键信息
- 任务背景涉及声音事件识别、音频标注、声事件定位与检测、自动音频描述、音频问答等。
- 传统输出流程：输入音频转为时频表示，SER 模型输出 logits，经 softmax/sigmoid 后通过 argmax 或阈值 φ 得到离散类别。
- 拟声词已被用于音频检索、音频到拟声词转换和声音生成，但较少用于 SER 低置信度输出设计。
- 实现较简单，当前仅做声音事件分类；分类器可替换为 SED、SELD、音频描述等下游预测器。
- 输出模板基于置信度阈值切换；片段中未给出完整实验数值表格。

---

## 39. ParA-LLM: A Unified Approach to Paralinguistic and Acoustic Speech Understanding

**作者**: Nishit Anand, Jiaqi Su, Ke Chen, Yunyun Wang, Dinesh Manocha, Ramani Duraiswami, Rithesh Kumar, Zeyu Jin
**链接**: [2609.22771](https://arxiv.org/abs/2609.22771)
**分类**: Speech Understanding / Audio LLM (Paralinguistic & Acoustic Understanding) | **关键词**: paralinguistics, acoustics, speech understanding, large audio language models, curriculum learning, Audio-QA dataset, benchmark

## 核心痛点

当前 Audio LLM（如 GPT-4o-Audio、Qwen2-Audio 等）在**语义/文字内容**理解上已接近人类水平（ASR 人类 97% vs 模型 94%），但严重缺乏对**副语言（paralinguistic）信息**的理解能力，即「**怎么说**」而非「**说了什么**」——包括说话人特质（音色、口音、鼻音）、表达变化（情感、语速、音高）以及环境声学条件（混响、噪声、回声）。作者的小规模对照实验显示：在 100 道副语言问题上，人类准确率 78%，而 SOTA 的 GPT-4o-Audio 仅 36%。现有专用模型（如情感识别、口音分类）只能处理单一属性，无法跨属性联合推理。

## 方法创新

1. **22 项副语言特征分类体系**：系统性地划分为 3 类——10 项声学特征（Reverb Type、Noise Type、Reverb DRR/RT60/ERR/DER Level、Overall Reverb Level、Background Noise Level、Post Processing、Overall Quality(STOI)）、7 项说话人固有特征（Gender、Accent、Nasality、Timbre、Loudness、Smoothness、Articulation）、5 项话语级语音特征（Emotion、Speaking Rate、Pitch、Expressivity、Flow）。特征设计尽量客观（声学用 DRR/RT60/SNR/STOI 等信号指标，发音/语音用自然语言描述符 + 多数标注者一致）。
2. **数据引擎 + 大规模数据构建**：基于 EARS、Emilia、Expresso、VoxCeleb、ParaSpeechCaps 的干净语音，通过 RIR 卷积（MIT IR Survey、EchoThief）与背景噪声混音（TAU Urban Audio-Visual Scenes 2021、Isolated Urban Sound Background、合成有色噪声）进行声学仿真，并加入 clipping、动态压缩、overdrive 等后期效果，最终产出 **超过 1.2M Audio-QA 对**、70 万+ 唯一音频样本。
3. **两阶段课程学习（Two-Stage Curriculum）**：
   - **Stage 1**：688K 原子单属性 QA（306K 音频），用模板生成，每问只针对一个副语言/声学属性，建立基础属性知识；
   - **Stage 2**：513K 多属性 QA（217K 音频），用模板 + LLM-based ICL 生成，训练跨声学/说话人/语音属性的联合推理。
4. **ParA-LLM**：统一副语言与声学理解的音频 LLM，支持对多个相互作用的属性进行**自由形式联合问答**（区别于 Vox-Profile 等只能做单属性分类的方案）。
5. **ParA-Bench**：6,000 道多选题基准，覆盖 speaker-speech、acoustic、mixed 三类；测试集的音频、RIR、噪声与训练数据严格不重叠。

## 实验结果

**ParA-Bench 总体准确率**：

| 模型 | Speaker-Speech | Acoustic | Mixed | Overall |
|---|---|---|---|---|
| Qwen2-Audio | 34.80 | 23.45 | 25.90 | 28.05 |
| Voxtral | 51.95 | 29.20 | 35.25 | 38.80 |
| Audio Flamingo 3 | 34.35 | 38.75 | 33.40 | 35.50 |
| Mellow | 3.60 | 3.60 | 3.80 | 3.67 |
| R1-AQA | 26.60 | 19.00 | 21.20 | 22.27 |
| Qwen2.5 Omni 3B | 20.85 | 9.45 | 10.35 | 13.55 |
| Qwen2.5 Omni 7B | 21.30 | 11.75 | 10.35 | 14.47 |
| GPT-4o-Audio | 32.00 | **41.85** | 34.25 | 36.03 |
| **ParA-LLM (Ours)** | **55.85** | 34.80 | **39.95** | **43.53** |

- 在 ParA-Bench 上超过 GPT-4o-Audio **7.5%**（43.53 vs 36.03）；
- 相比基座模型，在 **MMAU-Pro Speech** 上提升 **1.13%**，在 **MMAR Speech** 上提升 **7.49%**，说明该课程学习不仅提升副语言理解，也惠及更广泛音频理解；
- 前沿模型在 ParA-Bench 上仅约 **36%** 准确率，凸显该任务仍为开放难题。

**核心贡献**：(1) 1.2M+ 结构化 Audio-QA 数据集与两阶段课程训练范式；(2) ParA-LLM 统一副语言与声学理解模型；(3) ParA-Bench 基准。

## 一句话评价

本文通过 22 项特征体系、百万级 Audio-QA 数据与「原子→联合」两阶段课程学习，首次让 Audio LLM 具备对声学、说话人及语音动态属性的自由形式联合推理能力，在自建 ParA-Bench 上大幅超越 GPT-4o-Audio，填补了「怎么说」这一副语言理解的关键空白。

---

## 40. COT-TTS: Audio Context-Aware Text-to-Speech with Chain-of-Thought Reasoning

**作者**: Weizhen Bian, Sitong Cheng, Rongxiu Zhong, Jiahao Pan, Liumeng Xue, Boyi Kang, Shilei Zhang, Jinglei Liu, Yue Wang, Junlan Feng, Bei Liu, Wei Xue
**链接**: [2609.22697](https://arxiv.org/abs/2609.22697)
**分类**: Text-to-Speech | **关键词**: Context-aware TTS, Chain-of-Thought Reasoning, Expressive Speech Synthesis, Dialogue Speech Dataset, Autoregressive Modeling

## 核心痛点
- 现有TTS系统在语音表现力和可控性上进展显著，但生成语音的说话风格通常依赖用户显式指定指令，难以从对话历史中自然推断。
- 在对话、影视配音、有声书、虚拟角色等场景中，目标句子的说话方式应依据前文对话上下文自动推断，而非逐句人工提供风格提示。
- 缺乏匹配该任务的大规模数据：现有对话语音数据集场景较简单、说话人多样性和上下文变化有限；部分数据集虽提供上下文标签或角色信息，但很少解释上下文如何导致特定说话方式；音频推理数据集多关注回答什么，而非应如何说。
- 现有系统通过显式指令、参考语音或可编辑声学属性控制风格，但说话方式仍由用户指定；级联ASR+LLM+TTS系统可能丢失非语言发声、节奏、情感强度等副语言信息，并依赖下游TTS准确实现推理出的风格。

## 方法创新
- 提出COT-TTS任务：给定历史多说话人对话音频Ha、目标文本y和参考语音ra，模型需输出带情感标签的历史转写T、显式推理分析C以及目标语音xa，即( T, C, xa ) = fθ(Ha, y, ra)。
- 推理分析C包含五个维度：语言行为、场景语义、认知与动机、预期交际结果、情感轨迹；同时预测时长和情感表达强度等显式说话属性，并给出结构化最终总结。
- 数据构建：从约100K小时中英文对话音频出发，设计可复现pipeline，包括数据收集与预处理、多维标注、结构化样本构建；得到9M双语训练样本，其中含1M高质量子集。
- 基准构建：从约3M测试候选中构建源分离双语基准，经自动过滤和人工验证后包含800个样本，并建立结合客观指标、LLM评估和人工听测的评测协议。
- 模型构建：开发0.6B和1.7B参数的端到端自回归模型，生成情感标签转写、可编辑语音风格推理和语音token；相比由多个大模型组成的级联系统，参数显著更少。
- 资源开放：将公开数据构建pipeline、数据集、训练模型及相关代码，支持可复现研究。

## 实验结果
- 所提模型以显著更少参数达到与大规模基线系统相当的整体性能。
- 模型在时长一致性和情感一致性上表现良好，能根据对话上下文生成合适的情感、重音和节奏变化。
- 任务基于自然发生的上下文表达，而非人工设计风格提示；目标文本已给定，模型不决定说什么，而是决定如何说，并利用参考语音主要控制目标说话人音色。
- 摘要提到demo页面和附加资源，但前部分未给出具体客观指标数值。

## 一句话评价
COT-TTS将链式推理引入音频上下文感知TTS，以明确任务定义、大规模双语对话数据和轻量自回归模型推动TTS从读文本向根据对话历史决定怎么说转变，具有较强的学术价值和应用潜力。

---

## 41. Hi-Singers: A Comprehensive High-Quality Dataset for Expressive Audio-Driven Singing Head Synthesis

**作者**: Yichi Zhang, Hui Zhang, Guanjun Liu, Yuefeng Zou, Fengzhao Sun, Jun Yu
**链接**: [2609.22264](https://arxiv.org/abs/2609.22264)
**分类**: Audio-Driven Singing Head Synthesis | **关键词**: Singing Head Synthesis, Audio-Driven Digital Human, Video Dataset, Rhythmic Synchronization, Beat Alignment Score

## 核心痛点
- 说话头（Talking Head）合成已取得照片级真实感，但将其扩展到歌唱头（Singing Head）合成仍面临显著 **Domain Gap**。
- 歌唱相比说话需要更夸张的面部表情、更大幅度的下巴开合，以及精确的节奏同步；现有主要基于语音数据训练的模型容易出现 **“节奏漂移”（rhythmic drift）** 和动态受限问题。
- 现有歌唱相关数据集存在明显不足：规模小、偏重 3D mesh/动画或身体动作、或局限于受控实验室环境，缺少大规模、高质量、in-the-wild 的 2D 歌唱头视频数据。

## 方法创新
- 提出 **Hi-Singers**：首个面向 2D 歌唱头合成的大规模、高质量、in-the-wild 视频数据集。
- 数据规模：**29,608 个视频片段，约 170 小时**；覆盖英语和中文，音乐风格涵盖 Pop、Rock、Classical、Hip-hop 等。
- 数据构建流程：从 YouTube、TikTok（抖音）、Bilibili 等平台采集约 **1,200 GB / 4,500 小时**原始视频；预处理为 1080p 以上、25 fps、16kHz、H.264，并切片；随后经过自动化过滤与人工过滤。
- 构建原则：以歌唱为中心；足够的面部分辨率；完整面部特征显示；面部显示稳定且连续。
- 自动化过滤：结合 **TBF（阈值过滤）** 与 **SBF（评分过滤）**；使用 face-alignment 检测/对齐人脸，过滤面部高度不足、遮挡、侧脸、模糊等；裁剪为 512×512 单脸；用 **SyncNet** 过滤唇音不同步；用滑动窗口分析面部中心位移与 Euler 角度（yaw/pitch/roll），过滤大幅运动和非正脸片段。
- 人工过滤进一步确保主题、质量与稳定运动等要求。
- 构建专用评测基准：在语言（英语/中文）与音乐风格上保持平衡。
- 提出节奏评价指标 **BAS（Beat Alignment Score）**：量化音频节拍与运动学运动峰值之间的节奏同步，用于识别通用模型中的节奏漂移。
- 在多种 SOTA 架构（3D 系数类 SadTalker 与 Latent Diffusion 类 V-Express）上验证数据集有效性。

## 实验结果
- 在多种架构上训练后，Hi-Singers 在所有维度上持续且显著提升性能。
- 具体表现为：更优的视觉真实感、更强的唇同步一致性、更精确的节奏动态。
- 有效弥合语音与歌唱之间的 domain gap，为歌唱合成任务设立新的性能标准。
- 数据集已公开：https://huggingface.co/datasets/CharlesZhang-USTC/Hi-Singers

## 一句话评价
Hi-Singers 通过构建首个大规模、高质量、in-the-wild 的 2D 歌唱头数据集，并配套平衡基准与节奏评价指标 BAS，系统性地缓解了歌唱头合成中的数据稀缺与节奏漂移问题，是该方向的重要数据基础设施。

---

## 42. Causal Localization of the Refusal Direction in Audio Language Models

**作者**: Leonardo Haw-Yang Foo, Hung-yi Lee
**链接**: [2609.22260](https://arxiv.org/abs/2609.22260)
**分类**: Audio Language Models (LALM) Safety & Mechanistic Interpretability | **关键词**: Audio Language Models, Refusal Direction, Mechanistic Interpretability, Causal Localization, AI Safety, Activation Ablation

### 核心痛点
大型音频语言模型（LALM）通常将语音前端接到已安全对齐的文本语言模型（LM）上。当模型拒绝有害语音请求时，拒绝行为究竟由音频前端携带，还是继承自文本 LM？现有安全审计多依赖探针（probe）的可解码性，但可解码不等于因果使用，且缺少固定的留出、逐站点因果测试来区分“可解码位置”与“移除后改变拒绝边际的位置”。

### 方法创新
- **因果定位框架**：在音频到 LM 接口与 LM 残差层分别拟合区分有害/良性提示的 rank-1 方向 r(l)，然后通过消融（ablation）移除该方向，观察首 token 拒绝边际 G(x) 的变化。
- **三类干预**：noop、ablate（x⊥ = x - (x^T r)r，并重缩放保持范数）、steer（x + kr）；另有 scalar rescue 恢复测试。
- **独立逐层消融**：每次只 hook 一层，估计该层方向对留出边际的依赖，而非 Arditi 等人选择单一层并在所有层消融。
- **数据集与留出协议**：588 对匹配的有害/良性音频对，覆盖 14 个危害类别；有害提示来自 AdvBench、HarmBench、JailbreakBench，经固定 TTS 渲染；良性为同域模板硬负例。采用 group-blocked（留出 4 个未见类别，N=238）与 leave-one-group-out（N=584）防止方向拟合循环。
- **读出指标**：首输出 token 上拒绝开场白集合与合规开场白集合的 log-sum-exp 边际 G(x)，越高越倾向拒绝；行为结果另用 HarmBench 分类器评估 512 token 生成。

### 实验结果
- 在 Qwen2.5-Omni 上，L16 方向消融使留出拒绝边际变化 ΔG=-7.10，而 projector 处仅 -0.013；rank-16 projector 子空间也仅 -0.14，接近随机方向零假设（|ΔG|≤0.02）。
- 效应集中在 LM 中后层带：L14=-2.51、L16=-7.10、L17=-9.19、L20=-5.43，L08 仅 -0.10；在 28 层模型的 L26 仍有约峰值一半。LOGO 复现类似对比。
- 音频通路仍在起作用：将 encoder 输出置零会使 G 变化 -4.7；但测试的接口方向消融影响很小。
- 跨模型：五个 LALM、三个骨干家族中，最大测试效应均出现在 LM 站点，呈现模型相关的中后层剖面，如 Voxtral 的宽平台、DeSTA 的 L20 峰值。
- 可解码性与因果性解耦：对比在早期层线性可解码，但单层消融影响小；仅在 LM 骨干上拟合的方向可迁移到完整音频模型。
- 形式混淆：用 XSTest 自然良性提示重新拟合后，L16 效应降至 -1.79，低于因果带阈值 |ΔG|≥3.55，说明 -7.10 部分来自匹配设计中的提示形式差异；作者因此将 r 解释为“与拒绝相关”而非“纯危害性”方向。
- 行为层面：改变 logit 边际并不总是改变模型实际写出的内容，因此安全审计不应仅依赖探针，应使用因果干预，并同时检查继承的文本 LM 与音频接口。

### 一句话评价
该工作用因果消融把 LALM 的拒绝行为定位到继承文本 LM 的中后层方向，而非音频接口，并强调安全审计应从可解码性转向干预性证据。

---

## 43. Beyond the Raw Waveform: Fusing Visual Representations of EDA for Stress Detection

**作者**: Stefanos Gkikas, Thomas Kassiotis, Yang Guo, Guangliang Li, Eric Nichols, Houshyar Asadi, Nikolaos Smyrnis, Giorgos Giannakakis
**链接**: [2609.22095](https://arxiv.org/abs/2609.22095)
**分类**: Affective Computing / Physiological Signal-based Stress Detection (EDA Signal-to-Image Representation) | **关键词**: Stress Detection, Electrodermal Activity (EDA), Signal-to-Image Representation, Multi-Representation Fusion, Transformer / Asymmetric Attention

## 论文信息

**标题**：Beyond the Raw Waveform: Fusing Visual Representations of EDA for Stress Detection

**机构**：Honda Research Institute Japan、Hellenic Mediterranean University、Ocean University of China、Deakin University、National and Kapodistrian University of Athens 等

## 核心痛点

1. **EDA 的表征方式过于单一**：电活动（Electrodermal Activity, EDA）是自动压力检测中最成熟的外周生理信号之一，反映交感神经对汗腺的调控。然而现有绝大多数流水线只把 EDA 当作**一维原始波形**（raw waveform）或仅做最小滤波处理，时频表征与非线性动力学表征（如 STFT 相位谱、递归图、小波尺度图等）仍鲜有系统探索，这些表征可能揭示波形本身难以学到的结构。
2. **可穿戴场景下的信号质量与泛化瓶颈**：临床/职业/作业环境中自评量表易受回忆偏差与社会期望影响，唾液皮质醇采样侵入性强且动力学延迟大；可穿戴设备虽可连续采集，但依从性、运动伪影与部署差异导致数据质量成为泛化关键障碍。因此需要在接近动态（ambulatory）使用的条件下，从设备已采集的信号中榨取尽可能多的信息。
3. **现有信号转图像（signal-to-image）研究存在空白**：已有工作或在多模态窗口上比较 GAF/MTF/递归图（如 WESAD 上），或把多种 EDA 表征**空间拼接**为单张多表征图（用于疼痛识别），或学习跨模态共享图像嵌入空间；但**在同一被试级压力识别协议下，对原始 EDA 波形、多种 EDA 派生视觉表征及其通道堆叠融合进行系统性对比的工作仍然缺失**。
4. **融合策略的架构开销问题**：常见的多表征融合依赖独立编码器分支或晚期融合（late fusion），结构复杂、计算成本高，需要验证是否能用更简洁的共享架构完成有效融合。

## 方法创新

### 1. 六种 EDA 图像化表征（+ 原始波形共七种）

每条 EDA 记录为单通道 1 kHz 采样、时长 120 s、共 119,988 个样本。除原始波形作为 1D 输入并在所有组合中占据一个通道外，其余六种 2D 图像表征在将信号降采样至 f_ds = 50 Hz（匹配 EDA 约 0.05–5 Hz 带宽）后计算：

| 表征 | 定义 |
|---|---|
| **PSD** | STFT 幅度谱图，128 样本窗、120 样本重叠，限带 0.05–5 Hz 并做对数压缩 |
| **Angle** | 同一 STFT 的**展开相位（unwrapped phase）**，沿时间轴做相位展开，消除缓慢变化 EDA 信号上原本会出现的棋盘状伪影 |
| **Phase** | 由展开相位时间导数得到的**瞬时频率图**，将幅度低于第 50 百分位的时频单元置零，并用高斯滤波（σ=1.5）平滑以抑制低功率区噪声 |
| **Scalogram** | 使用 Morlet 小波的连续小波变换，128 个对数间隔尺度覆盖 0.05–5 Hz，得到多分辨率时频能量图 |
| **Recurrence** | 对 z-score 归一化信号、以第 20 百分位为点阈值计算的**递归图**，可视化信号动力学中的重复状态 |
| **Wave** | 将全分辨率波形直接渲染为折线图，把 1D 轨迹转为 2D 图像，不做任何时频或非线性变换 |

所有六种图像均以 **224×224** 分辨率、统一 colormap 与画布捕获管线渲染，保存为无损图像并去除坐标轴，以减轻图像风格差异、使比较聚焦于底层信号变换；其中 PSD、Phase、Scalogram 额外做 5th–95th 百分位对比度归一化，Angle 不做百分位裁剪。

### 2. 多表征通道堆叠融合 + 共享非对称注意力架构

- **融合方式**：不采用空间拼接、也不使用独立编码器分支或晚期融合，而是把每张选定的图像表征从其原生 224×224×3 形状**展平为一维向量（长度 150,528）**，再与原始波形一起**堆叠为单个多通道输入**（通道堆叠，channel stacking）。
- **模型**：使用**共享的非对称注意力（asymmetric-attention）架构**统一处理，包含 8 头交叉注意力（Cross-Attention ×8 head）、8 头自注意力（Self-Attention ×8 head）与前馈网络（FFN），随后进行融合与分类；即在同一 Transformer 中完成表征间交互，避免多分支设计。
- **研究问题**：评估「超越原始波形」到底能带来多少收益，以及多种互补表征作为单通道输入的通道时，能否提升压力识别性能。

## 实验结果

- **数据集**：58 名被试的压力数据集；采用被试级（subject-level）压力识别协议。
- **融合优于原始波形**：
  - 最佳配置：**融合五种表征但排除展开相位谱图（Angle）**，测试准确率 **70.97%**；
  - 仅用原始波形（raw waveform）基线：**67.36%**。
- **单表征表现**：**单独的 PSD 谱图达到 69.44%**，非常接近最佳融合配置，同时计算成本更低——说明在资源受限场景下单一 PSD 谱图是极具性价比的选择。
- **结论性观察**：
  1. 同一 EDA 信号的**替代视觉形式能够提供有用的归纳偏置（inductive biases）**，有助于压力检测；
  2. **紧凑的互补表征子集**比单独使用原始波形更有效；
  3. 并非表征越多越好——排除 Angle 后反而取得最佳结果，说明表征选择需要精简与互补性考量。

## 一句话评价

该工作以「同一 EDA 信号的多视角图像化 + 通道堆叠式共享注意力融合」这一轻量方案，系统性地证明了**超越原始波形的表征设计本身就是一种有效且廉价的归纳偏置**，在 58 被试试集上把压力识别准确率从 67.36% 提升到 70.97%，其中单张 PSD 谱图以 69.44% 逼近最优融合，为可穿戴压力监测提供了一条实用且可解释性较强的表征工程路线；其局限在于增益幅度相对温和（约 3.6 个百分点）、仅在单一数据集与单一被试协议上验证，且最优组合需通过排除式搜索确定。

---


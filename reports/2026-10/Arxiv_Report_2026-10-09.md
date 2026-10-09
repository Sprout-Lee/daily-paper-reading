# Arxiv Daily Deep Report - 2026-10-09

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 17
---

## 1. SteerablePlex: Can We Steer Full-Duplex Models?

**作者**: Haolong Zheng, Maike Züfle, Dominik Macháček, Peter Polák, Xulin Fan, Xavier Sumba, Siyin Wang, Ondřej Klejch, Mark Hasegawa-Johnson
**链接**: [2610.12201](https://arxiv.org/abs/2610.12201)
**分类**: Full-Duplex Spoken Dialogue | **关键词**: Full-Duplex Speech, Spoken Dialogue, Instruction Following, Reinforcement Learning, Turn-Taking, User Simulator

# SteerablePlex: Can We Steer Full-Duplex Models?

## 核心痛点
- 全双工语音模型可以同时听与说，支持自然交互，但随着对话历史增长，模型越来越难以控制。
- 当用作用户模拟器时，缺乏控制会导致模型偏离预设场景，产生不可靠的评测结果；模拟器错误会与目标智能体能力混淆。
- 现有系统主要依赖 system prompt，但对话推进后指令遵循会漂移；严格延迟预算也限制了模型规模和长程规划能力。
- 当前开源全双工模型难以遵循多阶段约束；GPT-Realtime 虽能遵循大多数单条指令，但在按顺序完成完整指令序列上仍不可靠。

## 方法创新
- **SimIF-Bench**：Simulator Instruction-Following Benchmark，复用 Full-Duplex-Bench v2 的 200 个分阶段场景，固定 PersonaPlex 为被考者，通话 120 秒，LLM judge 评估话题遵循、自然度、目标完成和严格四目标顺序。
- **SteerablePlex**：一种可在对话进行中接收指令的全双工模型，作者称之为 online instruction following。
- **特殊 token 注入接口**：将指令 token 拼接进 model-text 流中的 <SOI> 与 <EOI> 之间；插入步骤中音频流使用 silence token，对话时间不推进，利用预训练模型对文本流的语义理解来学习指令控制。
- **GDPO 训练配方**：Group Reward-Decoupled Normalization Policy Optimization，对多个奖励维度独立做组内归一化后再组合，联合优化指令遵循、响应自然度和轮次转换。
- **奖励设计**：目标完成度（none/partial/full）、对话自然度（0/1）、轮次转换 VAD 奖励（overlap、take、latency、backchannel），并使用 KL 约束限制相对 adapter-off PersonaPlex 策略的漂移。
- **数据准备**：基于 Fisher 数据集，用 Qwen3-32B 生成 turn-level 指令，得到 9,417 个 RL 样本、130.8 小时 rollout；再按 Behavior-SD 流程合成 2,000 段重叠语音对话，共 84.1 小时立体声音频，其中 200 段留出。
- **Actor-Director 架构**：actor 为全双工模型，负责语音生成、聆听和轮次转换；异步文本 LLM director 利用流式 ASR 和模型文本流跟踪任务与目标，每 2 秒更新目标状态并产生候选指令与动作（send/wait/none）。

## 实验结果
- **SimIF-Bench 200 任务**：SteerablePlex 与 in-domain 变体使用相同 actor-director harness。In-domain 变体在话题遵循 4.80、完成率 91.4%、严格顺序 47.5% 上超过 GPT-Realtime（4.72、80.6%、32.5%）和开源基线；相比 PersonaPlex（话题 2.19、完成率 10.6%、严格顺序 0.0%）提升显著。自然度略低于 PersonaPlex（SteerablePlex 3.49/in-domain 3.81 vs PersonaPlex 4.45），说明遵循指令时存在自然度权衡。
- **Full-Duplex-Bench**：SteerablePlex 改善 pause handling（Syn 0.394/0.365 vs PersonaPlex 0.642；Cand. 0.500/0.417 vs 0.718），保持 smooth turn TOR 1.000 和 interruption rating 1.000，同时 backchannel 频率和 JSD 处于合理范围，表明在提升可控性时未明显牺牲轮次转换能力。
- **训练细节**：从 PersonaPlex 初始化，训练 LoRA 适配器（temporal/depth ranks 128/32，scaling 2.0），GDPO 使用 G=8，音频/文本采样温度 0.8/0.7，top-k 250/25，学习率 1e-5；任务无关训练 β 从 0.05 向 KL 目标 0.3 调整，in-domain 训练固定 β=0.01。

## 一句话评价
SteerablePlex 通过在线指令注入接口与 GDPO 多目标强化学习，在保持全双工轮次转换能力的同时，将全双工语音模型转变为更可控、更可靠的多阶段用户模拟器。

---

## 2. CloudEar: Integrating Perceptual, Diagnostic, and Cross-Modal Evidence for Music Evaluation

**作者**: Qiqi He, Anqi Huang
**链接**: [2610.11672](https://arxiv.org/abs/2610.11672)
**分类**: Music Evaluation / Text-to-Music Evaluation | **关键词**: Music Evaluation, Pairwise Preference, Prompt Alignment, Perceptual Quality, Cross-Modal

## 核心痛点
- 生成音乐评估需要同时建模感知质量、技术音频质量和提示对齐。
- 现有方法常忽略信号级缺陷（如削波、异常响度），且回归模型存在中心趋势偏差，导致分数差异被压缩。
- 通用音频-文本模型虽能捕捉粗粒度语义，但忽略乐器、流派等细粒度音乐属性，高音频-文本相似度并不等于提示对齐。

## 方法创新
CloudEar 是一个成对（pairwise）评估框架，包含三个专家：
1. **Perceptual Expert（感知专家）**：对每首歌随机采样30秒片段，提取 MuQ 特征，经 Transformer adapter 得到感知表示；联合优化序数回归、连续回归和成对排序损失，总损失 L_PE=0.4L_OR+0.4L_reg+0.2L_pair，以缓解回归预测集中问题。
2. **Diagnostic Expert（诊断专家）**：引入信号级特征真峰值TP、削波率CR、峰值因子CF、积分响度LUFS，以及 HEAR（结合 MuQ 和 MusicFM）质量分数，与感知分数拼接后经线性层融合为 musicality score，用 BCE 成对偏好训练。
3. **Cross-modal Expert（跨模态专家）**：音频侧用 Genre Discogs400 预测400种风格、MTG-Jamendo Instrument 预测乐器标签；提示侧用 Qwen3-30B 抽取结构化流派/乐器信息，映射到同一标签空间；两层 Transformer 联合建模音频感知表示、音频属性向量和提示表示，输出 alignment score，并用 BCE 成对偏好训练。

## 实验结果
- 训练数据：AIME、MusicArena、约7000小时内部人工评分音乐（主要英文，来自五个生成模型，保留超过200位听众评分）；成对训练额外使用 MusicEval 和 CMI-Pref 训练集。
- 评测：PAM-Music、CMI-Test、MusicArena 测试集（1,340对，2025年7-12月生成，无训练重叠），指标为 P-ACC、SRCC、LRCC。
- 主要结果：CloudEar 全面优于 CMI-RM、HEAR、SongBench、MuQ 等基线。例如 CMI-Test 音乐性 P-ACC 0.8179、对齐 P-ACC 0.7635；PAM-Music P-ACC 0.7657、SRCC 0.7257、LRCC 0.7229。
- 消融：完整 CloudEar 优于 PE+HEAR、PE+DSP、PE only，说明三类证据互补；仅 Perceptual Expert 已在 CMI-Test 音乐性上超过 SongBench，在 MusicArena-Test 上保持竞争力。
- 发现：SongBench 和 HEAR 在无提示情况下也能获得高于随机的对齐准确率，暗示音乐性与对齐偏好之间存在相关性。

## 一句话评价
CloudEar 通过感知、诊断、跨模态三类专家证据融合，在成对偏好与评分相关性上实现了对生成音乐音乐性和提示对齐的更准确评估，但方法依赖多个外部模型和人工标注数据，完整系统复杂度较高。

---

## 3. Monaural Continuous-Radius Regional Speech Extraction with Cross-Radius Consistency Learning

**作者**: Biao Dong, Jie Chen, Jianwei Fang, Wei Xiao, Jiqing Han, Yongjun He
**链接**: [2610.11507](https://arxiv.org/abs/2610.11507)
**分类**: Target Speech Extraction | **关键词**: Regional Speech Extraction, Continuous-Radius Conditioning, Cross-Radius Consistency Learning, Monaural Speech Extraction, Distance-Based Speech Extraction, TF-GridNet

# 论文总结：Monaural Continuous-Radius Regional Speech Extraction with Cross-Radius Consistency Learning

## 核心痛点
- 传统目标语音提取（TSE）多依赖说话人身份/注册，目标未知或动态变化时灵活性不足。
- 源到麦克风距离可用于说话人无关提取，但现有单通道方法如 DSS 使用固定距离阈值，QD-TSE 使用局部距离窗口，无法实现连续可控的累积区域提取。
- 多通道区域语音提取依赖麦克风阵列，单通道连续半径区域提取研究不足。
- 查询半径对应的目标说话人集合具有嵌套结构，相邻半径若未跨过新的说话人边界，其目标信号应一致，但普通逐半径训练未显式约束这种一致性。

## 方法创新
- 任务定义：给定单通道混合 x(t) 和查询半径 r∈[0,Rmax]，Rmax=4m，目标为半径内所有说话人语音之和；目标说话人集合 S(r)={i|di≤r}；空集时目标为静音。推理只需用户指定物理半径，不需要估计源距离。
- 连续半径条件网络：采用轻量 TF-GridNet 骨干，STFT 后拼接幅度归一化实部、虚部和对数幅度；半径 r 归一化后经三层半径编码器得到频率相关表示 er，通过 FiLM 在相邻 TF 块之间进行特征级线性调制，使单个模型支持训练范围内的任意连续半径查询。
- 跨半径一致性学习（CRC）：同一混合采样 Q=4 个查询半径；仅在相邻半径目标说话人集合相同且非空时施加一致性约束，排除跨说话人边界的半径对，避免过平滑。一致性损失最小化两组预测波形的 L1 差异，并按公共目标 RMS 归一化。
- 训练损失：非空目标使用归一化重建损失 Lrec=10log10(1+MSE(error)/(MSE(target)+eps))；空目标使用 α·mean(|yhat|) 抑制输出，α=100；多半径损失平均后与 CRC 损失加权求和，λcon=0.1。

## 实验结果
- 数据与设置：gpuRIR 生成 1000 个房间用于训练/验证，房间尺寸 2-12m，高 2-5m，RT60 0.1-1.0s，源距离 0.3-5.0m；测试使用 dEchorate 实测 RIR 评估真实声学泛化。语音来自 AISHELL-1、AISHELL-2、THCHS-30、VCTK；噪声来自 DNS Challenge；16 kHz、4.5 s；训练/验证混合含两个说话人，噪声以 0.5 概率加入，SNR 0-15 dB。
- 基线：DSS 训练 1/2/3/4 m 四个固定半径模型；QD-TSE 使用 r_spk=0.5m 的局部距离窗口，并通过 1m 间隔划分求和来近似累积区域。
- 指标：full-target SI-SDR、partial-target SI-SDRi、empty-target attenuation、RCE（0.1m 查询网格上的半径一致性误差）。
- 主要结果：所提方法达到 29.25 dB SI-SDR、4.40 dB SI-SDRi、62.01 dB attenuation、0.46% RCE，优于固定阈值和局部范围基线。相比 DSS，full-target SI-SDR 提升 7.22 dB，partial-target SI-SDRi 提升 4.01 dB，empty-target attenuation 提升 5.89 dB；相比 QD-TSE 区间求和也取得更优区域提取效果。方法在更多说话人和加性噪声下仍有效。
- 实现：约 0.66M 可训练参数；Adam 优化器，初始学习率 6e-4，warmup 2000 步，ReduceLROnPlateau，batch size 1，最多 50 epochs；结果在三个随机种子下平均。

## 一句话评价
该工作将连续半径条件注入单通道目标语音提取网络，并利用目标说话人集合的嵌套结构设计跨半径一致性学习，在实测 RIR 上实现了高保真区域保留、强区域外抑制和良好半径一致性，是距离/区域语音提取方向的重要推进。

---

## 4. Toward accurate speaker inventories for online speaker diarization

**作者**: Youngki Kwon, Hee-Soo Heo, Minjae Lee, Bong-Jin Lee
**链接**: [2610.11278](https://arxiv.org/abs/2610.11278)
**分类**: Online Speaker Diarization | **关键词**: online speaker diarization, speaker inventory, speaker counting, speaker registration, latency, candidate speaker pool, commit-gated label assignment

### 论文信息

- 标题：Toward accurate speaker inventories for online speaker diarization
- 作者/机构：Youngki Kwon, Hee-Soo Heo, Minjae Lee, Bong-Jin Lee, NAVER Cloud Corporation, South Korea
- 主题：在线说话人日志中的说话人清单（speaker inventory）准确性，即正确返回说话人数量。

### 核心痛点

- 在线说话人日志系统需要维护一个不断增长的说话人集合，应用直接读取该清单：实时转录按出现顺序枚举说话人。
- 现有系统有两类增长规则：
  1. 固定说话人容量（speaker capacity）：预先设定系统最多能返回的说话人数或输出槽位；真实说话人数超过容量后，多个说话人被合并（merge），造成说话人数目过少。
  2. 无界、仅基于距离的注册：每个与已注册质心距离足够远的 embedding 都立即成为新说话人；噪声和话轮边界会不断触发注册，造成分裂（split），使说话人数目过多。
- 上述两类失败在 DER 上不一定被报告：DER 按时间加权，不报告返回了多少说话人；JER 虽然均衡每个参考说话人的权重，但仍基于最优映射，对计数及其方向不敏感。
- 在 VoxSRC-23 上：固定容量系统返回的说话人数比参考少 44–46%；无界跟踪器虽然 DER 最低，但返回的说话人数比参考多 63%。
- 因此需要一种能在没有固定容量的前提下，准确控制说话人注册的在线方法。

### 背景与基线

- 基线是 DC-OST，一种基于 embedding 的 tracker，没有固定说话人容量。
- 它以 0.5 s 为 embedding step，维护已提交质心注册表 S_t 和一个未匹配 embedding 的 buffer B。
- 路由：若 embedding e_t 到最近质心距离 d_min ≤ τ_t，则分配给该说话人；否则加入 B。
- 注册：当 |B| 达到预设大小 K 时，将 B 的中枢点（medoid）作为新说话人质心注册。
- 局限：
  1. 单一 buffer 混合所有未见说话人：两个交替出现的未见说话人会混在同一 B 中，被注册成一个说话人。
  2. 每个决策只依赖一次观测：单个 outlier 即可触发新说话人，被立即标为 N_t+1。

### 方法创新

- 整体仍基于 DC-OST，保留其路由规则和延迟承诺，只改变触发说话人注册的机制。两个核心组件：
- **候选说话人池（Candidate speaker pool）**：
  - 用池 P_t 替代单一 buffer，使未注册 embedding 按候选分开保存。
  - 注册表拒绝的 embedding，对每个候选计算它与候选成员距离的中位数；若最小中位数距离 ≤ τ_pool，则加入最近候选；否则新建候选。
  - 一个候选累积到 K 个成员后才注册为说话人，质心为成员归一化均值。
  - 由于每个成员都是通过 admission test 加入，K 个 embedding 是同一说话人的累积证据，而非恰好错过注册表的 K 个 embedding。
  - 两个交替的未见说话人会积累到不同候选；单个噪声观测不会留下痕迹；|P_j|=1 且 T_e 后无进展的候选被丢弃。
- **提交门控标签分配（Commit-gated label assignment）**：
  - 属于未决候选的输出进入有序队列 Q_t，携带 fallback（最近已注册说话人）和 provisional（候选的临时身份）两个可能身份。
  - 候选是否成为说话人在几步内确定，因此队列暂存输出而非猜测。
  - 等待由延迟预算 L_prov 限制：若候选注册，输出以其 provisional 身份释放；若达到 L_prov 仍未注册，则按 fallback 释放。
  - 没有说话人在确认前出现在输出中；超时输出不再重访，若候选后来注册，错误表现为 merge。
  - 队列按步骤顺序释放；已路由输出到达即决定，只可能被队头阻塞（head-of-line blocking）。L_prov 作用于队头，而非整个队列。
- 算法 1 描述单个 embedding step：路由测试、τ_pool 与 K 两个门控、候选注册、队列释放、过期候选丢弃。

### 实验设置与结果

- 数据集：九个公共数据集，共 1,907 条录音，包括 DIHARD I–III、VoxConverse、VoxSRC 2021–2023、AMI、AliMeeting。
- 评价指标：DER 及其分量 FA（误报）、MS（漏检）、SC（说话人混淆）；说话人计数误差 |e| = Σ_i |ε_i| / Σ_i N_ref_i，其中 ε_i = N_sys_i - N_ref_i，双向计数；latency 以分布报告。
- 前端：FireRed-VAD streaming detector（0.6M 参数 causal DFSMN，zero look-ahead）和 ReDimNet2 checkpoint b6-vb2+vox2 v0-lm.pt，训练于 VoxBlink2 与 VoxCeleb2；embedding 每 0.5 s 一步，仅检测语音。
- 主要结果：
  - 九个数据集 macro speaker-count error 从 225% 降至 21% of reference。
  - macro DER 从 17.59% 降至 15.95%。
  - 平均增加延迟 0.109 s over all outputs；91.4% 输出无额外延迟，8.6% 输出等待，平均等待 1.27 s，观测最大 4.16 s。
  - VoxSRC-23 上，+ Pool + Delay 同时取得最低 DER 和最准确说话人计数：DER 6.76%，|e|=16.0；相比之下 Baseline rule DER 7.40%、|e|=63.1；Streaming Sortformer |e|=46.2；LS-EEND |e|=43.7；DIART |e|=27.7。
  - DIHARD III 上，+ Pool + Delay：DER 24.31%，|e|=23.2；Baseline rule：DER 28.28%，|e|=294.6。
- 对比系统：DIART、Streaming Sortformer、LS-EEND、S2SND-M；基线为 DC-OST。

### 一句话评价

提出候选说话人池与提交门控标签分配，以少量可控延迟为代价，显著提升在线说话人日志的说话人清单计数准确性；在 VoxSRC-23 上同时获得最低 DER 和最准确的说话人数量，缓解了固定容量合并与无界分裂的两难。

---

## 5. Using the enrollment gallery as evidence: affine-invariant score calibration for target speaker tagging

**作者**: Hee-Soo Heo, Minjae Lee, Youngki Kwon, Bong-Jin Lee
**链接**: [2610.11272](https://arxiv.org/abs/2610.11272)
**分类**: Speaker Recognition (Speaker Verification / Target Speaker Tagging) | **关键词**: target speaker tagging, speaker verification, score normalization, score calibration, affine-invariant calibration, cohort-free calibration, enrollment gallery

# 论文总结：Using the Enrollment Gallery as Evidence: Affine-Invariant Score Calibration for Target Speaker Tagging

## 核心痛点

**任务背景**：Target Speaker Tagging (TST) 需要将长时多说话人录音分割为单说话人片段（diarization），并为每个片段分配已注册说话人身份或拒绝为非目标。TST 服务场景的一个天然优势是：系统会为每位注册说话人累积大量注册语音（enrollment），且这些语音与被识别的测试语音往往来自同一采集流程、同一录音条件，甚至同一音源池。

**关键问题**：一个很自然的问题是——能否直接把"其他已注册说话人的注册语音"当作 cohort，用于传统的分数归一化（Z-norm / T-norm / S-norm / AS-norm），从而省去外部 cohort 集？

**作者的发现（否定答案）**：不能。基于注册库（enrollment gallery）的 cohort 与分数归一化假设的"大规模、独立同分布冒充者集合"截然不同：
1. **注册语音按录音会话聚集**：多个说话人常在同一会话（如一次会议）中被注册，导致 gallery 的子集共享录音信道/房间/对话域。
2. **说话人相似度受会话影响**：同一或相似会话的两段语音（无论注册还是测试）相似度更高，因为共享信道被编码进 embedding。

因此，per-speaker 的 cohort 统计量（如 $
mu_e$）度量的是"该说话人的注册语音与 gallery 其余部分的接近程度"，而非冒充者行为。归一化会引入与说话人相关的分数偏移：
- $
mu_e$ 大的说话人（被很多人一起注册）被减去一个本不该存在的 offset，导致**整类说话人的目标片段被大量拒绝**（在 in-house 语料上，Z-norm 从 81.64% 掉到 41.72%，T-norm 47.84%，S-norm 46.28%）。
- $
mu_e$ 小的说话人（远离 gallery 注册）归一化后分数相对最高，**虚警集中在这类说话人身上**。
- 这破坏了"全局共享判决阈值"所需的跨说话人分数可比性。
- 对照实验：在声学条件几乎均匀的合成 TST-Bench 上，注册 cohort 不会失效（因为不存在信道的聚集），说明失败源于**注册条件的聚集**而非 gallery 规模。

## 方法创新：Gallery Affinity Verification

作者提出一种**无 cohort（cohort-free）标定方法**，核心思想是：**有用的信息量不是 per-speaker 的分数统计，而是一个片段在整个已注册说话人集合上的分数分布模式（profile pattern）**。

**关键性质：仿射不变性（affine invariance）**——对每个说话人引入的偏移（offset）和尺度（scale）畸变免疫，这正是破坏 cohort 归一化的两类畸变。

标识（identifier）的候选决策保持不变，只对选中候选 $c$ 的验证分数做标定。最终判决分数为：

$$D_c = s_c - \rho(s_{-c}) - \frac{\max(r_c^2 - f_c^2,\, 0)}{2 f_c}$$

其中 $s = [s_1,...,s_N]$ 为片段在 $N$ 个注册说话人上的 GMM 标定分数，$s_{-c}$ 为去掉候选后的"竞争者画像"（competitor profile，共 $m=N-1$ 项）。

### 创新点 1：竞争者画像离散度惩罚 $\rho(s_{-c})$

- 定义**对称分位间距半径（symmetric interquantile radius）**：
$$\rho(s_{-c}) = \frac{1}{2}\left[Q_{1-\tau}(s_{-c}) - Q_{\tau}(s_{-c})\right]$$
- 直觉：候选是 $N$ 个分数中的最大值，因此分布越宽，非目标片段的上分位数也越可能越过阈值，产生虚警。
- **无自由超参数**：尾部深度采用平方根规则 $d = \lfloor\sqrt{m}\rfloor$，即 $\tau = 1/\sqrt{m}$。这样每个分位数由 $\sqrt{m}$ 个样本支撑（估计稳定），同时尾部比例随 gallery 增大而消失（半径趋近全体散布）。
- 判据：真实目标片段与自身说话人近、与 gallery 其余部分近似均匀地不相似，竞争者画像窄、$\rho$ 小；冒充者则相反。
- 该统计量对"众多竞争者分数同时抬升"敏感，而对少数恰好像该片段的竞争者鲁棒。

### 创新点 2：注册画像偏离度惩罚

- 惩罚片段的竞争者画像与候选说话人的注册画像之间的一致性偏离，用残差 $r_c$ 相对于候选 $c$ 正常残差水平 $f_c$ 来度量。
- 同样设计为仿射不变，免疫每说话人 offset/scale 畸变。

### 两大项都仿射不变，因此避免了注册 cohort 统计量带来的说话人相关偏移问题。

## 实验结果

**数据集**：(1) 合成基准 TST-Bench（由 MLS 有声书合成，声学条件近乎均匀）；(2) 自建 in-house 会议语料。外部 cohort 为 VoxBlink2 的 2170 条 4 秒语音（与 embedding 窗长匹配）。评价指标 DIR@FAR=1%。

**表 1 关键结果（DIR@FAR=1%, %）**：

| 方法 | In-house (Ext.) | In-house (Enr.) | TST-Bench (Ext.) | TST-Bench (Enr.) |
|---|---|---|---|---|
| 无归一化 | — | 81.64 | — | 87.89 |
| Z-norm | 85.26 | 41.72 | 81.28 | 82.20 |
| T-norm | 85.42 | 47.84 | 80.26 | 80.74 |
| S-norm | 85.35 | 46.28 | 82.34 | 84.00 |
| AS-norm | 82.75 | 77.42 | 83.17 | 80.76 |

**主要结论**：
1. 外部 cohort 上 Z/T/S-norm 相对基线提升约 4 pp；但注册 cohort 上同类方法损失约一半基线精度（失败）。
2. 合成 TST-Bench 上注册 cohort 不失效（与外部 cohort 相当），验证了失败根源是注册条件聚集。
3. 提出的 Gallery Affinity Verification 在**有无传统分数归一化的条件下都能提升 tagging 精度**，并且与常规归一化**组合使用时还有额外增益**。

**系统设置**：遵循 [1] 的 TST 框架；采用 [11] 的解耦 identifier–verifier 架构（两个 extractor 为同一 embedding 模型不同训练阶段的 checkpoint，提供多样性）；cosine 相似度打分；聚类式 diarization 前端；[10] 的会话级 GMM 标定（双分量 GMM 聚合 verifier 分数，对聚类错误鲁棒）；单一全局阈值 $\theta$ 判决。注意本文在候选集设置上比 [1] 更严格：每个会话的候选集包含全部注册说话人（不利用出席信息）。

## 一句话评价

本文通过严谨的实证分析揭示了"用注册库当 cohort"在 TST 中系统性的归一化失效机理，并据此提出一个无需外部 cohort、对每说话人仿射畸变免疫的两项标定方法，原理清晰、无自由超参数、可与现有归一化互补，是 TST 分数标定方向一篇扎实且有实用价值的贡献；不过实验主要依赖单方 in-house 语料与合成基准，更大规模、多域真实会议场景的验证仍待补充。

---

## 6. Randomized Scores and Diverse Timbres: Augmenting Automatic Music Transcription with Online-Generated Data

**作者**: Haiwen Xia, Chao Zhang, Qiuqiang Kong
**链接**: [2610.11197](https://arxiv.org/abs/2610.11197)
**分类**: Automatic Music Transcription | **关键词**: Automatic Music Transcription, Synthetic Data, Data Augmentation, Domain Generalization, Timbral Diversity, Online Sampler-Renderer

# 论文总结：Randomized Scores and Diverse Timbres: Augmenting Automatic Music Transcription with Online-Generated Data

## 核心痛点
自动音乐转录（Automatic Music Transcription, AMT）需要大量“音频-符号标注”成对数据，但精确的多音符标注成本极高，导致监督数据在音乐与声学条件上覆盖有限。合成数据可以大规模提供监督信号，但现有研究尚不清楚：有效迁移究竟更依赖**真实的乐谱结构**，还是更依赖**广泛的音色覆盖**。现有渲染式方法保留源乐谱结构，增强式方法重组已有音频-标签对，但二者常将和声、复调与音色变化耦合，难以分离影响因素。

## 方法创新
论文提出一种**在线 sampler–renderer 数据生成管线**，将乐谱结构采样与音色渲染解耦：

1. **统一损坏采样器（Symbolic Sampler）**
   - 对采样的 MIDI clip 中的音符事件进行可控损坏。
   - 每个 clip 采样损坏率 ρ∈[0,1]，每个音符以概率 ρ 被替换为来自因子化音符分布 r(e) 的中间音符。
   - 通过插值强度 s∈[0,1] 控制替换程度：s=0 保留原音符，s=1 完全替换。
   - 三种设置属于同一采样器：
     - **Source**：ρ=0，返回原 clip。
     - **Corrupted**：ρ∼U[0,1] 且 s>0，部分音符向因子化分布移动。
     - **Note-factorized**：ρ=1, s=1，所有非 program 属性独立重采样。

2. **音频渲染器与音色覆盖（Renderer and Timbral Coverage）**
   - 渲染器从 pψ(z|y) 采样兼容的音色选择 z，生成音频 x=R(y,z)。
   - **Note-renderer**：使用 NSynth 录音逐音符渲染，并对齐起音、平滑衰减以匹配符号时值。
   - **Stem renderer**：将完整 MIDI stem 送入 Pianoteq，采样兼容预设。Pianoteq 免费版包含 797 个预设、25 个乐器组，但排除 8 个固定音高，受影响音符被重标记到同音级最近可演奏八度。
   - 钢琴实验比较 4%、20%、100% 的 program-0（Acoustic Grand Piano）预设子集，以及 programs 0–7（Broad Piano）。
   - 在线生成样本与离线音频按固定比例混合训练，每个样本损失权重相同。

3. **简化多通道自回归转录模型**
   - 编码器：卷积前端 + 时间 Transformer，使用 RoPE 与 RMSNorm，得到共享特征 E。
   - 通道拆分：线性投影后拆成 C=13 个通道流（参考 YourMT3+），每个通道对应粗粒度乐器类。
   - 解码器：所有通道共享参数，每个解码块包含因果自注意力、对相应编码器流的交叉注意力、FFN。通道间条件独立可并行解码，通道内 token 保持自回归依赖。
   - 训练目标为自回归 token 交叉熵 L_AR，在线与离线样本仅来源不同，共享同一目标。

4. **实验设计**
   - 实验 1、2 为 online-only，分别消融符号采样与音色覆盖，模型固定。
   - 实验 3、4 结合离线音频与在线数据，测试互补性。
   - 输入：2.048 秒、16 kHz、128 mel bins、8 ms hop。
   - Base 模型约 60M 参数，Large 模型约 190M 参数。
   - 评估：MAPS 域外钢琴迁移；MulTTiPop、RWC、Slakh/test、MAESTRO/test。指标为 50 ms 容忍度的 onset F1（Agn 或 Prog）。

## 实验结果
- 表 1 固定 NSynth 渲染器，比较符号采样器：
  - Source：MAPS 64.99，MulTTiPop 22.92，RWC 36.41，Slakh 49.55。
  - Corrupted（ρ∼U[0,1], s=0.5）：MAPS 67.28，MulTTiPop 21.58，RWC 36.70，Slakh 50.30。
  - Corrupted（ρ∼U[0,1], s=1）：MAPS 68.28，MulTTiPop 21.53，RWC 35.72，Slakh 49.78。
  - Note-factorized（ρ=1, s=1）：MAPS 61.18，MulTTiPop 12.56，RWC 28.21，Slakh 36.83。
- 核心发现：
  1. **中等程度的音符事件损坏不会损害迁移，反而可能提升迁移**，说明真实乐谱结构并非必要。
  2. **在固定音符事件分布下，扩大渲染器侧音色覆盖可带来单调的域外泛化增益**。
  3. **在线渲染样本在强的组合数据场景中仍能补充真实数据与现有合成数据**。
  4. 深度随机化（Note-factorized）会显著损害性能，表明完全丢弃音符级结构属性并不优。

## 一句话评价
论文通过解耦乐谱结构与音色覆盖，系统性地表明合成 AMT 数据应优先覆盖音符级属性及其音色实现，而非追求真实联合乐谱结构；其在线 sampler–renderer 管线与简化多通道架构为 AMT 数据增强和域泛化提供了实用且可复现的范式。

---

## 7. SmoothConv and DuplexConv: Complementary Mandarin Multi-Party Conversational Speech Corpora for Speech Interaction

**作者**: Chengyou Wang, Mingchen Shao, Chunjiang He, Zeyu Zhu, Jierui Guo, Bingshen Mu, Zikai Liu, Hanke Xie, Yuhang Dai, Zhou Zhu, Lei Xie
**链接**: [2610.11150](https://arxiv.org/abs/2610.11150)
**分类**: Multi-Party Conversational Speech Corpus & Benchmark | **关键词**: Mandarin multi-party conversational speech, speech corpus, benchmark, speech interaction, speech separation, multi-speaker ASR, turn detection, automatic annotation pipeline

## 核心痛点

- 大型音频语言模型（LALMs）推动自然、实时、连贯的语音交互系统发展，但系统需要建模复杂会话行为，如轮次转换（turn-taking）、语音重叠（overlapping speech）与说话人协调（speaker coordination）。
- 现有多方对话语料库大多缺乏**同步的说话人级别语音轨道（synchronized participant-level speech tracks）**以及**全面的交互行为细粒度标注**，限制了其在真实多方语音交互建模中的适用性。
- 高质量多方对话数据需要两个互补要素：各参与者独立的同步语音信号 + 描述内容、说话人信息与交互行为的细粒度标注。
- 人工标注可靠但昂贵、难以扩展；自动标注可扩展但可能引入识别、对齐与语义解释错误。因此需要同时提供**可靠分析用的人工校验数据**与**可扩展训练用的大规模自动标注数据**。
- 现有中文资源仍不足：Switchboard/Fisher 仅限英语双人电话对话；CHiME-5 面向鲁棒 ASR 与语音分离但缺少细粒度标注；AMI/AliMeeting/AISHELL-4 等基于麦克风阵列或缺少同步参与者轨道与交互行为标注。

## 方法创新

- 提出两个互补的中文多方对话语音语料库：**SmoothConv** 与 **DuplexConv**，总计 **2,100 小时**，覆盖 **Tutoring（辅导）** 与 **Social Chat（社交闲聊）** 场景，每段会话包含 **2–4 路同步参与者级语音轨道**。
- **SmoothConv**：100 小时，来自 2,503 个对话片段，经人工详细校验，覆盖转写、说话人身份、话语边界、轮次状态与交互属性；由 4 名标注员标注并由 3 名资深标注员复核，用于细粒度分析与可靠评测。
- **DuplexConv**：2,000 小时，来自 93,709 个片段，平均时长 76.8 秒（8–618 秒），通过可扩展自动标注流水线构建，支持大规模模型训练。
- **构建流水线**分两阶段：
  - **阶段一：逐通道识别与说话人标注**——VAD 检测各通道语音区域并保持时间轴同步；多套 ASR 系统（FireRed ASR、FunASR、FireRed ASR2、Qwen ASR）独立转写并用 **ROVER** 融合；**Dasheng** 过滤非语音段（音乐、噪声、静音等）；**Pyannote diarization**、**Qwen3-ForcedAligner-0.6B** 与 **3D-Speaker clustering** 精化说话人归属与话语边界，获得说话人属性化转写。
  - **阶段二：多维度细粒度标注**——轮次状态（**complete / incomplete / backchannel / wait**）由 **Qwen3-32B** 基于文本上下文预测候选，再由 **Qwen3-Omni** 引入声学信息验证；情感、非语言事件、性别、年龄由 **Gemini 2.5 Pro** 自动标注。SmoothConv 使用预定义情感类别（neutral、happy、confused、curious、angry、surprise、sad、contempt、worry、disgust、fear、sorry），DuplexConv 使用自由形式情感描述；DuplexConv 年龄分为 child、teenager、adult、middle-aged、elderly 五组。
- **质量验证**：从 DuplexConv 随机抽取 20 小时子集人工核验，整体通过率 **82.4%**；自动轮次状态标签与人工标注一致率 **91%**；当预测不一致时，对 incomplete 与 backchannel 优先采用基于音频的决策（韵律线索更重要）。
- 发布 **SmoothConv Benchmark**：
  - **语音分离 / MSASR 评测集**：9.48 小时、255 个片段、平均 133.9 秒、2–4 说话人、Tutoring 56.0% / Social 44.0%、严格说话人不相交划分、平均语音重叠率 3.33%。
  - **轮次检测评测集**：Complete 14,709 样本 / 9.64 h；Incomplete 3,643 / 2.15 h；Backchannel 3,080 / 0.42 h；Wait 1,000 / 0.71 h（合成样本，仅用于评测，由 DeepSeek V3 生成文本、IndexTTS2 合成语音并人工检查）。

## 实验结果

- 在三个代表性下游任务上评估所提资源：**语音分离（speech separation）**、**多说话人自动语音识别（MSASR）**、**对话轮次检测（turn detection）**，覆盖多方语音交互的三个重要方面。
- 摘要指出实验结果证明了所提资源在多说话人语音交互建模中的有效性，并体现了大规模自动标注数据与高质量人工校验标注的互补价值。
- 受限于所提供的论文片段，实验表格与具体指标（如分离 SI-SNRi、MSASR WER、轮次检测 F1 等）被截断，未能提取到完整数值结果。

## 一句话评价

本文构建并发布了 2,100 小时互补式中文多方对话语音语料库 SmoothConv 与 DuplexConv，兼具人工校验的高质量细粒度标注与可扩展自动标注的大规模训练数据，并配套 S 基准，为多说话人语音交互（分离、MSASR、轮次检测）研究提供了重要的数据与评测基础设施。

---

## 8. Towards Automated Clinical Behavioral Coding with Large Language Models: A Case study Using BOSCC recordings of Children

**作者**: Jordan Prescott, Aditya Kommineni, Tiantian Feng, Megan Micheletti, Alyssa Viggiano, Luis Angeles, Anfeng Xu, Lynn Perry, Catherine Lord, Daniel Messinger, Shrikanth Narayanan
**链接**: [2610.11106](https://arxiv.org/abs/2610.11106)
**分类**: Clinical Behavioral Coding with Large Language Models | **关键词**: Autism Spectrum Disorder, BOSCC, Large Language Models, Behavioral Coding, Child Speech, Multimodal LLM, Speaker Diarization

# 论文总结：Towards Automated Clinical Behavioral Coding with Large Language Models: A Case study Using BOSCC recordings of Children

## 核心痛点
- 自闭症谱系障碍（ASD）治疗干预常以社交沟通技能为目标，需要可靠的行为变化测量工具。
- BOSCC（Brief Observation of Social Communication Change）是一种经过验证的治疗反应测量方法，基于儿童与训练有素检查者之间约 12 分钟的简短游戏和社交沟通互动，由专家按照行为锚定评分标准对 20 个项目进行 0-5 分评分。
- 人工 BOSCC 编码资源密集、耗时、依赖专家，限制了可扩展性和可及性，且容易引入人为错误。
- 现有基于 LLM 的自闭症研究多聚焦诊断或行为特征描述，能否可靠支持 BOSCC 编码尚不明确。

## 方法创新
- 首次系统评估通用大语言模型（LLM）在 BOSCC 两个语音相关项目上的自动编码能力：Verbal Exchanges on a Topic（VET）和 Stereotyped and Echoed Speech（SES）。
- 不直接预测最终分数，而是将 BOSCC 决策树分解为一系列二元问题，每个问题使用特定提示让 LLM 独立回答，再按照树结构链接答案以确定终端代码和项目分数。VET 包含 6 个二元决策问题和 7 个终端节点；SES 包含 5 个二元决策问题和 6 个终端节点。
- 评估四种与语音相关的输入条件：transcript、diarized transcript、diarized transcript with audio、audio-only。
- ASR 使用 NVIDIA Parakeet TDT 0.6B v2；说话人角色分离使用 Xu 等人的儿童-成人分离模型；语句级语音清晰度标签来自 ChildVox 模型。
- 提示结构包括共享 BOSCC 任务前言、模态特定说明、决策问题、手动推导的操作定义与排除项、编码指导、两个允许响应和固定 JSON 输出格式。

## 实验结果
- 数据集：163 个 BOSCC-PSYF 录音，共 326 个 6 分钟片段，总时长 32.6 小时；儿童年龄 4.33±0.78 岁，22 名男性/16 名女性，ASD/DD/TD 诊断计数为 7/16/15。
- 评估模型：Qwen2.5-7B-Instruct、Qwen3.5-9B、Qwen3.5-9B (thinking)、Qwen3.8-27B-FP8、Qwen3.8-27B-FP8 (thinking)、Gemma 4 12B-IT、Gemma 4 12B-IT (thinking)。
- 指标：零样本终端代码平衡准确率，使用 5 样本多数投票，并报告 10,000 次按终端代码分层 bootstrap 的 95% 百分位置信区间。
- 随机机会平衡准确率：VET 为 14.3%，SES 为 16.7%。
- 最佳零样本平衡准确率超过随机水平 19.3 个百分点；VET 在带说话人分离转录条件下，Qwen3.5-9B (thinking) 和 Gemma 4 12B-IT 达到 33.6%；SES 最佳为 Gemma 4 12B-IT (thinking) 在带说话人分离转录条件下达到 26.3%。
- 说话人分离在 14 个比较中改善了 12 个；音频输入和少样本提示带来的增益不一致。
- LLM 在评估言语交流方面表现较好，但在识别非典型语音模式方面表现不佳；性能因评分决策而异，跨诊断组没有一致模式。
- 错误分析表明，应用 BOSCC 编码标准和解释模糊语音证据仍是主要挑战，ASR 相关错误也有影响。

## 一句话评价
该研究系统评估了通用 LLM 在 BOSCC 语音相关项目自动编码中的可行性，表明 LLM 在结构化行为编码上具有潜力，但距离可靠临床应用仍需解决评分标准应用和模糊语音证据解释等核心挑战。

---

## 9. Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners

**作者**: Xilin Jiang, Shun Zhang, Tejas Jayashankar, Yinghao Aaron Li, Osama Hanna
**链接**: [2610.10868](https://arxiv.org/abs/2610.10868)
**分类**: Voice Aesthetic Modeling | **关键词**: Conversational Voice Aesthetics, Speech Large Language Model, Group Relative Policy Optimization, Human Alignment, CANDOR

### 核心痛点
- 语音不仅是文字载体，其音高、节奏、情感、表达方式等构成“语音美学”对象；现有语音质量/奖励模型（PESQ、POLQA、MOSNet、DNSMOS、UTMOSv2、Audiobox-Aesthetics、AudioJudge、WavReward、SpeechJudge、GSRM）多缺少对话上下文，难以判断情感与 delivery 等依赖前文回合的属性。
- 情感、温暖、自信等感知属性主观且无唯一 ground truth，单个人类标注有偏且不一致，需要人类群体监督与能建模投票分布的优化目标。
- 真实与合成语音越来越多，需要同一公平标准描述二者。

### 方法创新
- 提出 Conversational Voice Aesthetic Model (CVAM)，基于 Qwen2.5-Omni 7B speech LLM，输入对话上下文音频与目标响应音频，输出结构化 JSON：gender、pitch、pacing、emotion、delivery 共 9 个类别标签及证据化描述。
- 四个美学字段：pitch/pacing 为客观字段，由工具测量（Praat F0、faster-whisper-large-v3 转写、NeMo Forced Aligner+CMUdict 音素对齐）和证据日志监督；emotion/delivery 为感知字段，由人类判断。
- 数据：从 CANDOR 自然英语对话语料构建 10k+0.5k 训练和 0.5k 测试对话回合，3–30 秒，去除 backchannels 和敏感主题；用 Qwen3-TTS 为每个真实响应生成 voice clone 和 voice design 两个合成版本，三倍数据，提升稀有情感/表达覆盖。
- 标注：30k 合成样本由 Gemini 3.1 Pro 生成描述与标签用于 SFT；1.5k 人类样本仅用于 RL 标签，每响应约 10 票，感知标签取人类多数投票。
- 两阶段训练：先 SFT 合成数据建立 JSON 输出格式与美学描述，再用 GRPO 在人类票分布上对齐。只用人数据会 data-starved，只用合成数据会继承 LLM 标注器偏差。
- GRPO 奖励：9 个标签中 gender+4 个客观标签占 5/9 准确率奖励，但预测近乎完美、方差小；4 个感知字段占 4/9，主要提供学习信号。提出 distribution-based reward，将 group 内预测标签频率与人类投票分布匹配，而非只强化多数标签，并排除当前 rollout、使用 Laplace 平滑。

### 实验结果
- 在 1500 个测试对话回合的 emotion 和 delivery 标签上，CVAM（SFTsynth + GRPOhuman）相对人类多数投票标签的 accuracy 和 macro F1 均优于 Gemini 3.1 Pro 及 Gemma-4-12B、Qwen3-Omni、Qwen2.5-Omni、Step-Audio-2 mini 等开源 speech LLM。
- CVAM 甚至超过 single-human-vs-rest agreement，说明其与人类群体判断的一致性高于单个人类与其余人类的一致性。
- 两阶段训练优于仅人类数据、仅合成数据或两者混合 SFT。

### 一句话评价
CVAM 将对话语音美学建模形式化为“上下文语音输入—结构化美学描述/标签输出”，通过合成 SFT + 人类投票分布 GRPO 的两阶段后训练，在主观感知字段上实现了优于强基线并超越单人类一致性的对齐效果。

---

## 10. STEMMA: Song-to-Stem Multi-Audio Reasoning for Large Audio Language Models

**作者**: Hoyeol Sohn, Wonil Kim, Keunhyoung Kim, Sangeun Kum, Taehyoung Kim, Dongjoo Moon, Theerasak Charoenchob, Teeratep Weerapang, Jongpil Lee, Juhan Nam
**链接**: [2610.11884](https://arxiv.org/abs/2610.11884)
**分类**: Music Understanding and Multi-Audio Reasoning | **关键词**: Multi-Audio Reasoning, Large Audio-Language Models, Music Question Answering, Instruction Tuning, Hierarchical Music Structure, Relation-First Data Construction, Stem/Section Provenance

# STEMMA: Song-to-Stem Multi-Audio Reasoning for Large Audio Language Models

## 核心痛点
现有大型音频语言模型（LALMs）和音乐问答数据集大多将每首录音视为独立样本，或在没有已知制作关系的情况下比较独立采样的曲目。音乐理解中真正需要的是跨音频 grounding：比较歌曲、段落和分轨（stems）之间的关系，例如两段音频是否来自同一 track 或同一 section，以及哪个 stem 属于哪个 mixture。传统 audio-first 采样下，结构性关系非常稀疏：从 N 首曲目中独立抽取两段音频共享同一 track 的概率为 O(1/N)，共享同一 section 更稀有，导致采样浪费大量被拒绝的 tuple。已有工作如 Beyond Single-Audio、PolyAudio、MUGEN、Jamendo-MT-QA 等虽探索多音频比较，但没有系统利用音乐制作数据中已知的 song-section-stem provenance，且候选集增大时性能下降。

## 方法创新
论文提出 STEMMA，一个围绕 production provenance 构建的多音频音乐问答框架。核心创新是 relation-first 数据构建策略：先指定目标关系，再查询 catalog 中满足该关系的正例和违反该关系的 hard negatives，而不是先采样音频再判断关系是否成立。标签直接由 catalog provenance 决定，而不是由语言模型从 metadata 生成。

具体流程：
1. 构建可查询 catalog：将每首歌按层次结构切分为有序 section，每个 section 再分离为各个 musical role；每个 excerpt 对应一个 section，包含完整 section mixture（section）或一个分离 role（section stem）。每行存储四个 provenance 字段：track、section index、section category、stem role，以及 tempo、key、instruments、genres 等音乐属性。
2. 关系查询：relation 是声明式记录，指定 anchor、正确候选和 distractor 的来源，以及正例和 hard-negative tuple 条件。条件使用八种算子作用于 catalog 字段：same/different、close/far（带容差）、overlap/no overlap（带最小计数）、greater/less。
3. QA 格式：pair QA 对两段音频问 yes/no 或短值；candidate QA 给一个 anchor 和四个音频候选，让模型选择，选项是音频而非文本。关系与格式正交，同一关系可生成多种任务。
4. 一条 SQL 查询即可生成任务 tuple、答案和答案位置，hard negatives 保留部分上下文但违反目标关系。

论文列出九种关系：结构性关系包括 same track、adjacent section、same section、parent-child；属性关系包括 same key、same tempo、tempo order、instrument overlap、genre overlap。

## 数据与训练
- STEMMA-Bench：held-out benchmark，基于完整歌曲的 sections 和 section stems，而非独立采样曲目。
- STEMMA-Instruct：track-disjoint 训练集。其两个角色 Relation MultiQA 和 coreference 各贡献 97,272 个实例，共 194,544 个实例，每个实例含 1 到 5 个音频输入。Relation 实例中 48% 为 section-only，45% 为 section-stem-only，7% 为 mixed。
- Coreference：将 2 到 4 首不同 track 的完整歌曲在各自标签下拼接，要求模型把语言引用（如 Audio A）正确 grounding 到对应音频输入，并在匹配标签下重复每首歌自己的全曲答案。
- Catalog 来自三个 full-song 集合：15,856 首内部制作歌曲（有 authored metadata：section 边界、分离 stems、tempo、key、genre、instrumentation）；69,297 首 JamendoMaxCaps；12,119 首 Free Music Archive 中短于 600 秒且可商用许可的子集。公开语料的所有字段由音频估计：section 用 SongFormer，stems 用 SCNet，key/tempo 用 Essentia，genre/instrument tags 用 Discogs-EffNet。
- 微调两个 backbone：Music Flamingo 和 MOSS-Music。二者均已针对单音频音乐理解做过 instruction tuning。训练为 full fine-tuning 1 epoch，batch size 128，learning rate 1e-5，在两张 B200 GPU 上完成。

## 实验结果
摘要报告：在 STEMMA-Instruct 上微调两个 LALMs 可提升多音频推理能力，其中结构关系（直接由 catalog 决定的关系）提升最大，同时保持单音频音乐理解能力。STEMMA-Bench 用于评估。更细的数值结果在截断部分未给出。

## 一句话评价
STEMMA 通过 relation-first 和 song-section-stem provenance 将多音频音乐推理从随机配对比较推进到可查询、可控制负例、标签可验证的结构化数据构建范式，为 LALMs 的跨音频 grounding 提供了高质量 benchmark 与 instruction 数据。

---

## 11. Reference-Free Singing Pitch Correction via Music-Constrained Sequence Editing

**作者**: Biao Dong, Jiajun Li, Binzhen Zhu, Mingwei Yi, Tong Liu, Yuanhao Zhang, Jiqing Han, Yongjun He
**链接**: [2610.11524](https://arxiv.org/abs/2610.11524)
**分类**: Singing Pitch Correction / Singing Voice Processing | **关键词**: Reference-free singing pitch correction, Music-constrained sequence editing, Symbolic music encoder, Tonal-aware reranking, MusicBERT

# 论文总结：Reference-Free Singing Pitch Correction via Music-Constrained Sequence Editing

## 核心痛点
- 现有演唱音高修正方法依赖目标旋律、伴奏、专业模板或预定义音阶，在用户自生成无伴奏录音、即兴哼唱、旋律草图和缺少工程文件的旧录音等场景中不可用。
- 无参考修正不同于常规音高估计：不仅要提取演唱音高，还要判断每个音是否应被修改以及如何修改。
- 演唱音高修正具有音乐特殊性：音符有效性不仅取决于音高值，还取决于旋律上下文、调性结构和演唱表情，不能直接套用通用序列纠错。
- 需要选择性编辑错误音符并保留正确音符，避免全序列预测引入不必要改动。

## 方法创新
1. 任务形式化：将无参考演唱音高修正建模为音乐约束下的序列编辑任务。输入为音符级演唱 MIDI 序列 X={x_i}，x_i=(p_i,d_i,s_i,e_i)，其中 p_i、d_i、s_i、e_i 分别为音高、时值、起始位置和结束位置；目标是输出修正后的 Y={y_i}，y_i=(p̂_i,d_i,s_i,e_i)，修正量为 Δ_i=p̂_i-p_i。引入二值编辑指示 z_i，表示音符 i 是否需要修正，最终 p̂_i=p_i+Δ̂_i。
2. 演唱感知音乐上下文编码器：采用预训练符号音乐模型 MusicBERT 作为骨干，并冻结其参数；在 12 个 Transformer 块后插入轻量演唱域适配器，门控形式为 A_l(h)=σ(g_l) W2_l Dropout(GELU(W1_l LN(h)))，得到适配表示 H~=H^12，以弥补通用 MIDI 与单声部、演唱特有音高变化之间的领域差异。
3. 分层修正建模：设计两个轻量修正头，联合建模修正必要性和有符号音高修改。必要性头输出 a_i=P(z_i=1|h~_i)；修改头在非零偏移集合 D≠0={-3,-2,-1,+1,+2,+3} 上输出 b_i(d)=Softmax(f_mod(h~_i))_d。二者构成因子化音高编辑分布：当 d=0 时 P(Δ_i=d|h~_i)=1-a_i，否则为 a_i b_i(d)。损失为 L=L_nec+L_mod，必要性用所有有效音符上的二分类交叉熵，修改用被扰动音符上的交叉熵。
4. 调性感知候选重排序：无需目标旋律或真值调性。对输入 X 使用 Krumhansl–Schmuckler 调性发现算法，构建时长加权的 12 维音级直方图 u_X，并与 24 个大小调模板做 Pearson 相关，经温度 τ=0.15 的 Softmax 得到软调性后验 ρ(k|X)，进而得到输入相关音级先验 r_X(v)。用后验熵和输入音符数计算歌曲级置信度 c(X)。对每个音符在候选集合 D={0,±1,±2,±3} 上计算 S_i(d)=logP(Δ_i=d|h~_i)+λ c(X) log r_X((p_i+d) mod 12)，取 argmax 得到最终修正量。该策略是软调性约束而非硬性单音阶约束，可将模糊候选偏向调性兼容解。
5. 完整流程：SOME 从无伴奏演唱录音中提取音符级音高、起始和时值，RMVPE 提取帧级 F0 用于重建；将音高量化到离散半音，乐器设为固定人声码，估计小节位置、拍号和速度以构造 MusicBERT octuple 表示；符号修正后，在稳定区域做基于半音的音高移动，在音符边界线性插值映射回 F0 轮廓，并用 NSF-HiFi-GAN 重合成音频。

## 实验与结果
- 训练数据：从 16,000 首专业录音（约 1,060 小时中英文流行歌曲）提取演唱 MIDI 并施加合成音高扰动。音高限制在 MIDI 36–84（C2–C6）。每个序列扰动 20% 音符，使用六个非零偏移；70% 扰动为独立扰动，30% 形成 2 至 4 个音符的相关跨度。合成扰动仅用于模型开发，真实成对数据只用于评估。
- 评估数据：私有成对演唱数据集，包含中英文流行歌曲，每首歌有业余和专业演唱版本，由声乐学生录制。使用动态时间规整（DTW）对齐以获得音符级对应关系。按歌曲划分：20 首验证歌（8,299 音符）和 80 首留出测试歌（30,682 音符）。所有超参数包括调性重排序强度仅用验证集选择。专业演唱作为评估参考而非绝对真值，因为演唱间可能存在表情差异。
- 主要结果：方法将音符级音高准确率从 73.25% 提升至 83.43%，比基于上下文的基线高 3.99 个百分点，同时在错误修正和正确演唱音符保留之间取得平衡。

## 一句话评价
该工作把无参考演唱音高修正转化为音乐约束下的序列编辑问题，结合冻结 MusicBERT 与轻量演唱域适配器、分层必要性/修改预测以及输入相关调性重排序，在没有目标旋律和调性标注时显著提升音准，并兼顾音乐性与正确音符保留。

---

## 12. Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech

**作者**: Shiao Zhu, Lianbo Liu, Sizhen Lyu, Yuzhe Wang, Sheng Li, Takahiro Shinozaki
**链接**: [2610.11461](https://arxiv.org/abs/2610.11461)
**分类**: Conversational Text-to-Speech | **关键词**: Speech-Rewarded Style Planning, Conversational TTS, Speaking Style Control, GRPO, Reinforcement Learning, Speech Caption, Large Language Models, Expressive Speech Synthesis

# 论文总结：Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech

## 核心痛点
- 对话 TTS 中，同一句回复因语气不同效果不同，仅靠回复文本无法决定合适说话风格。
- 自然语言风格描述是 LLM 与可控 TTS 的可解释接口，但现有做法常把语音 caption 作为伪标签，将目标声学信息压缩成文本，导致声学细节丢失。
- 更关键的是，描述保真度不等于对特定合成器的有效控制：即使风格描述准确，也未必能诱导出最接近目标语音的合成结果。
- 实证：同一话语的候选风格指令之间，语音-文本对齐 T2S 分数（ParaCLAP-C、ParaCLAP-S、CLSP）与下游声学相似度 S2S、情感相似度、-MCD 仅弱相关；按 T2S 选指令只略优于随机，而按下游声学指标选指令在全部五个下游指标上更好。说明描述对齐只是下游控制的弱代理。

## 方法创新：Speech-Rewarded Style Planning (SRSP)
- 问题建模：给定纯文本对话历史 H、回复文本 y、同说话人 prompt 音频 p 和目标语音 token s，风格策略 πθ(z|H,y) 生成自然语言风格指令 z；训练时 s 只用于构造奖励，推理时规划器只接收 H 与 y。
- 奖励设计：用冻结下游 TTS 模型对目标语音 token 的 teacher-forced 似然作为反馈。候选指令 z_i 的奖励 R_i = -L_TTS(z_i) - P_i，其中 L_TTS 是冻结 TTS 自回归 LLM 在目标语音 token 序列上的平均 teacher-forced 交叉熵，P_i 是辅助惩罚，抑制过短、泛化、重复的风格指令。
- 优化算法：采用 GRPO，对每个训练实例采样 G 个候选指令，在同一 (y,s) 组内标准化奖励得到优势 A_i；使用带 KL 惩罚的裁剪目标更新规划器，KL 参考策略为初始冻结策略。无需目标风格 caption 监督。
- 实现细节：Qwen3.5-9B 作为 planner，rank-16 LoRA 适配所有线性层；Fun-CosyVoice3-0.5B 作为冻结奖励与合成模型；G=8，学习率 2×10^-6，clip η=0.2，KL β=0.075；训练温度 1.3，测试 0.7；辅助惩罚包括少于 6 词罚 5、6–11 词罚 0.5、重复 bigram/trigram 罚 0.01，并使用每 worker 2,048 条生成历史的滚动惩罚。

## 实验结果
- 数据：ISCSLP 2026 CoT-TTS 英文子集，经时长、语音比、响度、转写长度、参考相似度、自然度、噪声等筛选得到 299.75 小时池；四个 dev/test 划分各 2,750 条（约 5 小时）。dev in/test in 留出训练中出现过的 movie 场景，dev out/test out 留出整个 movie；剔除与留出集在目标或对话上下文上重叠的训练样本后，剩 277.60 小时训练。
- 基线：Raw TTS（无风格指令）、Base LLM（未适配 Qwen3.5-9B）、AF-Next（NVIDIA Audio Flamingo Next Captioner）、Qwen3-Omni（Qwen3-Omni-30B-A3B-Instruct）。其中 AF-Next 与 Qwen3-Omni 是可直接访问 ground-truth 目标波形的 privileged captioning 基线。
- 指标：T2S 风格对齐（ParaCLAP-C、ParaCLAP-S、CLSP）、S2S 语音相似度、Emotion Cosine、MCD-DTW。
- 结果：SRSP 在 test in/test out 上相比 Base LLM 和 target-audio-informed captioning 基线取得更高的 speech-style 与 emotion similarity，并降低 MCD；LLM-based expressive speech evaluation 在 contextual appropriateness 与 reference consistency 上也优于所有基线。Table 2 中 SRSP 的 S2S、Emotion Cosine 和 MCD-DTW 表现突出，例如 MCD-DTW 为 5.9569/6.1637，优于 Raw TTS 的 6.2426/6.3932、Base LLM 的 6.3395/6.5072 和 Qwen3-Omni 的 6.1593/6.3189；Emotion Cos. 为 0.6417/0.6269，为最高。配对 Wilcoxon 检验加 Holm 校正显示，40 个下游声学比较中 38 个显著（pHolm < 0.05），例外为 test out 上情感相似度相对 Raw TTS 与 Qwen3-Omni。
- 值得注意：SRSP 的 T2S 分数并非最高，说明它优化的是下游合成行为，而不是与语音 caption 的描述对齐。

## 一句话评价
SRSP 用冻结 TTS 的目标语音似然作为奖励，并借助 GRPO 让文本风格规划器直接面向下游合成效果优化，摆脱了语音 caption 伪标签带来的描述对齐陷阱，在对话 TTS 风格控制上取得一致增益。

---

## 13. Edit Who Speaks, Control How They Speak: Global Timbre Editing and Local Instruction Control for TTS

**作者**: Junchuan Zhao, Chenglin Xu, Wei Zeng, Haoyang Li, Yiwen Guo, Ye Wang
**链接**: [2610.11437](https://arxiv.org/abs/2610.11437)
**分类**: Text-to-Speech (Instruction-based TTS & Voice Editing) | **关键词**: EDICT, Global Timbre Editing, Local Instruction Control, KV Cache Reconstruction, Instruction-based TTS, Voice Editing, Codec Token, TimbreEdit-Bench, IntraTTS-Bench

### 核心痛点
- 指令式 TTS 可通过声音克隆或文本声音设计控制音色与表达，但缺少直接修改给定参考音色并用于新文本合成的接口。
- 现有系统多使用 utterance 级单一提示，少数支持分段指令；TED-TTS 的分段 mask 机制不刷新声学历史，缓存 KV 状态会把前段条件带入后段，产生 control leakage。完全保留历史会削弱新指令，完全丢弃历史则破坏自然延续。
- 参考音色编辑与 TTS 的整合不足，且目标音色匹配不能证明未指定属性被保留。

### 方法创新
- 提出 EDICT，用编辑后的 codec 参考作为全局共享声音锚，统一全局音色编辑与局部表达控制。
- 全局编辑：可训练 timbre editor 以参考 codec c_ref、编辑请求 I_edit 和编辑参考文本 x_edit 为条件，生成 c'_ref。九类属性包括 perceived gender、age impression、pitch register、brightness、vocal weight、resonance focus、roughness、breathiness、nasality；性别和年龄为类别属性，其余为三级有序属性。LLM 把描述映射为属性操作，未提及属性用 <keep> 保持。
- 局部控制：冻结 TTS backbone 以 c'_ref 和 N 个文本-指令对 (x_k, I_k) 生成连续分段，局部指令只改变表达。
- KV cache 重建：每个非最终 <EOS> 触发 fresh prefill，包含下一条指令与文本、共享编辑参考，以及首 S 个和最近 K 个已生成位置的声学上下文；在段边界保留有界声学上下文并刷新条件，缓解 control leakage，同时维持说话人身份与自然过渡。
- 训练：editor 从 Qwen3-TTS-Base 初始化，先 SFT 预测目标 codec，再用 reward-weighted DPO (wDPO) 与辅助 SFT 优化；配对监督由 Qwen3-14B 描述源/目标 profile，Qwen3-TTS-VD 合成中英文语音，覆盖单属性与组合编辑、同文本/不同文本、同语言/跨语言。

### 实验结果
- 提出 TimbreEdit-Bench 与 IntraTTS-Bench，分别评估请求的音色编辑与未指定属性保留，以及局部指令遵循、说话人一致性和自然过渡。
- 在 Qwen3-TTS-VoiceDesign (Qwen3-TTS-VD) 和 CosyVoice 2 上评估 KV cache 重建跨 backbone 及与音色编辑的组合。
- 结果表明，相比各自 baseline，在音色编辑与 utterance 内控制上提升指令遵循，并在局部指令遵循、说话人一致性、过渡质量之间取得更好平衡；评估包含 objective metrics、listening tests 和 ablations。

### 一句话评价
EDICT 将参考音色的全局编辑与逐段局部表达控制解耦又串联，用编辑后 codec 参考作为身份锚、用段边界 KV cache 重建缓解 control leakage，是指令式 TTS 中兼顾音色一致性和时间变化表达的有前景框架。

### 其他关键信息
- 论文标题：Edit Who Speaks, Control How They Speak: Global Timbre Editing and Local Instruction Control for TTS。
- 论文为 Preprint，arXiv:2610.11437v1 [cs.SD] 8 Oct 2026。
- 作者：Junchuan Zhao, Chenglin Xu, Wei Zeng, Haoyang Li, Yiwen Guo, Ye Wang；单位：NUS, LIGHTSPEED, NTU, Independent Researcher。
- 主要贡献：参考条件音色编辑；通过 KV cache 重建实现段级控制；双语 benchmark 与组合评估。
- 注意：片段在训练细节处截断，缺少完整实验结果数值和消融细节。

---

## 14. MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness

**作者**: Jinbo Hu, Hang Su, Lichun Fan, Heinrich Dinkel, Gang Li, Zhanchen Dai, Yiru Zhang, Chang Liu, Peng Wang, Junnan Wu, Jian Luan, Cong Zou, Heng Qu
**链接**: [2610.11156](https://arxiv.org/abs/2610.11156)
**分类**: Audio-Language Models / Spatial Audio Understanding | **关键词**: Large Audio-Language Models, Spatial Audio Understanding, Sound Event Localization and Detection, Hierarchical Semantic-to-Spatial Conditioning, Data Synthesis, Direction of Arrival

## 核心痛点
- 现有大型音频语言模型（LALMs）在通用音频理解上表现强，但大多面向单声道输入，处理多声道时通常直接合并通道（如平均），丢弃了空间感知所需的通道间线索。
- 现有空间音频语言模型多为空间任务专用，架构与数据管线都围绕空间任务设计，无法充分利用单声道 LALMs 已具备的通用音频理解能力；且常用预定义闭集标签，难以用开放式自然语言描述复杂声学场景。
- 传统 SELD 系统虽能联合识别声音事件并估计时间边界与三维位置，但受限于预定义事件类别和结构化输出，难以描述未见事件、复杂空间关系与声源运动。
- 大规模带丰富语言标注的空间音频数据稀缺，空间音频数据规模远小于单声道音频数据，统一“通用音频理解 + 空间感知”仍是一个开放问题。

## 方法创新
- 提出 MiDashengLM-Spatial：据称是首个开源端到端统一音频语言模型，在单一架构内同时支持通用音频理解与空间感知。
- 在 MiDashengLM 基础上扩展空间音频编码器 Spatial-Dasheng，形成双分支音频编码器，并通过分层语义到空间条件化模块（HSSC）融合。
- Spatial-Dasheng 是 Dasheng 的空间变体，用于捕捉空间线索，估计重叠声源的方向到达（DOA）、距离与运动。
- HSSC 将语义分支的中间层语义嵌入分层传递到空间分支的对应层，使空间建模在多个网络深度利用语义上下文，同时保留原始语义路径，维持语义与空间分支的功能分离。
- 构建可扩展数据合成管线：第一阶段利用镜像源法为数千随机采样房间预计算大规模 RIR 数据库，生成沿多样线性与圆形轨迹的 RIR；第二阶段将音频/音乐描述和语音转写等干音频片段以随机起始时间排布在时间线上，静态源用对应 RIR 卷积，运动源用沿轨迹的时变卷积渲染。由于参数化模拟，可获得完整的场景元数据，包括声源与接收器位置、事件时间戳、房间尺寸和混响时间，从而支持方位角、仰角和距离的帧级标注。
- 场景级空间描述与问答生成：先将数值空间信息转为语言描述符，如静态位置量化为 “above”“front-right” 等方向表达，运动声源描述运动方向及起止位置；再用 LLM（Gemma-4-31B）结合真值空间元数据和事件原始音频描述/语音转写，合成整个场景的连贯叙述。根据源语料采用两类形式：通用音频场景的空间音频描述（spatial audio captioning）和语音场景的空间语音转写（spatial speech transcription），后者保留说话内容并用空间 grounded 表达指代说话人。问答方面，摘要提到不是让 LLM 生成问题再做事后验证，而是确定性地构造多项选择空间问答。
- 主要贡献：1）提出可帧级检测与定位重叠声源的空间音频编码器 Spatial-Dasheng；2）提出首个开源端到端统一模型 MiDashengLM-Spatial 及 HSSC 融合机制；3）提出可扩展数据合成管线，构造包含环境声、语音、音乐的大规模多声道场景及空间描述与问答；4）实验验证空间音频理解与推理性能提升，同时保持通用音频理解竞争力，并展示 Spatial-Dasheng 的鲁棒空间感知与 sim-to-real 泛化。

## 实验结果
- 在公开真实场景 SELD 数据集（Shimada et al., 2023；Guo et al., 2026）上评估 Spatial-Dasheng，结果显示其在真实世界声学场景中取得强性能。
- 在包含专门空间理解与推理子集的音频基准（Kumar et al., 2026；Liu et al., 2026）上评估 MiDashengLM-Spatial，结果表明其在空间音频理解与推理基准上显著优于现有 LALMs。
- 同时在多样单声道基准上，MiDashengLM-Spatial 与最先进的 8B 规模 LALMs 保持竞争力，说明可以在不牺牲通用音频理解能力的前提下获得空间感知能力。
- 论文还强调 Spatial-Dasheng 具备鲁棒空间感知和 sim-to-real 泛化能力。

## 一句话评价
- 该工作通过双分支编码器与分层语义到空间条件化机制，在保留单声道通用音频理解能力的同时注入空间感知，并用可扩展合成数据解决空间音频语言监督稀缺问题，是统一通用音频理解与空间感知的一次有代表性的尝试；不过当前片段未展开具体数值结果与消融细节，实际增益仍需结合全文实验判断。

---

## 15. Cross-Lingual Speaker Verification with Self-Supervised Pre-Trained Models

**作者**: Jinghan Peng, Yu Zheng, Weiqiang Wang, Jian Liu
**链接**: [2610.11099](https://arxiv.org/abs/2610.11099)
**分类**: Speaker Verification | **关键词**: speaker verification, cross-lingual, self-supervised learning, pre-trained models, w2v-BERT 2.0, TidyVoice2026

## 核心痛点
跨语言说话人验证（SV）中，说话人身份特征与语言特定声学线索相互纠缠，导致注册与验证语言不匹配时识别准确率显著下降。因此，核心挑战是提取**语言无关的说话人表示**，既能保留说话人生理与行为特质，又对语言内容不变。论文基于TidyVoice2026基准，系统研究利用自监督预训练模型提升跨语言鲁棒性。

## 方法创新
- 以**w2v-BERT 2.0**作为前端特征提取器，利用其从海量多语言无标注语音中学到的丰富声学、语音乃至语义表示。
- 提取SSL模型**所有层的隐藏表示**，每层通过Adapter（两层MLP）投影到统一的256维空间。
- 提出/比较六种**多尺度特征聚合**机制：Mean Fusion、Layer-wise Weighted Fusion、Channel-wise Weighted Fusion、Channel Concatenation、Temporal Concatenation，以及Hierarchical Cross-Attention Fusion（以最后一层为query，与前面所有层的key/value做交叉注意力，再经self-attention融合）。
- 聚合后的帧级特征经**Attentive Statistics Pooling**得到句子级表示，再通过Embedding Projection Layer输出256维说话人嵌入，使用**AAM-Softmax**损失训练。
- 采用**三阶段训练范式**：第一阶段冻结SSL主干、仅训练下游模块；第二阶段解冻主干联合微调；第三阶段仅在TidyVoiceX Train上进行大间隔微调（LM-FT）。
- 同时使用轻量**ReDimNet-B5/B6**（192维嵌入，SphereFace2-C损失）作为辅助系统，用于对比和分数级融合。
- 训练数据覆盖TidyVoiceX Train、VoxCeleb2、VoxBlink2、CN-Celeb 1&2、WenetSpeech清理子集、3D-Speaker等多语言语料，并采用混响、音乐、噪声、babble在线数据增强。

## 实验结果
- 评估指标为EER和minDCF（P_target=0.01, C_FA=C_Miss=1），在TidyVoiceX Dev、tv26 eval-A、tv26 eval-U上评测。
- 基于w2v-BERT 2.0 + AAM损失的SV系统取得：Dev 1.03%、eval-A 3.34%、eval-U 4.59%。
- 最终提交系统（team T02）在**tv26 eval-A上EER 2.21%**，在**tv26 eval-U上EER 2.99%**，在语言不匹配场景下验证了方法的有效性。
- 论文还分析了预训练模型选择、特征聚合方式和训练策略等关键设计要素，为实际应用提供指导。

## 一句话评价
该工作系统性地将大规模自监督预训练模型、多尺度层间特征聚合和三阶段训练策略结合，显著提升了跨语言说话人验证的鲁棒性，在TidyVoice2026基准上取得了有竞争力的结果。

---

## 16. Disentangling Linguistic and Paralinguistic Information with Routed Sparse Autoencoders

**作者**: Beimnet Bekele Guta, Xiaoyu Yang, Guangzhi Sun, Philip C. Woodland
**链接**: [2610.10865](https://arxiv.org/abs/2610.10865)
**分类**: Speech Representation Learning | **关键词**: Sparse Autoencoders, Speech Representation Disentanglement, Self-Supervised Speech Encoders, Paralinguistic Information, TopK SAE, Adversarial Training

# Disentangling Linguistic and Paralinguistic Information with Routed Sparse Autoencoders

**作者**: Beimnet Bekele Guta, Xiaoyu Yang, Guangzhi Sun, Philip C. Woodland（剑桥大学工程系）

## 核心痛点
- 自监督（SSL）语音编码器把**语言信息**（音素、文本内容）与**副语言信息**（说话人身份、情感、韵律）纠缠在同一共享表示空间中：同一激活可能同时携带音素内容、说话人身份、韵律等多种属性，导致对单一属性的选择性解释、移除或修改非常困难。
- 已有解耦路线（基于扰动的不变性、信息瓶颈、结构机制、对抗训练）各有局限。稀疏自编码器（SAE）提供了互补思路：把稠密表示映射为更宽的稀疏码，再由少量激活单元重构原表示；但**稀疏本身并不保证学到的单元对应预先指定的因子**——SAE 字典依赖模型宽度与训练选择，重构目标也不必然恢复规范或预定义的因子分解。
- 现有语音/音频 SAE 工作主要是"分析已发现的特征"，而非在显式解耦目标下把稀疏码**路由**到任务特定子空间，这正是本文要填补的空白。

## 方法创新
- **整体框架**：冻结的 SSL 语音编码器产出帧级表示 → TopK SAE → 其激活单元被划分为语言路径 z_L 与副语言路径 z_P；SAE、路由掩码与任务头在重构损失与任务监督下联合训练，而编码器始终冻结。
- **TopK 稀疏自编码器**：s_t = W_enc x_t + b_enc，z_t = TopK(s_t; k)，x̂_t = W_dec z_t + b_dec（K > D）。TopK 精确控制激活单元数且不对保留激活做收缩。为防"死单元"，引入 **AuxK**：用非激活单元预测重构残差，促使其重新进入 TopK 选择。
- **任务特定路由**：用互补可学习掩码 m_L + m_P = 1 将单元映射到两条路径，z_L = m_L ⊙ z_t，z_P = m_P ⊙ z_t。给出三种方案：
  1. **Learned routing**：每单元有可训练路由 logit，用直通硬 Gumbel-Softmax 得到分配，附加路由熵损失鼓励决定性分配；掩码为跨帧、跨语句共享的全局向量。
  2. **Fixed routing**：预定单元归属，并施加独立预算 k_L + k_P = k，全场训练保持不变。
  3. **Quota-freeze routing**：先学全局分配并用全局 TopK 选 k 个激活；在 freeze 步固化分配，把平均活跃度转成各路 quota，之后在各路内独立做 TopK。
- **任务监督**：语言路径 z_L 由**音素识别（PR）**以 CTC 监督；副语言路径 z_P 由**说话人识别（SID）**、**情感分类**与**韵律预测**（帧级 log-F0 与去均值 log-energy 的 MSE）监督。
- **跨因子对抗**：音素对抗作用于 z_P，说话人/情感/韵律对抗作用于 z_L，均经**梯度反转层** GRL_γ（前向恒等、反向梯度乘 -γ）。
- **总目标**：L_train = λ_recon·L_recon + λ_AuxK·L_AuxK + L_task + L_adv（learned routing 时再加 L_routing）。由于掩码互补，z_t = z_L + z_P，完整稀疏码仍可重构编码器表示。

## 实验设置
- **数据**：LibriSpeech train-clean-100 与 MSP-Podcast；音素标签由 CMU 发音词典 + 字素到音素回退得到，共 74 音素词表。LibriSpeech 上 PR 用 dev-clean 验证、test-clean 评测；闭集 SID 在 train-clean-100 内做语句不重叠划分，251 说话人一致。
- **编码器**：冻结的 SPEAR XLarge 与 WavLM Large，逐层 LayerNorm 后均匀平均；SAE 训练期间上游编码器始终冻结，所有实验共享同一架构/路由/优化设置。
- **配置**：SAE 宽度 K=5120，TopK k=256，AuxK 预算 64、权重 1/32；fixed routing 用 K_L/K_P=4096/1024、激活预算 k_L/k_P=240/16；quota-freeze 在第 4000 步冻结，由 20 个批次的平均活跃度决定冻结后预算。SPEAR 重构-only 与 fixed routing 训 12,000 步，WavLM 同配置 12,000 步（quota-freeze 为 16,000 步）。
- **基线**：Eta-WavLM——从 ECAPA-TDNN 嵌入拟合仿射说话人分量并从 WavLM 表示中减去。
- **评测协议**：所有探针事后训练于冻结表示，参数与 SAE、路由掩码、对抗完全独立（不能仅凭训练期对抗断言信息已被移除）。PR 用 PER，SID 用准确率，情感用 UAR，韵律用 F0 与能量相关性，重构保真用 MSE。
- **跨语料**：LibriSpeech 训练的冻结模型直接在 51,017 条、700 说话人的 MSP-Podcast 子集上评测（训练/验证/测试 41,067/4,975/4,975，闭集 SID 随机基线 0.143%），只训练 MSP 专属的音素与说话人探针。
- **受控干预**：250 个说话人不同、时长差 ≤10% 的受试–供体语句对；供体路径按归一化时间线性插值对齐帧数。P-route swap 把受试 z_L 与重采样供体 z_P 组合，L-route swap 反之；重组码经冻结 SAE 解码器得到重构特征，再由仅在未交换不重叠重构上训练的独立音素/说话人评测器评估。

## 实验结果
- **重构-only SAE** 同时保留语言与副语言信息，说明**稀疏本身不会产生所选的因子分解**。
- 在 SPEAR 与 WavLM 下，**音素信息在 z_L 更强，说话人信息在 z_P 更强**；MSP-Podcast 上呈现相同路由组织，情感与韵律也更多可从 z_P 恢复。
- 典型数值：SPEAR Fixed 路由 z_L 的 PER 10.02、SID 6.2，z_P 的 PER 99.60、SID 99.8；SPEAR Quota-freeze z_L PER 8.94、SID 0.6，z_P PER 80.26、SID 99.8；WavLM Quota-freeze z_L PER 9.40、SID 14.8，z_P PER 80.84、SID 99.8。
- **两种路由的取舍**：fixed routing 对 z_L 的副语言抑制更强；quota-freeze 对 z_P 的语言抑制更强，并在重构与路由选择性之间更平衡。
- **跨语料迁移**：LibriSpeech 上学到的路由组织在 MSP-Podcast 上可保持，无需表示侧重训。
- **干预实验**：特征空间的路由交换能把被交换因子迁移过来，同时大体保留未变路径所携带的信息。
- **基线对比**：Eta-WavLM 基本保留音素性能，但因子特定抑制明显弱于路由表示。
- **总体结论**：跨编码器、语料、独立探针与表示级干预，均呈现一致的路径选择性分离（route-selective separation）。

## 一句话评价
该文把 TopK SAE 从"事后特征发现"推进为"显式解耦目标下的可控路由"，通过单元级路由 + 路径特定任务监督 + 跨因子对抗，在冻结 SSL 语音编码器上实现了可跨语料迁移、可特征级干预的语言/副语言信息分离。

---

## 17. Controlled Acquisition and Abstention in Three-Channel Score Conflicts

**作者**: Mengzhe Geng
**链接**: [2610.10808](https://arxiv.org/abs/2610.10808)
**分类**: Multimodal Learning / Active Acquisition and Abstention | **关键词**: Multimodal conflicts, Active acquisition, Abstention, Selective prediction, Controlled benchmark, Three-channel score conflicts

## 核心痛点
- 当音频、视频和文本三种模态的分数发生冲突时，仅看最终准确率无法回答两个关键操作决策：是否值得再获取第三个来源，以及当前观测是否不足以安全回答而应弃权。
- 传统融合模型总是输出标签，隐藏了获取与拒识决策；高聚合准确率也不能说明缺失观测的价值，或冲突是否能仅由观测识别。
- 请求新来源与弃权都有成本，且奖励约定敏感：论文将弃权设为仅对 designated ambiguity 机制正确，而在 mixed corruption 下弃权受罚，因此结果衡量的是对奖励偏好的适应，而非通用不可识别性检测。

## 方法创新
- 提出受控三分数冲突协议：每个样本有潜在二值事件 y 和三维 signed scores x=(x_a,x_v,x_t)，策略先观察两个分数，可付费请求第三个，也可最终回答或弃权；请求决策与最终动作分离。
- 生成器包含 clean、invert、swap、dropout、mixed、burst、ambiguity 等机制；训练/seen split 含 clean、invert、swap、dropout，部分留出 split 引入 mixed、burst、ambiguity。
- 定义机制条件化效用：u(a,q)=2*1[a=y*]-1 - λq q - λa 1[a=2,z≠ambiguity]，其中 ambiguity 的 target 为 y*=2，否则 y*=y；λq=0.10，λa=0.20。报告 targeted decision accuracy、coverage、selective accuracy、query rate、abstention rate 和 mean utility。
- 固定 THRESHOLD 规则：观察 audio 和 video，若符号不一致或任一绝对值低于 0.35，则请求 text；无请求时用两个强且一致的分数回答；请求后仅当至少两个分数绝对值不小于 0.35 且同号才回答，否则弃权；该规则只使用 x，不看 ambiguity 指示 z 或真实标签。
- 学习式 LEARNED ACQUISITION：将前两个分数及其幅度输入 4→24→12→1 ReLU 网络，二值目标为请求是否能在训练效用上带来改进；属于特权离线监督，但 scorer 拟合与推理时只接收初始观测，阈值在独立 train-only 校准集上按效用选择。
- 匹配协议控制与匹配预算测试：比较 train-only value selector、pair uncertainty、matched random 和不可部署 oracle；并用 equal-information temporal controls、actor-disjoint media studies 分离 full-modality accuracy 与 pre-request selection value。
- 全信息参考基线包括 MAJORITY、MEDIAN、WEIGHTED、MLP、GATED；它们一开始就接收三个分数并总是回答，不请求来源，因此不是匹配的获取基线。

## 实验结果
- 在部分留出的合成 split、83 个独立种子上，THRESHOLD 达到 0.789 +/- 0.006 的 targeted decision accuracy 和 0.481 +/- 0.014 的 utility；三分数 MAJORITY 参考为 0.626 +/- 0.008 和 0.252 +/- 0.016，但使用了更多信息。
- 匹配预算测试中，train-only value selector 在 10% 和 25% 预算下比 no-query 和 matched-random 策略有更高 utility；但 pair uncertainty 在每个预算下 utility 都更高。
- 在 50% 和 63.7% 预算下，selector 虽然非歧义准确率略高，却降低了 utility，说明学习式选择价值依赖预算，且可能因观测对排序而失效。
- 若把所有弃权都计为错误，MAJORITY 在 utility 上超过 THRESHOLD，表明评价约定会改变方法排序。
- 在 central temporal setting，full-trace controls 能与神经模型匹配，而位置扰动可将二者区分。
- 在 held-out-actor 情感片段上，八帧融合对两个 encoder pair 的准确率差异符号相反，两个 actor intervals 均包含零；matched-request routing 增益很小且不确定。
- 总体而言，实验把 full-modality accuracy 与 pre-request selection value 分开，并显示选择价值取决于预算和当前观测对的排序。

## 一句话评价
该工作通过受控三分数冲突基准表明，多模态获取与弃权决策的收益高度依赖奖励约定、预算与观测对排序，因此它更像是一种可控的决策诊断工具，而非通用优越的主动获取策略。

---


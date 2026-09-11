# Arxiv Daily Deep Report - 2026-09-11

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 14
---

## 1. RetroThinker: Enabling Retrospective Thinking in Speech LLMs

**作者**: Yi-Jen Shih, Puyuan Peng, Abdelrahman Mohamed, David Harwath
**链接**: [2609.11864](https://arxiv.org/abs/2609.11864)
**分类**: Speech LLMs Reasoning | **关键词**: Retrospective Thinking, Speech LLMs, Moshi, Chain-of-Thought, Early Reasoning, Direct Preference Optimization, Streaming Speech, GSM8K

# RetroThinker: Enabling Retrospective Thinking in Speech LLMs

**作者与机构**：Yi-Jen Shih、Puyuan Peng、Abdelrahman Mohamed、David Harwath（UT Austin；FAIR, Meta Superintelligence Labs）

## 核心痛点
- SpeechLLMs 相比级联 ASR+文本 LLM+TTS 具有更低延迟、更好保留副语言信息等优势，但在复杂推理任务上仍落后于同规模文本 LLM。
- 实时语音交互对延迟要求极严。CoT 能提升推理准确率，却显著增加延迟；Early Reasoning 与并发推理可降低延迟，但准确率-延迟帕累托权衡依然存在。
- 既有回溯采样方法 REVERSE 依赖 rollback/回滚，不适合流式语音场景，因为中断或回滚会破坏用户体验。

## 方法创新
- 提出 RetroThinker：面向流式 SpeechLLM 的“回溯式思考”后训练框架，使模型在推理过程中自我验证并前向纠正 CoT 步骤，无需回滚已生成的语音。
- 基于 Moshi 多流全双工 SpeechLLM：在 System Text（inner monologue）流中注入/修正 CoT，同时保持 User Audio 与 System Audio 流完整，兼容 Standard Reasoning 与 Early Reasoning，也可与并发推理方法结合。
- 三阶段后训练配方：
  1. **Rule-based Retrospective Training**：将 GSM8K 标准 rationale 切分为有序 CoT 步骤，用规则扰动（改数值/换运算符）合成错误步骤；训练序列包含错误步骤、负向自验证标记 [✘]、纠正步骤、正向标记 [✔]；SFT 时对合成错误 CoT token 做 loss masking，但对验证标记和纠正续写保留 loss。
  2. **Sample-based Distribution Alignment**：用 Stage 1 模型生成推理轨迹，以 LLM-as-a-judge 逐步判断；若判错，则由 judge 给出从该步到最终答案的纠正续写。用模型真实错误作为 masked negative step，用 judge 纠正作为 positive correction，缩小规则错误与真实失败分布之间的差距。
  3. **Length-based DPO Fine-tuning**：用 LengthDPO 压缩推理轨迹，偏好“正确且简洁”的样本，抑制“错误”样本，降低延迟；同时缓解 Early Reasoning 下用户问题不完整带来的分布不匹配，使回溯能力适应不完整查询。
- 推理策略：区别于 REVERSE 的 rollback，采用 forward-only self-correction——模型继续生成后续 CoT 步骤和最终回答，不中断语音输出。

## 实验结果
- 在 TTS-spoken GSM8K 上评估。
- RetroThinker 显著改善准确率-延迟权衡，在可比延迟下比非回溯 baseline 取得 11 个百分点绝对准确率提升。
- 将 Early Reasoning、Retrospective Thinking 与 DPO 结合可进一步推动准确率-延迟帕累托前沿；论文还分析了三者之间的相互影响。

## 一句话评价
RetroThinker 把“回溯式思考”引入流式 SpeechLLM，在 Moshi 上通过三段式后训练实现不中断语音输出的前向自纠错，在 TTS-spoken GSM8K 上同延迟下取得 11 个百分点准确率提升，是推动语音大模型实时推理精度-延迟帕累托前沿的实用探索。

---

## 2. Whisper-Based Speech Transcription from Videos Across Multiple Languages for Cross-Cultural Understanding

**作者**: Michael Picheny
**链接**: [2609.11772](https://arxiv.org/abs/2609.11772)
**分类**: Speech Recognition | **关键词**: Whisper, WhisperX, Multilingual Speech Recognition, Video Transcription, Cross-Cultural Understanding, Fine-tuning

# 论文总结

## 1. 核心痛点
- 跨文化理解在全球化互联环境中日益重要，LLM 技术推动自动化辅助工具发展，而这类工具常依赖多模态的文本、音频和视频数据。
- 将音频转写为文本是重要预处理步骤，但公开 ASR 排行榜上的低词错误率通常来自提示化、风格化、专业说话人和相对干净环境，不能代表 in-the-wild 自然语音。
- 跨文化理解更关注自然口语，非英语/低资源语言仍困难；自建系统需要数千小时数据，非语音专家难以承担；文化标记稀疏，必须处理大量音频，时间与成本关键。
- DARPA CCU 等场景没有人工转写，无法直接评估 ASR 性能。

## 2. 方法与创新
- 使用 Whisper 与 WhisperX，因其易用 API、多语言零样本性能和微调能力；WhisperX 还集成 Pyannote 说话人日志与加速版 Whisper，large-v2 比 Whisper 快约 10x，适合批量处理长视频。
- 选择 7 种语言：西班牙语、日语、韩语、普通话、土耳其语、俄语、希伯来语；前 6 种来自 CCU，Whisper 训练数据均超过 4000 小时，希伯来语仅 688 小时作为挑战语言。
- 从 YouTube 采集视频：用 yt-dlp 和 Jtubespeech 工具，筛选有字幕和 Creative Commons 许可的视频；对字幕/视频不足的语言从头爬取；限制时间范围；使用 Wikimedia 索引生成搜索词，并进行语言相关过滤。
- 处理流程：检查字幕为人工或自动；下载视频并提取 16kHz 单声道音频；处理 VTT 字幕，合并连续片段至 20 秒或 0.1 秒静音；用 WhisperX 语言相关音素对齐模型获得更准词边界；再按 >=0.5 秒静音重新分段；用 WhisperX large-v2 转写，SCTK 评分。
- 进行零样本和微调实验，并发布语音与元数据供社区复现和改进。

## 3. 实验结果
- 在七种语言上，WhisperX 零样本平均转录错误率约 30%；加入少量微调数据后，平均错误率可降至约 20%，显著提升下游可用性。
- 论文指出 Whisper 训练数据共 68 万小时，其中 56.3 万小时英语，11.7 万小时覆盖 96 种其他语言；13 种语言至少有 2000 小时；所选语言训练小时数：普通话 23446、西班牙语 11000、俄语 9761、日语 7064、韩语 7793、土耳其语 4333、希伯来语 688。
- 数据表给出 All 与 Small 数据集的 Train/Dev/Test 视频数、片段数和时长，用于多语言转写实验和微调。
- 局限：零样本错误率仍偏高；VTT 时间边界不精确；large-v3 在噪声数据上可能更易幻觉；非英语和数据稀缺语言仍是难点。

## 4. 一句话评价
这是一篇面向跨文化理解的多语言视频语音转写实践与数据资源论文，验证了 WhisperX 零样本与少量微调在多语言 in-the-wild 视频上的可用性，并提供了可复现的低成本流程，但 20% 左右平均错误率仍说明完全自动化转写远未理想。

---

## 3. Not All Attacks Are Learned Equally in Speech Deepfake Detection

**作者**: Avantika Singh, Aurosweta Mahapatra, Ismail Rasim Ulgen, Nicholas Andrews, Kong Aik Lee, Berrak Sisman
**链接**: [2609.11763](https://arxiv.org/abs/2609.11763)
**分类**: Speech Deepfake Detection | **关键词**: Speech Deepfake Detection, High-impact Attacks, Curriculum Learning, Attack-level Bias, Voice Conversion, Text-to-Speech

## 核心痛点

语音深度伪造检测（SDD）模型通常在多攻击数据集上以二分类（真实/伪造）目标联合训练，所有伪造攻击共享一个伪造标签，评估仅报告总体等错误率（EER）。这种聚合视角掩盖了不同攻击对模型学习和泛化的差异化影响：模型可能被某些攻击主导，导致在其他攻击上泛化不佳，而总体 EER 无法揭示攻击级不平衡。现有课程学习、持续学习和主动学习在 SDD 中主要关注分布偏移、合成语音质量或灾难性遗忘，而非攻击级主导问题。

## 方法创新

1. **受控暴露分析**：构建八种训练配置，包括标准多攻击、样本省略（子采样 TTS 以匹配 VC 样本总量）和六种攻击级省略（每次移除两个 TTS 攻击，保留两个 VC 攻击），以隔离 TTS–VC 暴露与攻击组成的影响。
2. **攻击级偏差诊断**：提出结合省略诱导的 EER 敏感性与攻击级训练损失和预测熵的分析框架。高 EER 敏感性、集中熵和低训练损失表明攻击主导优化并强烈塑造决策边界，定义为**高影响攻击**。
3. **重放正则化的攻击感知课程学习**：先学习低影响攻击，再逐步适应高影响攻击，同时通过教师–学生正则化重放保留的低影响样本，防止灾难性遗忘，缓解高影响攻击主导。

## 实验结果

在 ASVspoof 2019 LA 上，使用 RawNet2、AASIST 和 SSL 模型（SLS-XLSR）进行实验。标准多攻击训练下 VC 与 TTS 的 EER 已存在差异，样本平衡后仍不均衡：样本平衡训练下 RawNet2、AASIST 和 SSL 的总体 EER 分别为 5.45%、3.22% 和 0.70%。攻击级省略显示，移除 A1 和 A4 会导致跨模型显著退化：RawNet2 总体 EER 升至 23.98%（TTS 29.63%），AASIST 升至 18.36%（TTS 24.31%），SSL 升至 17.81%（TTS 23.22%），表明 A1 和 A4 为高影响攻击；而移除 A2 或 A3 时性能相对稳定。该现象在三种架构上一致。论文进一步在 ASVspoof 2019、2021、ASVspoof 5 和 Fake-or-Real 上验证所提课程学习策略，报告整体鲁棒性提升且攻击级不平衡降低（片段未展示完整结果）。

## 一句话评价

该工作首次系统刻画 SDD 中的攻击级学习偏差，定义高影响攻击并提出攻击感知课程学习，为更均衡、鲁棒的语音深度伪造检测训练提供了新视角。

---

## 4. Investigating catastrophic forgetting in sound event classification

**作者**: Riccardo Casciotti, Annamaria Mesaros
**链接**: [2609.11447](https://arxiv.org/abs/2609.11447)
**分类**: Sound Event Classification (Audio Tagging) | **关键词**: Sound Event Classification, Continual Learning, Class-Incremental Learning, Catastrophic Forgetting, Audio Tagging

## 核心痛点
- 深度神经网络通常针对单一目标函数训练，难以顺序学习多个任务，因此容易发生灾难性遗忘：学习新信息时会覆盖或丢失旧知识。
- 在声音事件分类/音频标注场景中，输入音频复杂、噪声大，且常为多标签、多事件共现，模型不仅要学习新类别，还要在多个增量阶段保留旧类别的判别性表示，稳定-可塑性权衡更困难。
- 论文聚焦**类增量学习**：模型按任务序列接收数据，每个任务引入一组新类别，评估时需同时测试新类和所有已见类；学习过程不能访问旧任务数据。

## 方法创新
1. **动态分类头扩展**：分类头随新任务逐步扩展输出单元，每个类别对应一个输出节点，保留旧任务输出，从而支持输出空间增长。
2. **知识蒸馏**：基于文献[17]，在训练新任务时保留旧模型作为教师，用软目标约束当前模型在旧类别上的输出，属于功能正则化方法，防止旧类决策边界剧烈漂移。
3. **被动滤波器剪枝启发的核重要性冻结**：基于文献[14]的无数据滤波器重要性估计，按卷积核贡献排序，在后续任务中保护最重要的核，实验冻结比例包括 12.5%、25%、50%、75%、100%。
4. **核级可塑性调制（learning-modulation）**：基于文献[13]的 Hebbian 深度网络思想并改为反向传播可用。训练中记录核权重更新幅度与累计激活，识别 top-k 重要核；新任务中抑制重要核的大幅更新，并提高非重要核的可塑性，将学习引导到对旧任务影响较小的部分。
5. **全冻结微调**：首个任务后冻结所有卷积层及批归一化层，仅训练动态分类头，作为最激进的架构/参数隔离方案。

## 实验结果
- 在 **FSD50K** 和 **AudioSet** 两个大规模音频数据集上评估，采用不同任务配置与类别顺序，并使用标准音频分类指标与持续学习指标。
- 主要发现：灾难性遗忘主要发生在更深的层，尤其是**分类器头**。
- 在域内声音分类问题中，效果最好且最高效的方案是：**全冻结特征提取器 + 微调动态头分类器**。该方案几乎不遗忘，训练稳定性好，并在记忆稳定性与学习可塑性之间取得良好平衡。
- 论文对冻结、正则化、架构扩展和核级可塑性调制策略进行了实验比较，代码已开源以支持复现。

## 一句话评价
该工作系统比较了类增量声音事件分类中的多种抗遗忘策略，指出遗忘集中于深层分类头，并发现“冻结特征提取器+动态头微调”在域内多标签音频标注中兼具低遗忘与高稳定性，为音频持续学习提供了实用基线。

---

## 5. Preference Optimization with LALM Feedback for Continuous Autoregressive Non-Verbal Vocalization Generation

**作者**: Jingbin Hu, Qirui Zhan, Yuang Cao, Ziyu Zhang, Yunxiang Chen, Houdun Liu, Shuo Feng, Bengu Wu, Lei Xie, Liumeng Xue
**链接**: [2609.11260](https://arxiv.org/abs/2609.11260)
**分类**: Text-to-Speech | **关键词**: Non-Verbal Vocalization, Preference Optimization, Continuous Autoregressive Speech Generation, Flow Matching, Large Audio-Language Model, Direct Preference Optimization

## 论文总结

### 核心痛点
- 非语言发声（NVV），如笑声、叹气、呼吸、哭泣等，承载情感、意图和交互信息，对表达性人机交互很重要。
- 可控 NVV 生成仍具挑战：需要准确实现预期发声类型与出现位置，同时保持感知显著性、与周围语音的自然融合以及整体声学质量。
- 多样化、带上下文标注的 NVV 数据稀缺，限制了传统监督微调。
- 将偏好优化用于连续自回归 TTS 存在根本性不匹配：DiTAR、VoxCPM、dots.tts、VoxCPM2 等模型通过扩散或流匹配声学头自回归生成连续 latent patch，而不是具有显式序列对数似然的离散 token，因此标准 DPO 不能直接适用。
- 为 NVV 构建可靠偏好对并不简单，因为候选语音需要从 NVV 正确性、感知有效性、自然度、质量和表达性等维度联合评估。

### 方法创新
- 提出一种基于大音频语言模型（LALM）反馈的偏好优化框架，用于连续自回归语音模型中的可控 NVV 生成。
- 自动化双语 NVV 偏好数据构建流程：
  - 双源提示构建：从 Emilia 数据集采样 2,500 条真实转写并随机插入单个或多个 NVV 标签，形成冲突丰富的控制条件；再用 Gemini 3.1 生成 2,500 条语义对齐提示。二者互补，覆盖挑战性控制场景与真实表达场景。
  - 随机 rollout：对每个提示，基线模型用独立采样的高斯初始化生成 K=10 个候选语音。
  - LALM 评分与配对：采用 Qwen3.5-Omni-Plus 作为自动偏好评判器，按 NVV Accuracy、NVV Perceptual Effect、Overall Naturalness、Overall Quality、Overall Expression 五个维度按 1–5 分评分，并以 0.30A + 0.25P + 0.15N + 0.15Q + 0.15E 聚合。每个提示选最高分为 chosen、最低分为 rejected，形成同提示 chosen–rejected 对。5,000 个提示产生 50,000 个候选语音和 5,000 个偏好对。
- 将偏好优化适配到连续自回归语音生成：把 patch 级流匹配损失聚合为话语级流匹配损失，作为 DPO 的替代偏好信号。
- 两阶段优化策略：
  - 第一阶段 RSFT 冷启动：在 LALM 选出的高分样本上，用标准流匹配目标微调基线模型，获得偏好感知初始化。
  - 第二阶段 Anchored Flow-DPO：在 RSFT 初始化基础上，使用话语级流匹配损失构造相对量 Δθ(X,c)=LFM,θ(X|c)−LFM,ref(X|c)，并优化 LDPO=−logσ(β[Δθ(Xl,c)−Δθ(Xw,c)])，使模型相对参考模型更偏好 chosen 样本。同时保留 chosen 样本的流匹配目标作为 SFT anchor，以直接监督偏好实现，避免仅优化相对排序而忽略 chosen 样本的绝对损失。

### 实验结果
- 在官方 NVVSpeech Challenge Track 2 测试集（1,600 条话语）上评估。
- 方法取得 Final Track2Score 75.80（中文 79.39 / 英文 72.21），比 VoxCPM2 基线 73.96 绝对提升 +1.84。
- 提升主要来自 NVV Accuracy 和 NVV Perceptual Effect，整体质量保持稳定。
- 中英文 Track2Score 均有一致提升。

### 一句话评价
该论文针对连续自回归 TTS 中 NVV 生成缺乏显式序列似然和人工偏好标注的问题，提出 LALM 自动偏好数据构建与 RSFT + Anchored Flow-DPO 两阶段优化框架，在 NVVSpeech Challenge Track 2 上稳定超越 VoxCPM2 基线，是偏好优化在表达性语音生成中的一次有效适配。

---

## 6. AudioICL-Bench: A Benchmark for Large Audio Language Model In-Context Learning

**作者**: Jia-Hung Chen, Yi-Cheng Lin, Kai-Wei Chang, Ke-Han Lu, Hung-Yi Lee
**链接**: [2609.11252](https://arxiv.org/abs/2609.11252)
**分类**: Audio In-Context Learning | **关键词**: In-Context Learning, Large Audio Language Model, Audio Benchmark, Task Learning, Diagnostic Benchmark

## 核心痛点
现有音频 In-Context Learning (ICL) 研究主要衡量 **Task Recognition**：演示仅提示模型调用预训练已有能力，而非 **Task Learning**（从演示中推断真正新的输入-标签映射）。音频信号缺乏显式单元边界、信息模式跨多个时间尺度，使得音频 Task Learning 比文本更具挑战。目前尚无专门隔离音频 Task Learning 的基准。

## 方法创新
提出 **AudioICL-Bench**，一个诊断性基准，每个 episode 的规则独立重采样，使正确答案无法从预训练先验中获得，只能从演示中归纳。
- 共 9 个任务，沿两个正交轴组织：
  - **Axis-C（上下文操作轴）**：C1 快速绑定、C2 归纳、C3 结构化组合。
  - **Axis-A（音频能力轴）**：A1 语音内容理解、A2 非语音声学模式理解、A3 时间结构。
- 设计原则：抗零样本（无演示时性能接近随机）；主要使用人工任务以独立控制变量，辅以一个自然任务。
- 任务包括 AudioCount、AudioCountHard、AudioLength、AudioLengthHard、AudioOperator、AudioOperatorHard、AudioRemap、MorseCode、AnomalyDetect。
- 每个任务 300 个 episode，使用精确匹配准确率评估。

## 实验结果
在 5 个 Large Audio Language Models (LALMs) 上评估：
- 当感知任务较简单时，最强模型能轻松将任意声音绑定到新标签。
- 但在 **时间测量**（如 AudioLength 系列、MorseCode）和 **多规则组合**（如 AudioOperatorHard）上严重失败。
- 揭示两个主要能力边界：**时间感知** 与 **多规则组合**。

## 一句话评价
AudioICL-Bench 是首个专门隔离音频 Task Learning 的诊断基准，通过两轴分类法与每 episode 重采样规则，系统性地揭示了 LALM 在时间感知与多规则组合上的能力边界。

---

## 7. Domain-Incremental Learning for Multi-Channel Replay Speech Detection

**作者**: Michael Neri
**链接**: [2609.11194](https://arxiv.org/abs/2609.11194)
**分类**: Multi-Channel Replay Speech Detection / Speech Anti-Spoofing | **关键词**: Domain-Incremental Learning, Continual Learning, Replay Speech Detection, Multi-Channel Audio, Task-Specific Beamformer, Elastic Weight Consolidation, Gradient Projection Memory, Spatial Audio

# 论文总结：Domain-Incremental Learning for Multi-Channel Replay Speech Detection

## 核心痛点
- 重放攻击是语音控制系统最易实施的威胁之一，其声学线索会被录音环境强烈调制，例如办公室、走廊或车内等不同混响和噪声条件下，检测器性能会显著下降。
- 部署中的检测器需要随着新声学环境不断更新，但联合所有历史数据重新训练不现实；同时，长期保存历史语音受隐私与 GDPR 约束，因为语音属于生物特征数据，涉及数据最小化、存储限制和删除权。
- 现有持续学习工作多为单通道、攻击增量场景，即每次增量引入新的伪造算法而声学条件相对固定；物理访问重放检测的判别线索由环境调制，因此更接近域增量学习：标签空间固定，仅输入分布变化。
- 论文首次将多通道物理访问重放语音检测形式化为声学环境上的域增量学习问题，并建立持续学习基准。

## 方法创新
- 提出 Task-Specific Beamformer (TSB)：一种基于架构的持续学习策略，将 SOTA 多通道重放检测器 M-ALRAD 解耦为环境特定的空间前端和环境无关的分类器。
- TSB 为每个环境实例化一个可学习波束形成头 f_BM^(k)，各头参数为 theta^(k)，并共享一个 CRNN 分类器 g_phi。
- 在适应第 k 个域时，只优化当前头 theta^(k) 和共享分类器 phi，冻结所有先前头。这样在波束形成阶段从结构上防止遗忘，同时共享分类器保持可塑性以继续提升判别能力。
- 推理阶段不需要环境标签：输入由所有已训练头处理，其 logits 在 softmax 前取平均；在中间域，只使用已训练的头参与平均。
- 额外开销为每个域增加一个头，随 K 线性增长；每个波束形成头约 9.4k 参数，在 K=4 时整体约增加 11.3%，相对共享分类器占比较小。
- 对比基线包括 EWC 与 GPM。EWC 为正则化方法，使用 lambda=5000、对角经验 Fisher 和单锚点；GPM 为优化方法，通过 SVD 保留覆盖 0.97 奇异值能量的主方向，并将后续梯度投影到其正交补。
- 不采用基于回放或表示的方法：前者因语音隐私与生物特征数据限制而不可行，后者缺少多通道空间音频领域的大规模预训练或自监督编码器。
- 采用的多通道检测器 M-ALRAD 输入 4 通道、1 秒、16kHz 音频，STFT 使用 1024 点窗和 512 跳步；CNN 预测波束形成权重，CRNN 分类，损失为标签加权 BCE 加正交与稀疏正则。

## 实验与结果
- 构建了首个多通道重放语音检测持续学习基准：在 ReMASC 语料上评估所有 4! = 24 种环境顺序，每种顺序使用 5 个随机种子，共 120 条增量序列。
- 评价指标包括 EER、AE、AIE、FM、BWT 和 IM。其中 AE 关注最终平均错误率，AIE 关注整个增量过程，FM 衡量遗忘，BWT 衡量后向迁移，IM 需要联合训练参考模型；论文片段在 IM 定义处截断。
- 顺序微调遗忘严重，已学环境的错误率上升 18.8 个百分点。
- EWC 可将遗忘减半，但牺牲可塑性；GPM 与朴素微调在统计上不可区分；提出的 TSB 在最终准确率和增量准确率上均有显著提升。
- 进一步发现：序列中最后一个环境影响最终性能最大，环境顺序对结果的影响甚至大于算法选择。

## 一句话评价
论文将多通道重放语音检测从静态跨环境泛化推进到无需回放历史数据的域增量持续学习，提出的 TSB 以每个环境一个轻量波束形成头实现结构抗遗忘，并在全环境顺序基准上揭示了顺序效应与算法选择同样关键。

---

## 8. Exploring Second-Order Pattern Recognition in Speaker Recognition

**作者**: Yanze Xu, Wenwu Wang, Mark D. Plumbley
**链接**: [2609.11182](https://arxiv.org/abs/2609.11182)
**分类**: Speaker Recognition / Explainable AI | **关键词**: Explainable AI, Second-order Pattern Recognition, Speaker Recognition, Hierarchical Clustering, Extrapolation Space, Gradient Cost

# 论文总结：Exploring Second-Order Pattern Recognition in Speaker Recognition

## 核心痛点
- 经典模式识别让神经网络学习人类定义模式，但网络多为黑盒，XAI 虽能解释部分潜在模式，却缺少对潜在模式的定义、发现、语义解释和面向未见数据的自动识别框架。
- 说话人识别中，说话人嵌入对人类不可理解；现有 XAI 多训练下游分类器推断性别、国籍、语音等语义信息，而未直接解码嵌入中的二阶模式。
- 本文因此提出两个问题：现实中是否存在大量待联合发现的二阶模式；以及能否自动识别未见话语展示哪些已知二阶模式。

## 方法创新
1. 定义二阶模式：受认知心理学一阶/二阶信念启发，将 XAI 技术“相信”的、刻画网络如何将输入识别为人类定义模式的潜在模式称为二阶模式。
2. 提出新任务“二阶模式识别”：给定从已知话语中发现的二阶模式，判断未见话语展示了其中哪些模式。
3. 完整系统：SLINK 层次聚类发现二阶模式；HCCM 通过 L-score 将层次表示聚类与预定义语义类一一匹配，实现语义解释；HCNA 负责对未见话语进行二阶模式识别。
4. HCNA 候选路径：对未见话语表示，先找最近已知表示，再沿包含该表示的嵌套聚类路径形成候选二阶模式。
5. 经验空间与外推空间：沿用 McInnes 等人的思路定义 birth distance 和经验空间；HCNA 不直接使用经验空间，而是引入 Gradient Cost 和 Gradient-Cost Ratio 估计外推空间，判断未见表示是否落入其中。
6. Gradient Cost：针对 angular prototypical loss，定义为单位角度差异所需的梯度调整量，并用最近已知表示与未见表示的角度差、梯度范数和表示尺度计算。

## 实验结果
- 论文设计了多项评估指标来评估 SLINK+HCCM+HCNA 组成的二阶模式识别系统。
- 实验结果显示，HCNA 引入的外推机制显著提升了二阶模式识别任务性能。
- 摘录片段未给出具体实验数值、数据集和消融细节，需查看全文获取。

## 相关工作定位
- 说话人嵌入解释：现有研究通过下游分类器将嵌入映射到性别、国籍、语音等语义类，成功分类即认为嵌入编码对应语义；本文则直接用 SLINK 分析二阶模式并用 HCCM 关联语义类。
- 聚类伪标签：类似工作把聚类结果当伪标签并预测未见输入是否属于这些伪标签；本文的二阶模式有明确定义，刻画网络决策，并且可被 HCCM 语义解释。

## 一句话评价
- 该工作从 XAI 与认知心理学交叉视角提出“二阶模式识别”新任务，并用 SLINK+HCCM+HCNA 构建从模式发现、语义解释到未见话语分配的完整框架，为说话人识别网络可解释性提供了新思路。

---

## 9. Low-Latency State Space Voice Activity Detection with Robust Onset Time Evaluation

**作者**: Elad Cohen, Arnon Netzer, Hai Victor Habi
**链接**: [2609.11110](https://arxiv.org/abs/2609.11110)
**分类**: Voice Activity Detection | **关键词**: Voice Activity Detection, Low Latency, State Space Model, S4VAD, Onset Time Evaluation, Annotation Noise, Expectation-Maximization

## 核心痛点
- 现有 VAD 评估常用 AUROC、F1、EER 等分类指标，但这些指标对检测时序不敏感，无法反映低延迟与流式场景中真正重要的 onset 延迟。
- VAD onset 标注本身存在噪声：不同数据集的标注抖动可达数十到数百毫秒，例如 AVA-Speech 为 1 Hz 分辨率，LibriSpeech 依赖强制对齐工具生成边界，TIMIT/Buckeye 上也有数十毫秒偏差。直接以标注 onset 计算延迟会不稳定且可能有偏。
- 说话人分离和声事件检测常用 collar 或容忍窗处理边界不确定性，但这些方法只是启发式容错，会掩盖边界误差，不能显式估计延迟，也无法原则性地处理噪声标注。
- 低延迟 VAD 缺乏标准化 latency 评估，尤其缺少对标注不确定性的鲁棒评估方法。

## 方法创新
- 提出概率化 onset 延迟评估框架：将标注 onset 视为真实 onset 的含噪观测，即 t = t* + δ，其中 δ ~ π(δ) 为标注噪声。
- 使用参考 VAD 输出构造 hazard-style 活动函数 ψ(t;x)，并通过 EM 从数据中估计全局标注噪声分布 π(δ)。
- E-step 计算后验 q_i(δ) ∝ π(δ)ψ(t_i - δ; x_i)；M-step 更新 π(δ) = (1/N) Σ_i q_i(δ)，交替迭代 K 次。
- 用估计得到的噪声均值 μδ 校正 naive onset bias eB，得到 corrected onset bias B = E[bt(x) - t*] = E[ϵ] + E[δ]，最终 onset latency = corrected onset bias B + hardware inference latency。
- 提出 S4VAD：据称是首个基于状态空间模型 SSM/S4 的 VAD 架构。S4VAD 将线性状态空间递归与高效序列建模结合，通过状态矩阵与离散化衰减率控制历史声学证据的衰减速度，从而在长上下文鲁棒性与快速 onset 响应之间做原则性权衡，并支持高效流式推理。
- 对比 CNN、RNN、Transformer 和 SSM 等低延迟 VAD 架构，重点评估时间响应性。

## 实验结果
- 摘要与引言报告 S4VAD 在保持有竞争力 AUROC 的同时取得最低 onset latency。
- 标注噪声分析中，EM 估计的噪声分布与干净子集得到的形状接近；负 δ 值表明标注者存在系统性提前标注偏差，即倾向把 onset 标在真实 onset 之前。结果在 LibriSpeech 和 AVA-Speech 上报告。
- 为减轻参考 VAD 自身偏差，使用 Silero VAD 作为参考。论文片段在实验细节前被截断，因此未给出具体数值表格；完整实验应包含多架构 latency 与 AUROC 对比。

## 一句话评价
- 该工作把 VAD 低延迟评估从直接对标注 onset 计时推进到在标注噪声下用 EM 校正 onset bias，并通过 S4/SSM 架构实现低延迟 VAD，兼具评估鲁棒性与架构创新。

---

## 10. Downstream-Task-Aware Unified Source Separation

**作者**: Yoshiki Mitsui, Ryo Aihara, Tatsuhiko Saito, Yoshiki Masuyama, Christoph Boeddeker, Julius Richter, Gordon Wichern, Jonathan Le Roux
**链接**: [2609.11092](https://arxiv.org/abs/2609.11092)
**分类**: Audio Enhancement | **关键词**: source separation, speech enhancement, prompt extension

## 核心痛点
- **TUSS 忽略下游任务需求**：任务感知统一源分离（TUSS）虽能通过提示词（prompt）让单一模型处理多种分离任务，但未考虑增强后语音是用于人耳聆听还是自动语音识别（ASR）等下游任务。
- **同一输入、不同理想输出**：例如语音增强用于人耳聆听通常追求最小化残留噪声，而用于 ASR 时，单通道增强反而可能比原始含噪输入更差。
- **现有 ASR 导向目标存在局限**：ASR 导向损失常牺牲感知质量，且直接优化特定 ASR 系统会使增强模型绑定后端，并需要可微 ASR 流程，复杂且不灵活。
- **观察加和（Observation Adding, OA）只能在推理时后处理**：无法把下游任务需求融入训练目标。
- **需要统一训练框架**：使单一模型能根据下游任务要求自适应输出不同信号特性。

## 方法创新
- **面向 TUSS 的提示扩展框架**：将下游任务信息加入输入 prompt，并在训练时根据给定 prompt 切换损失函数，使同一模型在推理时可通过选择 prompt 输出不同特性的信号。
- **两类下游任务专用 prompt**：
  - **源条件 prompt（source-conditioned prompts）**：与特定源类型和下游任务绑定的新可学习 prompt token，如 `<Speech-XXXX>`。
  - **仅下游任务 prompt（downstream-task-only prompts）**：仅编码下游任务信息、与源身份无关的额外 token，如 `<ex-XXXX>`；仅用于 cross-prompt 模块 conditioning，不传入 TSE 模块。
- **ASR 前端应用**：提出 ASR 专用 prompt `<Speech-ForASR>` 与 `<ex-ForASR>`，并配对正则化损失。标准 prompt 仍使用传统 SNR 损失。
  - MAP 风格 L1 正则化损失：`L_L1,R(s_n, ŝ_n) = ||s_n - ŝ_n||_1 + λ||y_n - ŝ_n||_1`，其中 `y_n = s_n + 10^{-α/20}(x - s_n)`，实验设 `λ=1`、`α=5.0`。
  - 进一步提出 SNR 版本正则化目标：`L_SNR,R(s_n, ŝ_n) = -SNR(s_n, ŝ_n) - λ·SNR(y_n, ŝ_n)`。
- **联合训练机制**：训练时以一定概率切换 prompt 和对应损失，使单一 TUSS 模型同时支持通用增强与 ASR 导向增强；推理时用户可按需求选择 prompt。
- **混响控制扩展**：引入仅下游任务 prompt `<ex-KeepRev>`，当包含该 prompt 时以带混响语音为目标，否则以去除晚期混响（RIR 前 50 ms）的目标语音为目标，实现保留/去除混响的控制。

## 实验结果
- **数据与任务**：在 LibriSpeech 和 JNAS 语料（摘要）以及 ATRANS-II 噪声数据库（实验部分）上评估 ASR 导向语音增强与混响控制。
- **模型设置**：
  - A1：标准 SNR 损失，prompt 为 `<Speech>`、`<SFX-mix>`。
  - A2：正则化 SNR 损失（式 3），prompt 为 `<Speech-ForASR>`、`<SFX-mix>`。
  - A3/A4：以 50% 概率联合优化两种目标；A3 使用源条件 prompt（`<Speech>` 配 SNR 损失，`<Speech-ForASR>` 配正则化损失），A4 在存在 `<ex-ForASR>` 时用式 3，否则用 SNR 损失。
  - B1–B3：将 SNR 损失替换为 L1 等价版本。
  - A5：联合 ASR 导向增强与混响控制，prompt 包括 `<Speech>`、`<SFX-mix>`、`<ex-ForASR>`、`<ex-KeepRev>`，训练时独立以 50% 概率开关两个下游任务 prompt。
  - 输出后缀：`-H` 表示高质量增强输出，`-A` 表示 ASR 导向输出；`-XD`/`-XR` 表示不含/含 `<ex-KeepRev>`。
- **训练细节**：16 kHz 输入，STFT 窗长 32 ms、帧移 8 ms；采用与 [17] 相同的频带划分；TUSS Medium 配置；`D=64, K=4, S=1, H=4, G=8`；cross-prompt 模块 `(B,E,C)=(4,128,384)`，TSE 模块 `(2,96,256)`；训练 150 epoch，每 epoch 2000 更新步，batch size 4，AdamW，学习率 warm-up 至 0.001（10k steps），验证损失 5 epoch 不改善则学习率减半并回退到当前最佳模型。
- **A5 混响数据**：使用 SLR26 数据库模拟 RIR，训练/验证/测试按 7:2:1 划分；噪声 77 类按 54/16/7 划分，并用 Silero-VAD 去除噪声中的清晰语音片段。
- **主要结论（摘要）**：所提联合训练方案使单一模型在广泛 SNR 条件下，通过选择 ASR 专用 prompt 可相对含噪输入提升 ASR 性能，同时在使用标准 prompt 时保持通用语音增强质量。

## 一句话评价
提出一种简单有效的 prompt 扩展与 prompt-dependent loss 机制，使统一源分离模型能够按下游任务（如 ASR 或人耳聆听）动态切换输出特性，在保持通用增强质量的同时提升 ASR 鲁棒性。

---

## 11. Less can be More: What Aspects of Speech Drive End-of-Turn Detection

**作者**: Rini Sharon, Manickavela A, Kadri Hacioglu, Andreas Stolcke
**链接**: [2609.11066](https://arxiv.org/abs/2609.11066)
**分类**: End-of-Turn Detection | **关键词**: End-of-Turn Detection, Prosody, Multimodal Fusion, Streaming Speech Processing, Conversational AI

## 核心痛点
- 在对话式 AI 中，判断说话人是否说完（End-of-Turn, EOT）对自然轮转至关重要：过早响应会打断用户，过晚等待会造成不自然延迟并降低任务完成率。
- 传统方法依赖静音检测、VAD 或 ASR blank token，需要把静音阈值设得较高，无法区分犹豫、句中规划停顿与真正的话轮结束。
- 近期工作开始引入语义信息，但声学、韵律、语义三类信号在 EOT 中的相对贡献仍不清晰；文本可能带来 ASR 延迟与错误传播，而且说话人可能在语义完整时仍想继续。

## 方法创新
- 提出 APT（Acoustic–Prosodic–Text）三模态流式 EOT 检测器：仅优化约 261K 参数的轻量融合分类头，冻结 Zipformer2 声学编码器（70M，14k 小时对话语音）和 MiniLM 句向量编码器。
- 三路输入统一到 25Hz（40ms/帧）：
  - 声学：80D log-mel filterbank，经冻结 Zipformer2 编码器输出 25Hz 表示。
  - 韵律：5 维手工特征（归一化 F0 中位数、ΔF0、voiced、speech、对数静音累计 dsil），100Hz 提取后聚合到 25Hz。
  - 文本：RNN-T 贪心解码的 running transcript，MiniLM 句向量仅在新词解码时更新并缓存，并用绝对帧位置正弦编码隐式编码距上次解码词的时长。
- 每路独立投影后经过 7 帧（280ms）因果深度可分离时序卷积，拼接为 272D，融合头为 272→128→1，输出每帧 EOT 概率。
- 控制变量消融：禁用某模态时用同维度零向量替换并阻断梯度（register_buffer），保持输入维度、参数量、训练数据与优化设置一致；对 {A,P,T} 的全部 7 个非空子集从头独立训练。
- 补充特征空间分析，独立于分类器量化各模态的类可分性。

## 实验结果
- 在 5,000 条测试话语上，A+P 取得最佳平衡：F1=0.930，FA=7.8%，Miss=5.2%，中位延迟 400ms；优于完整 APT（F1=0.909，FA=10.7%，中位延迟 360ms）及其他组合。
- 单模态：A 的 F1=0.927，中位延迟 440ms；P 的 F1=0.828，延迟 960ms；T 最差，F1=0.292。
- 加入文本（A+T、APT）未提升性能，反而增加过早检测与误报；特征空间分析显示韵律特征类可分性最强，文本表示重叠严重。
- 结论：话轮转换主要由语调和静音模式传达，而非语义完整性；不依赖昂贵文本推理即可实现更快、更可靠的 EOT 系统。

## 一句话评价
该工作通过严格的控制消融证明“少即是多”：在流式 EOT 检测中，声学+韵律已足够甚至更优，文本语义并非必要，为轻量、低延迟对话系统设计提供了有力实证。

---

## 12. Diarization Error Decomposition Under Pause Annotation Ambiguity

**作者**: Shota Horiguchi, Marc Delcroix, Naohiro Tawara, Alexis Plaquet
**链接**: [2609.11007](https://arxiv.org/abs/2609.11007)
**分类**: Speaker Diarization Evaluation | **关键词**: speaker diarization, diarization error rate, pause annotation ambiguity, morphological closing, error decomposition, overlap-aware evaluation, pause-fill attribution

# 论文总结：Diarization Error Decomposition Under Pause Annotation Ambiguity

## 核心痛点
- 说话人日志评估对暂停标注模糊敏感：短停顿标注不一致会抬高 diarization error rate，或掩盖真实模型错误。
- 常用的 collar tolerance 不能消除 pause-annotation 不一致带来的影响。
- 已有 pause-tolerant 评估使用 morphological closing，但论文指出：任何完全 pause-invariant 的指标必然通过 closing 分解，从而丢失 segment-level 区分，无法区分 pause-preserving hypothesis 与其 pause-filled 版本，也无法区分 tight annotation 与 indiscriminate filling。
- forced alignment 方案需要额外繁琐评估流程；word DER 需要 ASR 输出且不是独立 diarization 指标。

## 方法创新
- 提出标准 DER 的精确、overlap-aware 分解：将错误拆成 pause-attributable component 与 residual core component，且不改变原始 DER 值，满足 E = Epause(τ) + Ecore(τ)。
- 对每个映射后的 reference-hypothesis speaker pair，定义 internal hypothesis pause g=(a,b)，若 d=b-a≤τ、reference speaker 在整个 g 内 active、且单个 reference activity interval 跨越 g 的两端边界，则视为 pause-fill compatible；对称地定义 reference pause。
- 用 PM(t;τ) 和 PF(t;τ) 表示 pause-attributable candidates，并定义 Mpause(t;τ)=min(M(t),PM(t;τ))、Fpause(t;τ)=min(F(t),PF(t;τ))；speaker confusion 保持不变。
- 理论性质：
  - Proposition 2：τ 增大时，pause-attributable error 单调非减，core error 单调非增。
  - Proposition 3：对有限个 internal pauses，存在有限 τsat，之后 Epause 和 Ecore 饱和。
- 与 closing 不同，增大 τ 只改变 DER 的分解方式，不会让评估变得更宽松。
- 备注：core error 是诊断性 proxy，不是独立指标；不解决 reference tightness 下的直接可比性；可兼容 collar，并可扩展到 JER 等其他 duration-based metrics。

## 实验结果
- 使用 AMI corpus 的原始 speech activity labels 与合成变换版本进行 controlled synthetic validation。
- 合成变换包括：Fill、Insertion、Shift、Long fill；设置 dmax、baseline closing width 和 τ=1 s。
- 预期语义：Fill 代表 pause-attributable errors；Insertion 产生 isolated activity 而非 bridging pause，代表 core errors；Shift 与 Long fill 也代表 core errors。
- 实验覆盖 synthetic transformations、annotation mismatch、cross-domain evaluation、tight-boundary diarization，表明分解能揭示标准 DER 不明显的错误来源。
- Fig. 1 示例：loose reference 与 tight hypothesis 下，标准 DER 为 35%，closing baseline 会改变 DER，而 proposed method 给出 Core: 10%、Pause: 25%，保持 DER 分解解释性。
- 论文片段中 Table 1 等具体数值被截断，但摘要与引言声称分解后的 pause-attributable 和 core components 随 pause threshold 单调变化并最终饱和。

## 一句话评价
- 该论文在不改变标准 DER 的前提下，将错误精确分解为暂停可归因部分与核心残差部分，提升了说话人日志评估的可解释性，但 core error 仅作为诊断代理且受 reference 标注紧致度影响。

---

## 13. From Metrics to Natural Dialogue: French Full-Duplex Benchmark for Spoken Dialogue Models

**作者**: Hamid Soltani, Gilles Boulianne (Luqia Technologies)
**链接**: [2609.10765](https://arxiv.org/abs/2609.10765)
**分类**: Spoken Dialogue Models | **关键词**: Full-Duplex Spoken Dialogue, French Benchmark, Turn-Taking, Backchanneling, Speech Dialogue Evaluation, CALLFRIEND, MEDIA

# 论文总结：From Metrics to Natural Dialogue: French Full-Duplex Benchmark for Spoken Dialogue Models

## 核心痛点
- 全双工语音对话模型的评估基准主要面向英语，尚不清楚在非目标语言或语言不匹配场景下，Full-Duplex-Bench（FDB）指标是否仍然可靠。
- 法语缺少专门的全双工对话基准；法语包含 euh、ben、ouais、d'accord 等语言特定互动线索，其功能和韵律难以直接映射到英语。
- 部分现有 FDB 任务基于合成语音，可能无法充分反映自然对话的多样性。
- 当前 FDB 指标通过指标优化定义更好表现，但真实对话比固定指标目标更灵活，可能牺牲自然性。

## 方法创新
- 提出两个法语全双工基准变体：CALLFC-FDB（加拿大法语，基于 CALLFRIEND French Canadian 电话对话）和 MEDIA-FDB（欧洲法语，基于 MEDIA 酒店预订/旅游信息领域 Wizard-of-Oz 人机对话）。
- 为兼容 FDB 系列，适配 FDB v1.0 的四个核心任务：Pause Handling、Backchanneling、Smooth Turn Taking、User Interruption。MEDIA-FDB 因缺少足够有效系统 backchannel 样本，未包含 Backchanneling 任务。
- 从连续双通道真实口语对话构建 FDB 兼容样本，保留时序、说话者活动、停顿和 backchannel。
- CALLFC-FDB 转录准备：用 Whisper large-v3 转写各音频通道，用 Montreal Forced Aligner 对齐，再用 LCS 对齐自动与手动转录，恢复重叠区域说话者信息和词级时间；恢复 44,165 个重叠词，约占最终 386K 词转录的 11%。
- MEDIA-FDB 基于已有说话者标注的 MEDIA 转录（片段后续截断）。
- 除引入法语 FDB 外，还用 FDB 指标评估人类-人类对话，建立真实对话中指标取值的参考。

## 实验结果
- 大多数基于时序的指标在不同语言间表现相似或一致。
- 基于内容的评估在语言不匹配时退化，例如用英语回复法语用户中断，即使时序合适，Rating 也可能较低。
- 任务语言依赖性不同：Pause Handling 弱语言依赖；Smooth Turn Taking 依赖时序但更受语言匹配影响；Backchanneling 更依赖语言；User Interruption 最依赖语言。
- 发现优化 FDB 基准指标与保持自然口语互动之间存在权衡。

## 关键指标
- Takeover Rate (TOR)
- Backchannel Frequency
- Jensen-Shannon Divergence (JSD)
- Smooth Turn-Taking Latency
- User Interruption Latency
- Rating（基于 LLM 的用户中断回复质量评分，0-5）

## 一句话评价
该工作将全双工对话评估扩展到法语真实口语场景，并揭示时序指标跨语言较稳健、内容评估对语言匹配敏感，同时指出指标优化与对话自然性之间存在取舍。

---

## 14. Xiaomi-CocktailASR-1 Technical Report

**作者**: Yiru Zhang, Hang Su, Lichun Fan, Ying Zeng, Chang Liu, Yifeng Wang, Yuquan Liang, Tao Li, Lian Li, Wenhao Yang, Jian Luan, Cong Zou, Heng Qu
**链接**: [2609.11274](https://arxiv.org/abs/2609.11274)
**分类**: Speech Recognition (Target-Speaker ASR / Cocktail Party ASR) | **关键词**: Target-Speaker ASR, Cocktail Party Problem, LLM-based ASR, Negative Sample Rejection, Chain-of-Thought, Voiceprint Prompt, Single-Speaker Robustness

## 核心痛点
- 现有 LLM-based ASR 在单说话人场景表现强，但普遍不支持多说话人/鸡尾酒会场景；现有 TS-ASR 方法（端到端说话人嵌入、LLM-based 探索）在单说话人场景性能下降，且无法在目标说话人缺失时拒绝输出。
- 真实交互场景（智能家居、可穿戴、智能会议）需要系统同时兼顾：多说话人干扰抑制、单说话人识别不退化、目标缺失时拒绝转写、以及可解释推理。
- 现有系统难以在统一架构中平衡单说话人 ASR 与多说话人 TS-ASR，且负样本拒绝能力缺失会导致误触发和错误转写。

## 方法创新
- 提出 Xiaomi-CocktailASR-1：基于 LLM 的端到端 TS-ASR 架构，使用参考语音作为声纹提示，直接转写目标说话人语音，无需显式语音分离模块。
- 架构组成：输入为参考语音 + 1 秒静音 + 混合语音；Audio Encoder（0.6B，基于 Data2Vec2，前端加入 FBank 模块以替代原始波形输入，输出 1280 维帧级表征）→ Adapter（轻量线性网络，映射到 LLM 隐空间）→ LLM 主干（Qwen3-8B）。参考语音作为条件提示，使编码器自适应聚焦目标说话人并抑制无关说话人干扰。
- 双模式设计：标准模式下，统一 prompt 同时支持单说话人识别、多说话人目标说话人 ASR 和负样本拒绝；CoT 模式下生成显式中间推理步骤，包括说话人数、性别、与参考语音的声纹相似度，提升可解释性与复杂场景准确率。
- 训练策略：构建多阶段训练管线，覆盖四项核心能力——多说话人识别、单说话人识别、负样本拒绝、CoT 推理。多说话人数据加入环境噪声与语音噪声混合、随机重叠增强；单说话人数据用同一说话人不同话语构造参考-目标对，并优化单/多说话人采样比例以缓解过抑制；负样本通过不匹配参考语音训练，逐步增加比例，使拒绝能力内化到模型权重，无需推理阈值。
- 训练数据：使用开源多说话人数据（AMI、AliMeeting、LibriMix）以及自有单说话人数据模拟生成的 overlapping 多说话人数据。

## 实验结果
- 摘要声称在多种合成与真实多说话人基准上达到 state-of-the-art 性能。
- 在单说话人场景下，性能与主流 ASR 模型相当，无需因说话人数不同而切换模型。
- 具备负样本拒绝能力：当目标说话人不在混合语音中时输出空文本，减少误触发。
- 支持 CoT 推理模式，提供显式推理步骤和可解释性。
- 论文片段未给出具体数值结果、消融实验和详细基准对比表格。

## 一句话评价
- Xiaomi-CocktailASR-1 尝试用统一 LLM 端到端框架整合鸡尾酒会 TS-ASR、单说话人鲁棒性和负样本拒绝能力，是面向真实交互场景的实用型 TS-ASR 系统。

---


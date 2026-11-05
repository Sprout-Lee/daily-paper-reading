# Arxiv Daily Deep Report - 2026-11-05

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 13
---

## 1. The Hearpiece Database of Binaural Room Impulse Responses and Driver Responses on KEMAR

**作者**: Tong Xiao, Reinhild Roden, Matthias Blau, Simon Doclo
**链接**: [2611.06345](https://arxiv.org/abs/2611.06345)
**分类**: Binaural Room Impulse Response Database | **关键词**: Hearpiece, KEMAR, binaural room impulse responses, BRIR, driver responses, hearing-device signal processing, room acoustics, MATLAB database

# 论文总结

## 核心痛点
- 现有 Hearpiece 数据库多为消声室 HRIR/驱动响应，缺少房间相关的双耳房间脉冲响应（BRIR），难以支持混响、空间滤波、去混响、反馈抑制等真实场景研究。
- 已有听戴设备数据库在通道数、房间条件、佩戴重复性、驱动响应等方面覆盖有限：例如部分数据库仅含 In-Ear/Concha 麦克风且无驱动响应；部分聚焦 ANC 路径或外部分布式麦克风；部分聚焦个体 HRTF/HARTF 而非房间相关响应。
- 需要统一测量框架，将 Hearpiece 多麦克风/多驱动响应、KEMAR 双耳/耳鼓位置响应、可控房间条件、不同拟合配置与独立插入重复性整合到同一可复现数据库中。

## 方法/数据库创新
- 在 KEMAR 45BB-12 上双边佩戴 Hearpiece，构建 Hearpiece-KEMAR 房间响应数据库，扩展 Denk 与 Kollmeier 的消声室 Hearpiece 数据库到房间相关 BRIR，并同时提供驱动响应。
- 覆盖两种 Hearpiece 拟合配置：AC0031（闭合 fitting）与 AV0006（通风 fitting）；每种配置 3 次独立插入。
- BRIR 覆盖 3 种房间条件（reverb1、reverb2、reverb3，混响由弱到强）与 24 个水平声源方向（0° 起始、15° 步进、仰角 0°），每个文件包含 10 个记录通道：Hearpiece 麦克风与 KEMAR 耳模拟器/耳鼓位置等。
- 驱动响应覆盖 4 个 Hearpiece 驱动器和 10 个记录通道，仅在 reverb1 测量；另含无 KEMAR 时阵列中心麦克风 RIR（三种房间）和用于补偿的播放-录制环路脉冲响应。
- 所有脉冲响应采样率 48 kHz，提供 MATLAB MAT 文件、Load_Hearpiece_Database.m 加载脚本与 Documentation.pdf，公开 DOI 为 10.5281/zenodo.23667308，采用 CC BY-SA 4.0。
- 测量硬件：24 只 Genelec 8030 扬声器组成半径约 2 m 的水平圆阵，间隔 15°；RME MADIface XT、ADI-8 QS、OctaMic XTC 用于播放与录制；KEMAR 配 G.R.A.S. 43BB-1 低噪声耳模拟器与 KB5000/5001 anthropometric pinnae，使用中等硅胶耳塞。

## 数据库规模与“实验结果”
- BRIR：2 配置 × 3 房间 × 3 插入 = 18 个 BRIR 文件；每文件 24 方向 × 10 通道 = 240 个脉冲响应；总计 18 × 24 × 10 = 4320 个 BRIR 脉冲响应。
- 驱动响应：2 配置 × 3 插入 = 6 个文件；每文件 4 驱动器 × 10 通道 = 40 个响应；总计 6 × 4 × 10 = 240 个驱动响应脉冲响应。
- 另含 3 个房间条件的中心麦克风 RIR（CenterMic_reverb1/2/3.mat）与 1 个 Loopback.mat。
- 提供的数据组织包括 BRIRs_MAT、DriverResponses_MAT、CenterMic_MAT、Calibration_MAT 四个文件夹，以及加载脚本和文档。
- 论文片段未给出下游算法性能对比或定量评测结果；其“结果”主要是数据库组成、测量条件与可复现性描述。摘要指出潜在应用包括语音增强、空间滤波与源分离、去混响、主动噪声与堵塞控制、声反馈消除。

## 一句话评价
该论文发布了一个面向 Hearpiece/KEMAR 的可复现多通道房间响应数据库，将两种拟合配置、三种房间条件、三次插入重复、24 个方向和驱动响应统一起来，为双耳助听设备信号处理研究提供了较完整的数据基础。

---

## 2. Speaker-Consistent Grounding for Confusion-Resilient LLM-Based Target Speech Extraction

**作者**: Hanyu Meng, Hao Shi, Zhanhong He, Qiquan Zhang, Yang Xiao, Sungwoo Cho, Haowei Lou, Haizhou Li
**链接**: [2611.06297](https://arxiv.org/abs/2611.06297)
**分类**: Target Speech Extraction / LLM-based Generative Speech Processing | **关键词**: target speaker extraction, target confusion, speaker-consistent grounding, code-space grounding, LLM-based TSE, training-free evidence repair

## 核心痛点
- 确定性目标说话人提取（TSE）虽然能较好保留观测到的语言内容，但可能错误地提取干扰说话人，即“目标混淆”（target confusion）。这种输出可能清晰可懂，却携带干扰者的身份和内容，因此仅靠感知质量无法保证目标提取可靠。
- 自回归生成式 TSE 可提升感知质量，但容易出现内容幻觉和说话人身份漂移。已有工作尝试用确定性 TSE 输出作为证据进行 grounding，但如果证据本身已经说话人混淆，grounding 反而会强化错误。
- 因此需要同时解决两个互补问题：生成前保证证据身份正确，以缓解目标混淆；生成过程中保持解码一致性，以限制幻觉和内容漂移。

## 方法创新
论文提出 **repair-before-grounding** 框架，包含训练无关的证据修复阶段和生成阶段的 code-space grounding：
1. **Conditioning-diverse candidate selection (CDCS-5)**：利用互补的 enrollment 视图和两条冻结 TSE 路径构造 5 个确定性候选，包括完整 enrollment、enrollment 三个时间段中最大能量窗口，以及基于 mixture-aligned enrollment TF map 与帧级 ECAPA 特征的 TF-context 路径。随后用冻结 ECAPA-TDNN 说话人编码器计算候选与目标 enrollment 的余弦相似度，选择最一致的候选作为修复证据。
2. **Code-space grounding (CSG)**：将选中的波形用 CosyVoice3 的 25-Hz S3 tokenizer 转为证据 token 序列，在冻结的 Qwen-TSE 解码过程中约束 token 选择。固定 CSG 使用 λ=1、w=0；自适应 CSG 根据 mixture 在证据上的投影与残差能量比估计难度，为每句话设置 grounding 强度，并使用 w=1 容忍轻微时间错位。
3. **系统集成**：Qwen-TSE 以 Qwen2.5-0.5B-Instruct 为骨干，结合 WavLM 说话人条件特征和说话人 embedding；推理时 Qwen-TSE checkpoint 保持不变，仅通过 CDCS 修复证据并用 CSG 约束解码。

## 实验结果
- 在 Libri2Mix 上，CDCS 将错误说话人提取错误率从 **6.87% 降至 0.75%**（干净混合），在噪声条件下从 **18.95% 降至 10.46%**。
- 在噪声测试中，固定 CSG 将内容切换率从 **12.79% 降至 9.10%**，声学切换率从 **1.68% 降至 0.51%**；自适应 CSG 分别降至 **9.37% 和 0.53%**。
- CDCS-5 将 BSRNN-TSE 的干净 WER 从 **11.41% 降至 7.02%**，噪声 WER 从 **39.85% 降至 30.67%**，同时减少内容/声学切换并提升说话人 margin。
- 生成式系统仍保持感知质量优势：噪声条件下 Qwen-TSE 系列 DNSMOS/UTMOS 高于确定性 BSRNN-TSE 基线。
- 结果表明：先修复证据身份再 grounding，可提升生成式 TSE 的可靠性，同时保留其感知质量优势。

## 一句话评价
该论文提出了一种训练无关的“先修复、后 grounding”框架，有效缓解了 LLM-based TSE 中的目标说话人混淆与生成漂移问题，在 Libri2Mix 上显著降低错误说话人提取和切换率，同时保留生成式模型的感知质量优势；但噪声场景下 WER 仍然较高，且方法效果依赖冻结 TSE 候选的质量与互补性。

---

## 3. Virtual Microphone Array for Direction-of-Arrival Estimation Based on Fiber-Optic Position Sensing

**作者**: Sebastian Schwarze (1), Jiekai Wang (2), Thomas Kissinger (2), Stephan Werner (1) ((1) Electronic Media Technology Group, Technische Universität Ilmenau, Germany, (2) Nanofabrication and Nanomeasurement Technology Group, Technische Universität Ilmenau, Germany)
**链接**: [2611.06285](https://arxiv.org/abs/2611.06285)
**分类**: Acoustic Direction-of-Arrival Estimation | **关键词**: Virtual Microphone Array, Direction-of-Arrival Estimation, Fiber-Optic Shape Sensing, Time Difference of Arrival, GCC-PHAT

## 核心痛点
传统声源波达方向（DOA）估计通常依赖固定几何、较多麦克风的物理阵列。为了抑制空间混叠，需要密集空间采样，这会增加阵列设计、同步、校准与数据处理复杂度。利用麦克风运动构建虚拟阵列可减少传感器数量，但现有方法多要求麦克风沿预定义轨迹运动，限制了虚拟阵列几何，也难以用于尺寸和重量严格受限的场景。若要从非预定义运动直接构建虚拟阵列，则必须高精度、高时间分辨率地连续重建麦克风轨迹。

## 方法创新
论文提出一种基于光纤位置传感的虚拟麦克风阵列 DOA 估计方法：
- 使用一个运动麦克风和一个静止参考麦克风构成双通道系统；
- 利用运动麦克风产生时变阵列几何，并通过光纤形状传感/干涉式位置传感重建麦克风轨迹，从而获得一系列虚拟麦克风位置；
- 对每个虚拟麦克风配置，估计运动麦克风与参考麦克风之间的到达时间差（TDOA）；
- 每个 TDOA 与对应麦克风几何定义一个双曲面（三维中）或双曲线（二维中），表示与该时间差一致的所有可能声源位置；
- 融合多个双曲面约束，估计相对于麦克风坐标系的方位角和俯仰角。

与固定几何阵列和依赖预定义轨迹的方法不同，该方法直接从实测麦克风运动推导虚拟阵列几何，仅用两个物理麦克风即可形成空间分布的虚拟阵列。系统采用基于光纤段干涉（FSI）的高动态光纤形状传感，并通过三根沿杆周向布置的光纤测量弯曲；每根光纤仅使用一个光纤段，并假设杆形符合悬臂梁模态，从而避免写入光纤布拉格光栅反射器，可使用标准通信光纤尾纤，降低成本。

## 实验与结果
摘要指出，方法在受控低反射条件下进行了实验评估，考察了不同声源位置、声源距离和信号特性；还分析了麦克风运动的影响，并用运动声源进行了测试。结果证明了在不需要预定义麦克风轨迹的情况下，使用虚拟麦克风阵列进行 DOA 估计的可行性。

## 一句话评价
该工作将非预定义运动麦克风、光纤形状传感与 TDOA 双曲面约束相结合，为尺寸/重量受限场景下的双麦克风 DOA 估计提供了一种低成本、可扩展的虚拟阵列思路。

---

## 4. CLRM: Cross-Layer Relation Modeling for Audio Deepfake Detection

**作者**: Yangyang Qu, Siqing Qin, Kong Aik Lee, Massimiliano Todisco
**链接**: [2611.05678](https://arxiv.org/abs/2611.05678)
**分类**: Audio Deepfake Detection | **关键词**: Audio Deepfake Detection, Cross-Layer Relation Modeling, Self-Supervised Learning, XLS-R, Score-Level Fusion, Speech Anti-spoofing, Layer-Pair Selection

# CLRM: Cross-Layer Relation Modeling for Audio Deepfake Detection

## 核心痛点
- **音频深度伪造检测 (ADD)** 旨在区分真实语音与合成/篡改语音，跨生成方法与录音条件的泛化仍是重要挑战。
- 预训练自监督学习 (SSL) 语音编码器（如 XLS-R）在多个处理深度产生表示，而**不同层的表示区分真伪语音的能力差异显著**。
- 现有做法（层选择、多深度特征聚合、逐层预测组合，如 XLSR-SLS 等）虽证明了多层信息的价值，但**并未将“跨层比较”本身作为检测输入**：直接拼接保留了各层表示，却把“如何比较这些表示”的学习负担完全交给分类器。

## 方法创新
**CLRM（Cross-Layer Relation Modeling）** 是一个检测器增强框架，在保留层特有特征的同时显式编码跨层关系：

1. **显式跨层关系表示**：将每层隐藏状态用时间均值 μ_l 与总体标准差 σ_l 拼接成固定维度的语句级摘要 z_l∈R^{2d}，并按 ASVspoof 2019 LA 官方训练集统计量做标准化。对选定层对 (p,q)，构造
   r_{p,q}(x) = [z̃_p; z̃_q; |z̃_p − z̃_q|; z̃_p ⊙ z̃_q; cos(z̃_p, z̃_q)]，
   共 (8d+1) 维。其中绝对差表示逐坐标差异、逐元素乘积编码乘性交互、余弦相似度刻画角度关系；由于在语句级摘要上操作，**无需帧级对齐**。
2. **关系打分**：用 3 个独立初始化的前馈头（线性投影 + GELU + Dropout + 线性输出）分别学习，取原始输出平均得到 s_rel；在源域训练集拟合、源域开发集选检查点。
3. **分数级融合**：将基检测器分数与关系分数各自标准化后，用逻辑回归融合 s_final = a·s̃_base + b·s̃_rel + c，系数在源域开发集拟合、正则强度在 Meta-dev 上选择。**原检测器与 SSL 编码器全程冻结，仅训练紧凑关系头与融合参数**。
4. **几何引导的层对选择**：利用真实语音的说话人标签，构造层几何嵌入（时间均值池化 + ℓ2 归一化），优先选择**编码深度相隔较远但说话人相对组织相似**的层对作为候选，再由源域攻击上的检测误差确定最终层对与融合配置，并原样应用于外部数据集。

## 实验结果
- 在 **5 个外部数据集**上，用 **3 种基于 XLS-R 的检测器架构**评估，所有检测器的五数据集平均 EER 均下降，**相对降低 7.8%–16.7%（最大 16.7%）**。
- 在**相同的层摘要与近似匹配的辅助头参数量**的受控比较下，显式关系特征在融合前后均比直接拼接取得更低的平均 EER。
- 结论支持：显式跨层比较可作为基于 SSL 的音频深度伪造检测器的有效检测输入。

## 主要贡献
1. 提出保留选定 SSL 层摘要并直接编码其差异与交互的**跨层关系表示**。
2. 提出**源域引导的检测器增强**方案：说话人相对层对候选构建 + 源域配置选择 + 关系分数融合。
3. 在 3 种架构、5 个外部数据集上完成**受控实证评估**，验证显式关系优于直接拼接。

## 一句话评价
CLRM 以“冻结主干 + 轻量关系头 + 分数融合”的低成本方式，把原本隐式的跨层比较显式化为检测证据，在多种检测器与外部数据集上稳定降低 EER，为 SSL 多层信息的利用提供了新视角。

---

## 5. SAUCE: Summary Analysis Using Conversation Entailment

**作者**: Man-Ling Sung, Hemanth Kandula, Jeff Ma, William Hartmann, Matthew Snover
**链接**: [2611.06812](https://arxiv.org/abs/2611.06812)
**分类**: Conversational Speech Summarization Evaluation | **关键词**: SAUCE, reference-free evaluation, conversation entailment, cross-lingual speech summarization, faithfulness, coverage, fact extraction, ASR/MT errors, explainability

## 论文基本信息
- **标题**：SAUCE: Summary Analysis Using Conversation Entailment
- **作者**：Man-Ling Sung, Hemanth Kandula, Jeff Ma, William Hartmann, Matthew Snover
- **机构**：RTX BBN Technologies
- **研究主题**：面向跨语言对话语音摘要的无参考、基于事实的自动评估

## 核心痛点
1. **摘要评估缺少唯一参考答案**：同一文档可存在多种正确摘要，用户偏好也会影响风格与内容，难以构建足够参考摘要覆盖所有合理变体。
2. **日常对话摘要更难评估**：对话通常缺少明确终点目标与信息流结构，且包含不流畅、说话人重叠、话题漂移等现象。
3. **ASR 与 MT 级联错误破坏语义表层**：跨语言对话语音摘要中，转录与翻译错误会显著改变文本语义，传统 n-gram 指标和部分 LLM-as-a-judge 方法难以捕捉信息损失。
4. **现有指标可解释性不足**：ROUGE、BERTScore 等偏重词面/语义相似度，未必反映事实准确性；LLM 评判方法虽可给解释，但定量解释困难、计算成本高，并存在自偏好、冗长偏好、AI 摘要偏好等偏差。
5. **用户需要可操作的审计工具**：当摘要得分低时，用户难以判断问题来自幻觉实体、遗漏核心主题还是风格偏差，因此需要能定位具体事实的评估管线。

## 方法创新
SAUCE 是一个无参考、基于事实的评估流程，核心包括两个指标：
- **SAUCE_Faithful**：衡量摘要中的事实被对话文本蕴含的比例，用于评估事实忠实度/准确性。
- **SAUCE_Coverage**：衡量对话中的关键事实被摘要覆盖的比例，用于评估关键信息覆盖率。

### 管线设计
1. **事实抽取**：使用 GPT-4o（gpt-4o-2024-08-06）从对话或摘要中抽取原子事实。作者称 LLM 事实抽取准确率约 90%，其内部评估超过 98%。
2. **文本蕴含判断**：使用 DeBERTa-v3（deberta-v3-large-mnli）判断事实是否被对话或摘要蕴含，因其在 NLI 任务上表现强且计算需求有限。
3. **Faithfulness 计算**：先抽取摘要中的所有事实，再将每个摘要事实与对话分块进行蕴含打分，每块包含 5 行对话；若事实-块得分超过阈值，则视为被对话蕴含。最终分数为被匹配事实的比例。作者也尝试过摘要事实对对话事实的蕴含，但发现事实对对话分块效果更好。
4. **Coverage 计算**：要求 LLM 从对话中只抽取 N 个最重要事实，N 由对话长度和目标压缩率决定；避免抽取全部事实导致事实数量过多。为缓解 LLM 输出不确定性，重复 5 次抽取最重要事实并拼接评分，多次被选中的事实更可能重要。每个事实再与摘要逐行做蕴含判断，计算匹配比例。
5. **事实账本**：SAUCE 不只输出一个不透明分数，而是输出被成功蕴含、被矛盾或未被支持的具体原子事实列表。用户可快速核验摘要，开发者可区分摘要中的幻觉错误与遗漏错误。

### 贡献
- 在存在 ASR 和 MT 错误的情况下有效评估跨语言对话摘要。
- 无需人工标注即可进行基于事实的评分。
- 在文本终点目标不明确时提供可解释的质量测量。

## 实验与结果
### 对话蕴含性能验证
作者在 MSU 公开对话蕴含数据集上评估 DeBERTa-v3 是否适合事实-对话蕴含。该数据集包含假设陈述与来自 Switchboard 的支持性对话块。对话蕴含本身较难，MSU 中仅约一半陈述被所有标注者一致同意。

实验设置包括：
- 直接用 DeBERTa-v3 判断对话块与陈述的蕴含。
- 使用完整对话运行 SAUCE_Faithful 评分，并取最被蕴含的对话块。
- 阈值尝试 0.9、0.95、0.98。

表 1 结果显示：
- 在选定对话块设置下，All 准确率为 77.0/79.2/77.0，NoEnt 为 63.6/71.6/77.1，Ent 为 88.4/85.7/80.0。
- 在完整对话设置下，All 为 68.1/71.4/74.2，NoEnt 为 39.7/49.9/61.4，Ent 为 92.2/89.7/85.0。
- 非蕴含对整体表现更差；部分误判来自时态或说话人身份互换。数据集本身也存在标注问题。
- 最终选择阈值 0.9，因为作者认为正确检测出存在蕴含的对更重要。

### ASR+MT 对话摘要评估
作者在阿拉伯语、西班牙语、汉语普通话和俄语四种语言的电话对话语音上实验。数据来自 LDC：阿拉伯语用 CallHome2，西班牙语用 CallHome3 和 Fisher，普通话用 HUB5，俄语用 Mixer 3 Speech。片段提到使用众包英文翻译，但后续内容被截断。

## 一句话评价
SAUCE 通过“原子事实抽取 + 对话蕴含”将摘要评估从单一黑箱分数转化为可核验的事实账本，在跨语言、含 ASR/MT 噪声的对话语音摘要场景中兼顾忠实度、覆盖率和可解释性，具有较强的实用价值。

---

## 6. SonoDyno: A Sonic Dynamometer for Engine Speed and Load Estimation from Audio

**作者**: Robin Doerfler, Beat Rossmy
**链接**: [2611.06262](https://arxiv.org/abs/2611.06262)
**分类**: Engine Audio Analysis / Acoustic Sensing | **关键词**: 发动机转速估计, 缸数估计, 负荷强度估计, 阶次分析, 无转速计测速, 发动机声音合成, Viterbi 解码, 声学测功

# SonoDyno 论文总结

## 核心痛点
- 发动机声音合成、主动声音设计（Active Sound Design）和阶次分析都依赖发动机瞬时运行状态，即转速与负荷；但带时间对齐标注的发动机录音非常稀缺。
- 获取标注通常需要转速计、测功机或访问车辆 CAN 总线等专用设备，成本高且接口常为专有。
- 现有无转速计方法或通用音高跟踪器难以直接用于未知发动机音频：
  1. 点火频率由“缸数 × 转速”共同决定，仅凭最强谐波线无法区分缸数与转速，会产生倍频混淆；
  2. 低转速时相邻阶次间隔很小，需要长分析窗，而急加速/换挡时转速快速变化又需要短分析窗，存在时频分辨率冲突；
  3. 阶次谐波结构会随转速、负荷、排气共振、麦克风位置、涡轮/胎噪/风噪等剧烈变化；
  4. 绝对扭矩无法仅从录音恢复，响度也不能表示负荷方向与相对大小。

## 方法创新
- 提出 SonoDyno，仅用麦克风信号估计发动机转速、缸数和发动机归一化负荷强度，无需转速计、总线访问或先验发动机配置。
- 前端在三个时间-频率分辨率上计算每帧的阶次能量，并在每个窗口内细化、跨窗口按阶次融合，避免不同阶次相互混合。
- 使用 124,302 参数的卷积评分器，对“缸数-转速”候选对联合打分；缸数仅通过点火阶次增益进入模型，因此一个模型可服务 1 到 18 中的 11 种缸数配置。
- 引入阶次模式检测器，跨所有阶次读取模式而不依赖缸数，帮助评分器应对快速转速变化。
- 使用基于转速及其相对变化率的 Viterbi 解码器施加旋转动力学约束，惩罚不合理的转速变化率，并从最佳路径读取缸数。
- 定义负荷强度 λ∈[0,1]：0 对应发动机制动/倒拖时的阻力下限，1 对应全负荷上限；用解码转速处的阶次电平估计 λ，并可结合发动机曲线在扭矩与 λ 之间转换。

## 实验结果
- 在完全未见过的真实发动机上：93% 到 97% 的帧转速误差在 2% 以内；缸数识别准确率 80%；倍频混淆少于 2% 的帧。
- 在已知类型但未见过的发动机上：负荷强度 λ 的平均绝对误差为 0.12；驱动/制动扭矩符号判断在 91% 的帧上正确。
- 在验证录音、5% 容差下，即使向最佳通用音高跟踪器提供谐波阶次，其仅有 62% 的帧在容差内，而 SonoDyno 达到 96%。
- 评分器仅 124,302 个学习参数，不大于最小的学习式跟踪器。
- 论文还通过逐项实验分析设计选择，包括前端、阶次模式检测器、动力学解码器等模块的贡献。

## 一句话评价
SonoDyno 将发动机阶次分析、学习式联合推断与物理旋转动力学解码结合，在未知发动机音频上实现了高精度转速/缸数估计和可用的归一化负荷估计，为无传感器发动机声学标注与可控声音合成提供了实用方案。

---

## 7. Human-like cross-language generalisation in deep neural speaker embeddings and its acoustic foundations

**作者**: Tianze Xu, Xiyang Li, Xiaoming Jiang, Volker Dellwo
**链接**: [2611.05384](https://arxiv.org/abs/2611.05384)
**分类**: Speaker Recognition (Speaker Embedding) | **关键词**: speaker embeddings, cross-language generalisation, voice similarity, human-machine alignment, representational similarity analysis, Cantonese-English bilingual speech

## 论文基本信息

- **标题**：Human-like cross-language generalisation in deep neural speaker embeddings and its acoustic foundations
- **作者**：Tianze Xu、Xiyang Li（共同一作）、Xiaoming Jiang、Volker Dellwo
- **单位**：苏黎世大学计算语言学系；上海外国语大学语言科学研究院
- **发表**：已接收至 Interspeech 2026（arXiv:2611.05384v1）
- **代码**：github.com/xiyangg12/wespeaker（Zenodo 归档）

## 核心痛点与研究动机

1. **跨语言泛化问题尚未得到充分研究**：深度神经网络能否把从既有经验中学到的表征与策略迁移到新输入（例如从英语迁移到粤语），是当前语音与语言处理领域的核心问题。说话人建模（speaker embedding）尤其敏感：不同语言的音系与语音结构存在系统性差异，会调制声音的声学实现，进而威胁跨语言语音合成、自动说话人识别等下游任务。
2. **工程优化较多，与人类感知对齐的机制研究较少**：大量工作致力于提升 embedding 的跨语言鲁棒性，但“深度说话人 embedding 是否、以及如何跨语言泛化，特别是它与人类听感的关系”，仍缺乏系统检验。
3. **既有对比研究存在局限**：Liu 等 [11] 在英语材料上发现，在细粒度控制下，感知相似度与机器相似度无显著相关，机器相似度只与 24 个声学变量的聚合结果相关，但该研究未涉及跨语言泛化；Gerlach 等 [12] 虽跨语言，但使用的是基于 MFCC 的早期模型。
4. **人类具有强跨语言泛化能力**：Xu 与 Jiang [8] 发现，英语母语者（无论是否具备粤语能力）在粤语、英语、混合语言条件下判断声音相似度时表现一致：同说话人对比异说话人更相似；混合语言对的评价更不相似（语言切换干扰了声学线索整合）；音高、声道构型和谐波/噪声频谱平衡是关键线索，且其权重随语言语境变化。

## 方法创新

### 数据
- **语音**：SpiCE 语料库，10 名早期粤语–英语双语女性（19–32 岁），每种语言 2 条语义可比的节日祝福语（粤语约 1.17–1.43 s；英语约 1.18–1.87 s）。
- **感知数据**：40 名被试（20 名粤语–英语双语者 + 20 名不懂粤语的英语母语者），9 点相似度量表，220 个试次（40 个同说话人对 + 180 个异说话人对；55 个纯粤语、55 个纯英语、110 个混合语言）。
- **声学特征**：5 大域共 29 个心理声学变量，用 VoiceSauce 每 5 ms 从清浊段提取——时间域（语速 SR）、音高（f0）、共振峰结构（F1–F4 与共振峰离散度 FD）、谐波源（H*1−H*2、H*2−H*4、H*4−H*2kHz、H*2kHz−H5kHz 相对幅度）、非谐波源（RMS 能量、CPP、SHR、HNR）；除 SR 与谐波谱形外均计算均值与变异系数（谐波量用 SD 代替 CV）。

### 模型与实验设计
- 用 **Wespeaker 1.2.0** 提取 embedding，覆盖 **18 个预训练模型**，横跨架构、参数量与预训练语料：
  - 7 个 ResNet（ResNet34-VX、ResNet34LM-VX、ResNet152LM-VX、ResNet221LM-VX、ResNet293LM-VX、ResNet34-CN、ResNet34LM-CN）；
  - 4 个 SimAM-ResNet（SimAMResNet34-VB/VBVX、SimAMResNet100-VB/VBVX）；
  - 5 个 ECAPA（ECAPA1024-VX、ECAPA1024LM-VX、ECAPA512-VX、ECAPA512LM-VX、ECAPA512DINO-VX）；
  - 2 个 CAM++（CAM++-VX、CAM++LM-VX）。
  - 后缀含义：-VX = VoxCeleb、-CN = CN-Celeb、-VB = VoxBlink2、-VBVX = VoxBlink2 预训练 + VoxCeleb2 微调；LM = large-margin softmax。
- **粤语微调**：在 ASR-SCCantDuSC（约 4 h、10 说话人）与 ASR-SCCantCabSC（约 5 h、10 说话人）上按原训练目标微调，得到 18 个微调版本，共 **36 个 machine RDM**。
- **统计建模**：
  - **线性混合模型（LMM）**：以 embedding 余弦相似度为因变量，固定效应包括说话人身份（同/异）、刺激语言（粤/英/混合）、微调状态、模型架构及其全交互；模型与语音对设随机截距，模型内说话人身份设随机斜率（逐步化简后保留）。
  - **表征相似性分析（RSA）**：构建感知 RDM（40 个）、声学 RDM（29 个）、机器 RDM（36 个），用 Spearman 秩相关按刺激语言、听者语言背景、微调状态分别计算，并以单侧 Wilcoxon 符号秩检验 + FDR 校正（α=.05）评估显著性；机器–感知相关性再用 LMM 分析。

## 实验结果

- 机器相似度范围为 0.41–0.92（M=0.63，SD=0.09）。
- LMM 显示显著主效应：说话人身份 χ²(1)=671.39, p<.001；刺激语言 χ²(2)=175.15, p<.001；微调状态 χ²(1)=17.30, p<.001；模型架构 χ²(3)=94.70, p<.001。
- 交互项中**仅说话人身份 × 刺激语言显著**（χ²(2)=81.49, p<.001）；说话人身份 × 微调（p=.827）、刺激语言 × 微调（p=.126）及三阶交互（p=.765）均不显著——说明粤语微调并未改变身份区分与语言切换效应的基本模式。
- 同说话人对相似度（M=0.78）显著高于异说话人对（M=0.60）；纯英语对的平均相似度最高（原文该处被截断）。
- 总体结论（摘要层面）：embedding 表现出**跨语言泛化**，且与人类行为大体平行——既能准确区分身份，又对语言切换敏感（混合语言对更不相似）；这种泛化依赖**大体共享的声学线索**，但线索权重随语言语境变化，与人类模式一致。RSA 进一步表明机器表征与人类说话人身份表征及细粒度声学特征存在对应关系。

## 结论与意义

- 为“跨语言声音相似度加工中的人机对齐”提供了收敛性证据：说话人 embedding 的跨语言泛化并非纯粹的语言无关魔法，而是建立在与人类共享的声学基础上、并带有语言敏感加权。
- 方法上把**工程指标（余弦相似度）**与**认知表征（RSA + 感知 RDM）**桥接，为评估语音模型提供可解释的评测范式。
- 实践上提示：预训练语料以英语/普通话为主（VoxCeleb、CN-Celeb），对粤语等低资源语言的有效性需谨慎；微调可适配但不改变基本泛化结构。

## 局限（基于片段可推断）

- 仅 10 名女性说话人、每人每语言 2 条短句，规模小；仅粤语–英语一对语言。
- 结果部分在提供的片段中被截断，声学–感知权重的具体数值与 RSA 相关性大小无法完整核实。

## 一句话评价

该研究用 18 个 SOTA 说话人 embedding（含粤语微调版本）、29 个声学变量与 40 名听者的感知数据做三方 RSA 对齐，首次系统证明深度说话人表征的跨语言泛化在行为模式与声学基础上都与人类高度相似，为“人机对齐”提供了可复用的评测框架。

---

## 8. Cross-Codec Robustness in Speech Watermarking

**作者**: Olli-Pekka Pauna, Xin Wang, Lauri Juvela
**链接**: [2611.04716](https://arxiv.org/abs/2611.04716)
**分类**: Speech Watermarking | **关键词**: speech watermarking, neural audio codec, zero-bit watermarking, channel augmentation, codec resynthesis, robustness

## 核心痛点
- 生成式语音模型可零样本合成高度逼真的语音，水印是主动披露合成内容、应对滥用与合规需求的重要手段。
- 现有深度水印模型虽能通过训练时通道增强抵抗传统 DSP 攻击，但仍易受神经音频编解码器重合成、声码器、去噪等未见神经攻击影响。
- 不同神经编解码器在架构、训练目标和重构行为上差异明显，单一编解码器增强难以泛化到未见编解码器，因此需要寻找可跨编解码器泛化的增强配方。

## 方法创新
- 提出一种新的零比特语音水印系统：以 Descript Audio Codec（DAC）作为水印生成器，冻结其编码器与量化器、微调解码器，以保持码本向后兼容；使用 AASIST 作为水印检测器，并保留 DAC 对抗判别器。
- 生成器采用多目标损失：DAC 原有的多尺度梅尔损失、最小二乘 GAN 损失、判别器特征匹配损失，加上水印检测损失；生成器与检测器协同训练，使生成器帮助检测器识别水印。
- 训练时引入神经音频编解码器通道增强：原始音频与水印音频在送入检测器前经过独立的冻结神经编解码器；针对 EnCodec、SpeechTokenizer、Mimi 修改官方代码以支持冻结模型端到端反传，SNAC 与 DAC 原生支持，并开源增强实现。
- 系统比较 7 个相同水印模型：无增强、5 个单编解码器增强（EnCodec 6 kbps、DAC 8 kbps、SpeechTokenizer 4 kbps、Mimi 1.1 kbps、SNAC 0.98 kbps），以及 Mimi+SNAC 双编解码器随机增强。

## 实验设置与结果
- 数据使用 LibriTTS-R，训练集为 train-clean-100，验证与测试为 dev-clean、test-clean；水印模型微调 40,000 次迭代，批大小 8，使用 AdamW，单张 A100 训练。
- 评估覆盖多种神经编解码器攻击、传统编解码器（MP3、Ogg Vorbis、Opus）、加性噪声、混响、低通/高通滤波，以及随机排列的多次神经编解码器重合成；并与 AudioSeal、WavMark 等后置水印基线比较。
- 论文摘要与引言给出的核心结论是：通道增强所用神经编解码器的选择会显著影响鲁棒性泛化；采用低比特率、高质量的 Mimi 与 SNAC 联合增强，可对未见神经编解码器和传统攻击取得有前景的鲁棒性，同时音频质量影响有限。
- 由于提供的论文内容在实验评估部分被截断，未包含完整的数值结果与听测细节。

## 一句话评价
- 该工作系统性揭示了训练时神经编解码器增强选择对跨编解码器水印鲁棒性的关键作用，并提出以 Mimi 与 SNAC 联合增强的实用配方，为神经编解码器攻击下的语音水印鲁棒性研究提供了新基线。

---

## 9. VeriSpoof: Beyond Real or Fake with One Audio LLM

**作者**: Yang Xiao, Ting Dang
**链接**: [2611.04634](https://arxiv.org/abs/2611.04634)
**分类**: Speech Deepfake Detection / Audio Forensics | **关键词**: 语音深度伪造检测, 音频语言模型, 源验证, 生成器归因, 可验证推理, 反事实训练

## 一句话评价
VeriSpoof 提出用一个开放音频语言模型统一语音深度伪造检测、生成器归因、录音条件分析、合成片段定位与同源验证，并把每个判断写成可逐句核验的理由；在 Speech-DF-Arena 上取得开放权重系统第一，同时展示出可解释性和反事实忠实性。

## 核心痛点
现有语音深伪检测器通常只回答“真/假”并输出一个分数，但法证分析还需要回答：是哪个系统生成的、两段录音是否同源、判断依据是什么。作者指出三个问题：
1. **一个分数只回答一个问题**：源追踪、同源比较往往需要额外模型或 Siamese 网络，每个新问题都要新数据和新模型。
2. **解释不能作为证据**：已有音频语言模型的解释多为自由文本或教师模型蒸馏，未验证陈述是否真实，也未测试决策是否依赖该解释，可能流畅但错误或正确却无关。
3. **不清楚瓶颈在哪里**：尚缺乏控制实验衡量音频表示、LLM、源监督分别限制检测还是同源比较。

## 方法创新
- **统一五类法证任务**：深度伪造检测、生成器归因（生成器、声学模型、声码器）、录音条件分析、合成片段定位、源验证，共享一套权重。
- **将法证问题转化为答案打分**：每个问题的候选答案写成句子，读取句子似然作为分数；检测和源验证无需单独分类头，并可在操作点阈值化。
- **可逐句核验的理由**：解释由固定字段陈述组成，观测值在模型听到的波形上测量，合成片段来自标签，源画像来自生成器元数据，因此每条陈述可独立检查。
- **反事实训练**：通过反事实样例训练模型让决策跟随所述证据，即在证据被改写或反转时改变判断。
- **轻量训练与部署**：2.85B 参数中仅训练 29.7M；使用梯度检查点，每个训练阶段可放入单张 24GB GPU，估计训练可适配 12GB GPU、推理可适配 8GB GPU。

## 数据与模型
- **VeriSpoof-Base**：仅使用八个语料官方训练划分，约 0.38M 条语音训练。
- **VeriSpoof-Plus**：在 Base 基础上扩展十二个额外语料和更大平衡训练混合。
- 发布内容：两个模型、推理代码（vLLM 后端）、在线 demo，以及 VeriSpoof-Bench 评测套件（54 个测试子集、177,852 个条目，覆盖检测、归因、源验证、录音条件、 grounded reasoning 与忠实性）。

## 实验结果
- **检测**：Speech-DF-Arena 14 个测试集上，VeriSpoof-Plus 达到 2.14% pooled EER、1.79% mean EER，在 28 个系统中排第三、开放权重第一；VeriSpoof-Base 达 4.43%，次优开放权重系统为 9.52%。
- **同源验证**：对训练中未见生成器的配对，VeriSpoof-Plus 在已知架构新模型上 6.2% EER、新架构上 15.0% EER；冻结反欺骗编码器上的 pair probe 分别为 26.5% 和 24.8%，通用音频 LLM 接近随机。
- **瓶颈分析**：固定编码器时，改变特征使用方式可将 ASVspoof 5 EER 从 9.6% 降至 3.1%，但源验证仍在 16–19%；替换 LLM 对检测仅影响约 0.5 个点，对源验证影响约 5.5 个点。结论是音频表示决定检测，LLM 决定两段录音比较。
- **源标签作用**：在真实性标签数量匹配时，源监督在 16 个集合中 8 个有帮助、1 个有害；对于神经编解码伪造，源监督是必要的。
- **推理收益**：在 PartialEdit 上，先写理由再决策可捕获 99.6% 的部分伪造，而一步答案仅 78.4%；在未见编辑下，反事实训练后 99.5% 的决策跟随改写/反转的定位证据，无此训练时为 73.8%。
- **理由可核验性**：SNR 与电平陈述在 88–100% 录音上正确，说明陈述可逐条检查。

## 关键结论
VeriSpoof 的核心贡献不只是更高的检测分数，而是把“真/假”扩展为可核验的法证问答：同一模型可检测、归因、定位并比较来源，且解释的每条陈述都有独立检查，决策可通过反事实测试验证是否真正依赖所述证据。

---

## 10. Attendance-guided speaker enrollment across meetings

**作者**: Minjae Lee, Hee-Soo Heo, Youngki Kwon, Bong-Jin Lee
**链接**: [2611.04394](https://arxiv.org/abs/2611.04394)
**分类**: Speaker Enrollment (Speaker Recognition) | **关键词**: speaker enrollment, speaker diarization, meeting corpus, benchmark, attendance metadata, profile contamination

## 一、论文信息
- **标题**：Attendance-guided Speaker Enrollment across Meetings
- **作者/机构**：Minjae Lee, Hee-Soo Heo, Youngki Kwon, Bong-Jin Lee（NAVER Cloud，韩国）
- **研究方向**：利用会议存档与期望出勤名单进行多人自动声纹注册（multi-participant automatic enrollment）

## 二、核心痛点
1. **注册语音难以获取**：会议转写中的说话人归属、声纹服务、智能助手等个性化语音应用都依赖“已注册的声纹档案”，而现实中这些档案必须先被构建。显式注册要求每位用户单独录音，采集成本随参与人数线性增长，不具可扩展性。
2. **会议存档是零成本的替代语音源**：反复召开的会议天然积累录音，日程系统又提供每次会议的“期望出勤名单”（expected attendance list）。但该名单只是**期望而非观测**：列名者可能缺席或沉默（inclusion noise，纳入噪声），发言者可能根本未被列出（omission noise，遗漏噪声）；即便有签到记录也无法消除该鸿沟，因为“出席”不等于“发言”。
3. **档案污染风险（profile contamination）**：若把他人语音误当作目标说话人的注册语音，将污染声纹档案并破坏下游判决。注册质量取决于片段**可靠性**而非数量，因此系统在证据不足时应当**弃权（abstain）**；而风险敏感部署（要求低污染）恰恰处于最不利的成功–污染权衡区间。
4. **现有工作空白**：已有工作仅涉及元数据辅助注册“录音用户本人”（无定量评测、无公开基准）、用外部元数据/屏幕文字给 diarization 聚类命名、以及带未知客人的家庭场景被动注册；**没有人形式化或基准化“从含噪会话级出勤名单中注册多个重复参会者”**。现有公共会议语料也不同时满足三个条件：跨会话一致身份的重复说话人、足够的复现与出勤变化、独立采集的期望出勤名单。

## 三、任务定义（Task Definition）
- **Episode**：档案级处理单元，由带索引 s 的多个会议会话组成；每个会话提供一段录音与一份期望出勤名单 L_s；真实说话人身份不提供。
- **输入**：仅“匿名说话人聚类”+“期望出勤名单”；**输出**：对每个名字返回被认为是该人语音的候选片段，或弃权。
- **关键洞察**：单会话内名字与声音是两个无序集合，无法建立对应；身份只能靠**跨会话对齐**——声学相似度把同一说话人的复现聚类串成 chain，而**期望出勤模式的变化是唯一的命名证据**。若两位参与者发言存在模式完全相同（如示例中的 Ben 与 Cara），则单凭该证据不可区分，方法必须对二者都弃权。
- **前端接口假设**：为隔离“出勤驱动的身份关联”与 diarization 误差，假设会话内聚类为 oracle（纯净单说话人、去除重叠语音），并剔除短于 4 s 的片段（短片段嵌入不可靠）；混叠/欠聚类破坏聚类纯度，过聚类则把同一人语音切碎，而在只有名单+匿名聚类的情况下这类前端误差通常无法与出勤噪声区分，故仅作诊断性量化（Fig. 2b）。
- **两类出勤噪声**：设 A_s 为会话 s 中实际发言的具名说话人集合（仅用于构造与评测，不作方法输入），则 r_inc = Σ|L_s − A_s| / Σ|L_s|（纳入噪声率），r_om = Σ|A_s − L_s| / Σ|A_s|（遗漏噪声率）。inclusion 会制造无支撑的“名字–会话”关联并稀释出勤证据；omission 会隐藏该说话人实际出现的会话、削弱跨会话模式——因此“名字不在名单中”只构成对比性而非结论性的负证据。
- **说话人集合划分**：P = ∪L_s 为注册候选集；被所有名单遗漏者为 off-list，任何基于名单的方法都不可达，排除出评测；**评测人群（evaluation population）** = 至少出现在一份名单、至少在一次会话中发言、且其“发言存在模式 a_p”在 episode 内唯一的说话人（a_p 是真值版的期望出勤模式，仅用于定义人群与打分）；模式与他人重复的 non-evaluated 说话人不计分，但其语音保留在数据中作为干扰聚类。

## 四、方法创新
1. **任务形式化 + 污染敏感评测协议（贡献 1）**：给出多人自动注册的完整形式化定义，并设计“在开发集上按污染预算选工作点、报告完整污染–成功曲线”的评测协议。
2. **参考方法（单一可调阈值，Fig. 1 五阶段）**：
   - ① 读取会议档案与期望出勤名单；② diarization 得到匿名单说话人聚类；③ 依据跨会话声学相似度构建聚类链（同色同链）；④ **身份赋值**：将每条链的跨会话出现模式与各参与者的期望出勤模式比对，仅当声学证据与某一模式足够一致时赋名，否则**弃权**（含 m=3 的资格门槛）；⑤ **注册**：对已命名参与者，选取最接近该链“池化均值嵌入（pooled mean embedding）”的片段作为注册语音，每个名字最多输出 3 段，以抑制逐会话的伪选择。
3. **合成基准（贡献 2）**：构建统计特性（说话人复现率、会话构成、出勤噪声率）与内部真实会议语料对齐的合成语料，并设计**四种条件分别隔离 inclusion 与 omission 噪声**；承诺发布基准生成器与评测代码。
4. **合成→真实迁移分析（贡献 3）**：用单一阈值设计便于分析“在合成开发数据上调阈值后，不改动地用于真实会议”的迁移行为，量化 synthetic-to-real gap。作者称这是**首个针对“从含噪会话级出勤名单中为多位重复参会者抽取带名注册语音”的基准**。

## 五、实验与结果（可见部分）
- **评测指标**：strong success（≥3 段目标语音且零污染）、contamination（含任意错误说话人片段即算污染）、weak success（≥1 段且零污染，仅作阈值选择的平局裁决）、segment recall（正确注册的目标片段比例）；所有指标在评测人群上按 episode 汇总分子分母。
- **工作点选择**：对每个污染预算 ε，仅在开发集上最大化 strong success（受预算约束），平局依次用 weak success、segment recall 打破；选定阈值**不调整**地应用于评测集，并报告预算网格上的工作点（含无阈值饱和极限）。
- **主要发现**：
  1. 注册成功与污染之间存在明显权衡，而**低污染（risk-sensitive）区间恰是成功–污染权衡最不利的区域**；
  2. 把合成开发集上的阈值原封不动迁移到真实会议时性能下降，暴露出**仍未解决的 synthetic-to-real 鸿沟**（被明确定位为 open challenge）；
  3. 放宽 oracle 前端假设（真实 diarization 误差）带来可量化的性能代价，仅作诊断性分析。
- **局限**：内部语料规模不足以支撑可靠开发/评测，扩充又需昂贵的说话人级与片段级标注，因此主要实验建立在合成基准上。

## 六、一句话评价
本文把“会议存档 + 期望出勤名单”这一零成本副产品转化为可评测的多人声纹自举注册任务，用单阈值参考方法与污染敏感协议**诚实地暴露了低污染区的权衡代价与合成–真实鸿沟**，是该方向上首个系统性基准工作；但其 oracle 会话内聚类假设与对合成数据的依赖，使结论距真实可用仍有一段距离。

---

## 11. NepTTS-Bench: Native-Speaker Benchmarking and NepaliMOS for Nepali Text-to-Speech

**作者**: Ashish Thapa, Rupak Ghimire, Lekhnath Sharma Pathak
**链接**: [2611.03718](https://arxiv.org/abs/2611.03718)
**分类**: Text-to-Speech | **关键词**: Nepali Text-to-Speech, TTS Benchmark, MOS Prediction, Minimal Pairs, Phonological Evaluation, Native-Speaker MOS, Automatic Speech Recognition, Speech Quality Assessment

## 核心痛点
尼泊尔语 TTS 已有多套公开模型和商用 API，但**缺乏统一、可复现的评测标准**：不同论文使用的测试集、听者池、评测协议均不相同，导致论文间报告的 MOS 分数无法直接比较；同时，面向英语训练的通用质量指标（如 SCOREQ）与 ASR 往返 CER，无法反映尼泊尔母语听者对送气、卷舌/齿音对立、鼻化、辅音重叠、央元音脱落等音系特征的敏感度，容易让系统排名失真。

## 方法创新
- **NepTTS-Bench 基准**：包含 205 句尼泊尔语测试句，其中 147 句构成 77 个最小对立对（覆盖送气/清浊、卷舌-齿音对立、口鼻元音、辅音重叠、央元音脱落），其余 58 句覆盖疑问语调、情感、对比重音、同形异读、语码混合、绕口令等实际场景。
- **统一评测协议**：由 180 名尼泊尔母语者通过网页应用对匿名音频在 1–5 MOS 量表上评分，同句刺激至少间隔 3 个位置，平衡随机采样；对 10 个 TTS 配置 + 2 个人工参考（自然语音、朗读语音）共收集 6,962 条评分。
- **NepaliMOS 预测器**：基于 IndicWav2Vec base 微调，帧表示平均池化后接两层回归头（768→256→1，ReLU + dropout 0.1），解冻 top-4 transformer 层，以音频级平均 MOS 为监督、MSE 损失训练；使用差分学习率（头部 1e-4、骨干 1e-5）、batch size 2、按验证损失选最优 checkpoint。最终匹配集含 1,697 个唯一 TTS 片段（来自 5,865 条匹配评分），90/10 语句级划分（1,530 训练 / 167 验证）。
- **自动化指标对照**：7 个 ASR 系统（Chirp 2、MMS、XLS-R Nepali、NepConformer、Whisper-small、Whisper large-v2、Whisper large-v3-turbo）做往返 CER 评测，SCOREQ 作为无参考质量基线；统计采用 95% 聚类 bootstrap（2,000 次重采样）、Spearman ρ、Benjamini–Hochberg 校正与 Krippendorff's α。
- **LOSO 迁移验证**：留一系统（leave-one-system-out）验证以测试跨厂商泛化能力。

## 实验结果
- **人类 MOS 排名**：自然语音 3.95 > 人工朗读 3.64 > TingTing Asmita 3.55 > **Piper 3.50** > TingTing Subina 3.47 = ElevenLabs v3 3.47 > Edge TTS Sagar 3.38 > Edge TTS Hemkala 3.37 > Gemini (Hindi) 3.34 > Gemini Flash 3.25 > TingTing Sambriddhi 3.20 > gTTS 2.60；顶部系统置信区间重叠，无法选出唯一赢家，gTTS 显著垫底。
- **指标一致性（表 II）**：NepaliMOS 与人类 MOS 的 ρ=0.90（BH 校正后 p=0.001，唯一显著），其次 Chirp 2 CER ρ=0.60、MMS CER 0.58、XLS-R Nepali CER 0.53、SCOREQ 0.40、NepConformer 0.30、Whisper large-v2 0.22、Whisper-small 0.17。
- **自动指标与人类偏好背离**：ElevenLabs 在 SCOREQ 上排名第 1 但人类 MOS 仅第 4；Piper 的 SCOREQ 排第 8 却被母语者评为第 2；Gemini Flash 的 Whisper-small CER 最低却人类 MOS 偏后。说明音频“干净易转写”不等于“听起来地道”。
- **评分者间一致性低**：Krippendorff's α=0.17，限制了接近质量系统被精确排序的能力。
- **NepaliMOS 的实际局限**：密集面板系统级 ρ=0.90，但在 LOSO 语句级仅 ρ=0.43——虽统计显著说明模型捕获真实信号，但跨厂商迁移有限，故建议对新系统做人工校准。
- **负面发现**：Whisper large-v3-turbo 存在幻觉，2%–10% 的文件 CER>1.0（Edge TTS Hemkala 达 186，gTTS 达 1,115），仅作阴性对照保留。

## 一句话评价
NepTTS-Bench 首次为尼泊尔语 TTS 建立了音系驱动的母语者共享基准，用实证数据揭示通用自动指标（SCOREQ/ASR CER）与母语听感之间的系统性错位，并提出有明确适用边界的 NepaliMOS（系统级 ρ=0.90、LOSO 语句级 ρ=0.43），为低资源语言的 TTS 评测提供了可复用的方法论模板。

---

## 12. ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models

**作者**: Ming-Hao Hsu, Shujie Liu, Yuxuan Hu, Yuxiang Wang, Yingda Shen, Jinyu Li, Zhizheng Wu
**链接**: [2611.04480](https://arxiv.org/abs/2611.04480)
**分类**: Long-Form Audio Question Answering (Audio Language Models) | **关键词**: training-free, audio language models, long audio understanding, evidence localization, temporal grounding, Jev-style scan, log-odds scoring, hour-long audio

# ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models

**作者/机构**: Ming-Hao Hsu, Shujie Liu, Yuxuan Hu, Yuxiang Wang, Yingda Shen, Jinyu Li, Zhizheng Wu（香港中文大学（深圳）数据科学学院、微软亚洲研究院、Microsoft CoreAI）

## 1. 核心痛点
- **音频语言模型（ALM）的上下文与任务时长严重不匹配**：现有 ALM 只能处理秒级到分钟级音频，而会议、讲座、广播、播客等真实场景常长达一小时以上；且答案往往只依赖其中几秒钟的内容。基准（LongAudioSpan、VoiceGiraffe、LAT-Bench 等）显示随着时长增加，准确率显著下降，很多模型根本无法把一小时音频作为输入。
- **现有两条路线的缺陷**：
  1. **先转写再检索/阅读（ASR + 文本检索）**：虽然能把一小时压缩进上下文，但答案变成“文本阅读理解”，**丢失了声音、说话人音色与时间信息**，而这些恰恰是许多问题的对象，也是 ALM 的专长。
  2. **训练模型“回到音频”（LAT-Audio 用音频裁剪细化全局时间线，Echo 在推理中生成时间戳请求片段，Speaker-Reasoner 学习多轮时间交互）**：需要针对每个新音频模型重复微调，成本高、不可即插即用。
- 因此理想方案应满足：**直接在音频上检索、无需独立前端、无需额外训练**。

## 2. 方法创新：ReListen
**核心思想**：把“在一小时音频中定位证据”这一困难搜索，降解为大量模型本来就能做的小判断——“这段短音频是否有助于回答问题”，从而让**同一个冻结的 ALM 既做检索又做回答**。

### 2.1 Jev-style 扫描（免训练、无生成）
- 将录音切成长度 τ=20 s、跳步 δ=10 s 的重叠窗口 $w_1,\dots,w_n$。
- 对每个窗口输入音频与由问题构造的 yes/no 提示（原生问题：“该片段是否包含有助于回答问题的信息？”；事件问题：“该片段是否包含事件 e？”）。
- **不生成 yes/no 文本**，而是读取第一个答案位置上的 next-token 分布，取对数几率作为相关性分数：
 $$\ell_i = \log p_\theta(\text{yes}\mid w_i,c) - \log p_\theta(\text{no}\mid w_i,c)$$
 分数为正表示“yes”更可能；分数越高排名越靠前。
- 所有窗口共享提示与长度，可无 padding 批处理；每窗口一次前向；**代价随时长线性增长、显存恒定**，且窗口互相独立可多 GPU 并行。

### 2.2 原生问题回答
- 按 $\ell_i$ 降序取窗口，跳过与已选窗口重叠者，取 b=3 个窗口（60 s，预算 bτ）。
- 按时间顺序把这些片段（相邻者合并、各自标注起止时间戳）喂回同一冻结模型回答原问题。
- **事件区间（grounding）**：从最高分窗口出发，向左右扩展连续正分窗口，得到输出区间，时长由分数决定而非固定预算。

### 2.3 出现次数问题（k-th occurrence）的有监督扩展
- 相关性排序对“第 k 次出现”类问题存在固有局限（需找全所有更早出现且不误计）。
- 部分事件类型（如音量/速度变化）不由音频内容描述，扫描分数信息量低。
- 方案：两个小型 CNN 声学检测器（在基准类型的**合成编辑**上训练）提出候选事件时间 → 在开发集上拟合逻辑回归校准 → Poisson–binomial 后验求第 k 次出现 $t^\star$ → 取 $t^\star$ 周围 60 s 交给 reader 回答。

**关键性质**：主路径**零训练、零转写、零生成时间戳**；片段的时间就是所选窗口的位置。

## 3. 实验结果
配置仅在 **LongAudioSpan 开发集一半**上选定，随后**原封不动**在 LongAudioSpan 测试半、VoiceGiraffe、LAT-Bench 上评测。

**（1）证据定位能力**
- 所选 1 分钟与标注证据重叠的比率为 **88.5%**（VoiceGiraffe），远超转写检索的 **58.8%**。
- LAT-Bench 平均时间 IoU **47.7**，与专门训练的 LAT-Audio（46.3）相当——且无需任何训练。

**（2）回答准确率（同等 1 分钟音频预算）**
- 相比均匀采样：LongAudioSpan **+8.5** 分，VoiceGiraffe **+21.3** 分。
- VoiceGiraffe 上是最准的音频输入形式，比“读整段录音的转写”高 **9.2** 分。
- LongAudioSpan 上与“听完整段录音”持平。
- 声音类问题上，“听所选片段”比“读其转写”高 **8.6** 分，说明**选出的证据值得“听”而不是“读”**。

**（3）效率**
- 约一小时录音上，比“转写+阅读”流水线快 **7–8 倍**。
- 显存随时长**恒定**，即使录音长到单卡无法整段收听；窗口可跨 GPU 并行。

**（4）可视化案例（图1）**：84 分钟录音、关于“菠萝披萨 vs 冷披萨辩论中有几位不同说话人”的问题，扫描选出的三个最佳窗口与标注证据重叠，答案 5 正确；而均匀取三个窗口时同一模型答成 4（错误）。

## 4. 与相关工作的对比
- **长音频理解**：剪枝音频 token、在音频/转写/事件索引上检索、阅读短窗口的文本描述——都依赖独立前端（识别器、嵌入模型、captioner）决定回答模型“听到什么”；ReListen 让**回答模型自己决定**。
- **概率作为分数**：文本 reranker、VQAScore、Jev 决策模型；最接近的是视频 QA 的 localization probe，但其定位器是**单独训练的模块**且片段为 12–76 s；本文的扫描就是冻结的回答模型本身。
- **重听式音频模型**：LAT-Audio、Echo、Speaker-Reasoner 都需要微调/强化学习，时间戳由模型生成；ReListen 不训练、不转写、不生成时间戳。
- 同时注意到 ALM 的 yes/no 探针会幻觉“存在”（Kuan et al., 2024）并漏报重复事件（Dai et al., 2026），故对出现类问题额外做分数校准（Guo et al., 2017）。

## 5. 一句话评价
ReListen 用“冻结 ALM 自问自答式打分”这一极简而优雅的免训练范式，把小时级音频的证据定位变成了若干次 yes/no 前向读概率，在定位覆盖率、回答准确率与推理效率三方面同时超过转写检索与部分需训练的专用系统，是长音频 QA 中“让回答者自己去找证据”这一思路的有力验证。


---

## 13. Metadata-Conditioned Audio Transformers for Adaptive Respiratory Sound Classification

**作者**: George Kontogiannis, Pantelis Tzamalis, Sotiris Nikoletseas
**链接**: [2611.03769](https://arxiv.org/abs/2611.03769)
**分类**: Medical Audio Analysis / Respiratory Sound Classification | **关键词**: Respiratory Sound Classification, Audio Spectrogram Transformer (AST), Feature-wise Linear Modulation (FiLM), Metadata Conditioning, ICBHI, Factor Disentanglement, Soft Masks

## 核心痛点

呼吸音听诊分类（以 ICBHI 2017 为基准）长期受**采集异质性**困扰：录音设备（4 种数字听诊器，频响与噪声特性不同）、听诊部位（7 个解剖位置）、患者人口学属性（性别、年龄、BMI、呼吸周期时长）都会引入与病理无关的系统性分布偏移。作者对 ICBHI 做了首个系统的**元数据层面统计分析**（使用按患者聚类的 GEE 模型）：

- **设备偏置**：AKGC417L 占全部呼吸周期 63%、Crackle 标签 80% 以上；LittC2SE 仅出现在训练集，测试时构成完全域鸿沟；126 名患者中 122 人只用过一台设备，患者身份与设备高度混淆，模型可将设备频谱特征当作病理代理。
- **部位效应**：后侧/侧侧部位异常周期占 35–40%，气管部位 71% 为 Normal 且测试集中无 Both 事件；后侧部位出现 Crackle 的几率是气管的 2–4 倍（p_bonf<0.01），右后侧 Both 的 OR≈4.2；训练/测试划分间部位分布也发生漂移。
- **连续协变量**：异常周期比正常周期长 0.1–0.4 s（p<0.05）；年龄增大提升 Both 几率（OR=1.07），BMI 升高则更多 Normal、更少 Both。性别经校正后不显著，故被排除在条件向量之外，最终条件向量为 {年龄, BMI, 周期时长}。

现有工作要么**完全忽略元数据**，要么采用朴素融合：BTS 框架把元数据转成自由文本、用 CLAP 式多模态编码器融合，仅提升 +1.17%；对比学习类工作只把性别/年龄当预训练 pretext 任务，或把听诊器类型当作域做对抗训练/域泛化。共同缺陷是：需要昂贵的多模态编码器、只在表示学习阶段介入而不对推理过程做条件化、孤立处理单一因素、以及无法刻画**不同元数据源影响声学表示不同侧面**这一结构。FiLM 虽优雅，但其在 ViT/AST 上的适配尚属空白，更从未用于呼吸音或医学音频。

## 方法创新

所有方法共享 **AST-Base**（ImageNet + AudioSet 预训练）作为声学主干：log-mel 谱图切 16×16 patch，线性投影至 D 维，前接 [CLS] 与 [DIST] 特殊 token，最终表示为两者均值。元数据中设备索引 d、部位索引 s 映射为可学习嵌入，年龄/BMI/时长标准化为 3 维连续向量。在此之上提出四级递进的条件化机制族：

1. **Gated Residual Fusion (GRF)**：MLP 投影拼接后的元数据向量，以可学习标量 α 做门控残差加到最终表示上。属晚期融合，元数据无法影响中间特征提取，作为最简基线。
2. **FiLM**：共享编码器产生条件嵌入 h_m=g(m)，逐层生成缩放/偏移 γ_ℓ=1+W_ℓ^(γ)h_m、β_ℓ=W_ℓ^(β)h_m；调制施加于第二个 LayerNorm（FFN 前归一化）之后、FFN 之前，保持 Transformer 残差结构；以恒等为中心的参数化保证初始化时近似恒等调制，从而保留预训练特征。
3. **Token-Aware FiLM (TAFiLM)**：指出标准 FiLM 对所有 token 施加相同参数，忽视了 [CLS]/[DIST] 负责全局聚合、patch token 负责局部时频模式的角色差异。TAFiLM 由 h_m 经两组独立线性投影分别生成 (γ_cls, β_cls) 与 (γ_patch, β_patch)，使元数据可**独立调节全局聚合与局部时频提取**，代价仅为每层 FiLM 参数翻倍（额外 <0.4M）。
4. **Soft-Factorized FiLM (SoftFiLM)**：不再用单一混合嵌入，而是设备、部位、连续量三源各有专属编码器与 FiLM 生成器；为每源学习 logit 向量 ω^(k)∈R^D，经温度缩放 sigmoid 得到软掩码 w^(k)=σ(ω^(k)/τ)，τ 由余弦调度从 1.0 退火到 0.2（训练早期软、收敛时近二值）；掩码 logit 使用 10× 学习率并初始化为近似三等分、scale=0.5；最终 FiLM 参数为掩码加权和，从而把嵌入维度**分配给互不重叠的元数据专属子空间**。生成器用 gain=0.1 的小 Xavier 初始化以保证掩码从第一步就能获得非零梯度。正则项含**重叠惩罚**（防止多掩码争抢同一维度）与**覆盖惩罚**（保证所有维度被使用），与任务损失联合优化。

## 实验结果

- 在 ICBHI 官方 60-40% 划分下，**所有条件化策略均带来一致增益**。
- **SoftFiLM**：官方 4 类任务 **64.11%**（较基线 **+3.94%**），2 类任务 **72.40%**（**+2.32%**）。
- 2 类任务取得**新的 state-of-the-art**，4 类任务达到有竞争力的水平。
- 消融表明：**全参数微调**与**对所有层施加条件化**能最大化增益；定性分析证实学到的软掩码确实带来**可解释的因子解耦**。代码已开源。

## 一句话评价

本文把"按元数据调制"从朴素拼接升级为**结构化、因子解耦的 Transformer 内部特征调制**，用极轻量的 FiLM 变体（TAFiLM / SoftFiLM）在 ICBHI 上同时刷出新 SOTA 与可解释性，是医学音频领域元数据条件化的一次范式级补位。

---


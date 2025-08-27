# 电动力学 第2周作业

 Chasse_neige

本作业所有求和默认采用爱因斯坦求和约定。

### 1. 矢量分析

#### (a) 

$\epsilon_{ijk}$ 满足:
$$
\sum_{k=1}^{3} \epsilon_{ijk} \epsilon_{lmk} = \delta_{il} \delta_{jm} - \delta_{im} \delta_{jl}
$$

证明：

先除去所有 $\epsilon_{ijk} \epsilon_{lmk} = 0$ 的情况，仅考虑$i,j,k \text{和} l,m,k$ 互不相同的时侯。此时仅存在两种情况， $i=l$ 且 $j=m$ 和 $i=m \text{且} j=l$ 。显然，当 $i=l$ 且 $j=m$时，$\epsilon_{ijk} = \epsilon_{lmk}$ ；当 $i=m \text{且} j=l$ 时，$\epsilon_{ijk} = - \epsilon_{lmk}$。所以 $\epsilon_{ijk} \epsilon_{lmk} = \delta_{il} \delta_{jm} - \delta_{im} \delta_{jl}$，因为求和时仅有一个 $k$ 满足$i,j,k \text{和} l,m,k$ 互不相同的条件。

#### (b) 

用 $\delta_{ij}$ 和 $\epsilon_{ijk}$ 证明，

1.
$$
\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c}) \vec{b} - (\vec{a} \cdot \vec{b}) \vec{c}
$$
证明：
$$
\begin{aligned}
\vec{a} \times  (\vec{b} \times \vec{c}) &= \epsilon_{lkm} \epsilon_{ijk} a_{l} b_{i} c_{j} \vec{e_{m}} = \epsilon_{mlk} \epsilon_{ijk} a_{l} b_{i} c_{j} \vec{e_{m}} \\\\
&= (\delta_{mi} \delta_{lj} - \delta_{mj} \delta_{li}) a_{l} b_{i} c_{j} \vec{e_{m}} = a_{j} b_{i} c_{j} \vec{e_{i}} - a_{i} b_{i} c_{j} \vec{e_{m}} = (\vec{a} \cdot \vec{c}) \vec{b} - (\vec{a} \cdot \vec{b}) \vec{c}
\end{aligned}
$$
2.
$$
(\vec{a} \times \vec{b}) \times (\vec{c} \times \vec{d}) = [\vec{a} \cdot (\vec{b} \times \vec{d})] \vec{c} - [\vec{a} \cdot (\vec{b} \times \vec{c})] \vec{d} = [\vec{a} \cdot (\vec{c} \times \vec{d})] \vec{b} - [\vec{b} \cdot (\vec{c} \times \vec{d})] \vec{a}
$$
证明：
$$
\begin{aligned}
(\vec{a} \times \vec{b}) \times (\vec{c} \times \vec{d}) &= (\epsilon_{ijk} a_{i} b_{j} \vec{e_{k}}) \times (\epsilon_{lmn} c_{l} d_{m} \vec{e_{n}}) \\\\
&= \epsilon_{kns} \epsilon_{ijk} \epsilon_{lmn} a_{i} b_{j} c_{l} d_{m} \vec{e_{s}} = \epsilon_{ijk} (\delta_{sl} \delta_{km} - \delta_{sm} \delta_{kl}) a_{i} b_{j} c_{l} d_{m} \vec{e_{s}} \\\\
&= \epsilon_{ijk}  (a_{i} b_{j} c_{l} d_{k} \vec{e_{l}} - a_{i} b_{j} c_{k} d_{m} \vec{e_{m}}) = [\vec{a} \cdot (\vec{b} \times \vec{d})] \vec{c} - [\vec{a} \cdot (\vec{b} \times \vec{c})] \vec{d} \\\\
\epsilon_{kns} \epsilon_{ijk} \epsilon_{lmn} a_{i} b_{j} c_{l} d_{m} \vec{e_{s}} &= (\delta_{ni} \delta_{sj} - \delta_{nj} \delta_{si}) \epsilon_{lmn} a_{i} b_{j} c_{l} d_{m} \vec{e_{s}} \\\\
&= \epsilon_{lmn} (a_{n} b_{s} c_{l} d_{m} \vec{e_{s}} - a_{s} b_{n} c_{l} d_{m} \vec{e_{s}}) = [\vec{a} \cdot (\vec{c} \times \vec{d})] \vec{b} - [\vec{b} \cdot (\vec{c} \times \vec{d})] \vec{a}
\end{aligned}
$$

#### (c) 思考选做题

试证明

i. 一阶张量除零矢量外，都不是各向同性的

证明：矢量$\vec{A} = \begin{pmatrix} A_{1}, A_{2}, \cdots, A_{n} \end{pmatrix}$ 各向同性意味着对所有方向的单位矢量而言，$\vec{A}$ 在它们上的投影值相同。
$$
\vec{A} \cdot \hat{e} = |\vec{A}| \cos<\vec{A}, \hat{e}> = const
$$

$$
\therefore \,\, |\vec{A}| = 0
$$

ii. 二阶张量中的各向同性的张量必为 $\lambda \delta_{ij}$

证明：设二阶张量 $T_{ij} $ 满足 $ Q_{ki} Q_{lj} T_{ij} = T_{kl} $ 对所有正交阵 $Q $均成立。取$Q$为绕 $z$ 轴的旋转阵，代入条件可得：
$$
\begin{aligned}
\begin{bmatrix} \cos \theta & \sin \theta \\\\
- \sin \theta &  \cos \theta \end{bmatrix} \begin{bmatrix} T_{11} & T_{12} \\\\
T_{21} & T_{22} \end{bmatrix} \begin{bmatrix} \cos \theta & - \sin \theta \\\\
\sin \theta & \cos \theta \end{bmatrix}  = \begin{bmatrix} T_{11} & T_{12} \\\\
T_{21} & T_{22} \end{bmatrix}
\end{aligned}
$$

$$
\begin{aligned}
\therefore \,\, \begin{cases} T_{11} &= T_{12} \\\\
T_{22} &= T_{21} = 0 \end{cases}
\end{aligned}
$$
同理，可以得到
$$
\begin{aligned}
\begin{cases} T_{11} &= T_{33} \\\\
T_{13} &= T_{31} = 0 \\\\
T_{22} &= T_{33} \\\\
T_{23} &= T_{32} = 0 \end{cases}
\end{aligned}
$$
即$T_{ij} = \lambda \delta_{ij}$

iii. 三阶张量中的各向同性的张量必为 $\lambda \epsilon_{ijk}$

证明：此时用上面的方法去凑变换消去自由度太繁琐，尝试再换一种方法：

考虑坐标架的一个无穷小转动 $\delta \vec{\theta}$ 则任意三阶张量在转动后可以表达为：
$$
T_{ijk}^{'} = T_{ijk} + \delta \theta_{l} (\epsilon_{lim}T_{mjk} + \epsilon_{ljm} T_{imk} + \epsilon_{lkm} T_{ijm})
$$
要求转动前后分量相等，所以
$$
\epsilon_{lim}T_{mjk} + \epsilon_{ljm} T_{imk} + \epsilon_{lkm} T_{ijm} = 0
$$
假设 $T $是完全反对称的，即满足：
$$
T_{ijk} = A \epsilon_{ijk},
$$
将 $ T_{ijk} = A \epsilon_{ijk} $ 代入原方程：
$$
\epsilon_{lim} (A \epsilon_{mjk}) + \epsilon_{ljm} (A \epsilon_{imk}) + \epsilon_{lkm} (A \epsilon_{ijm}) = 0.
$$
提取常数 \( A \)：
$$
A \left( \epsilon_{lim} \epsilon_{mjk} + \epsilon_{ljm} \epsilon_{imk} + \epsilon_{lkm} \epsilon_{ijm} \right) = 0.
$$
将三项相加：
$$
\begin{aligned}
& (\delta_{lj}\delta_{ik} - \delta_{lk}\delta_{ij}) \\\\
+ & (-\delta_{li}\delta_{jk} + \delta_{lk}\delta_{ij}) \\\\
+ & (\delta_{li}\delta_{kj} - \delta_{lj}\delta_{ki}) \\\\
= & \delta_{lj}\delta_{ik} - \delta_{lk}\delta_{ij} -\delta_{li}\delta_{jk} + \delta_{lk}\delta_{ij} + \delta_{li}\delta_{kj} - \delta_{lj}\delta_{ki} = 0
\end{aligned}
$$
对于非完全反对称的一般 $T$ ，对其做对称反对称分解，其中的对称部分设为$S_{ijk}$

带入：
$$
\epsilon_{lim} S_{mjk} + \epsilon_{ljm} S_{imk} + \epsilon_{lkm} S_{ijm} = 0
$$

$$
\epsilon_{lnm} (\epsilon_{lim} S_{mjk} + \epsilon_{ljm} S_{imk} + \epsilon_{lkm} S_{ijm}) = 0
$$

$$
2(\delta_{ni} S_{mjk} + \delta_{nj} S_{imk} + \delta_{nk} S_{ijm}) = 0
$$

当 $n = i$ 时：
$$
\delta_{ni} S_{mjk} + \delta_{nj} S_{imk} + \delta_{nk} S_{ijm} = S_{mjk} + \delta_{ij} S_{imk} + \delta_{ik} S_{ijm} =  S_{mjk} + S_{jmk} + S_{kjm} = 
3 S_{mjk}
$$


当$n = j$ 和$n = k$ 时同理。
$$
\therefore \,\, \delta_{ni} S_{mjk} + \delta_{nj} S_{imk} + \delta_{nk} S_{ijm} = 
3 (S_{mjk} + S_{imk} + S_{ijm}) = 0
$$

$$
S_{ijk} = 0
$$

即不能存在对称分量。

iv. 四阶张量中的各向同性的张量必为 $\lambda \delta_{ij} \delta_{kl} + \alpha \delta_{ik} \delta_{jl} + \beta \delta_{il} \delta_{jk}$

对于四阶各向同性张量，推广形式为：  

$\epsilon_{mis}\,a_{sjkl} + \epsilon_{mjs}\,a_{iskl} + \epsilon_{mks}\,a_{ijsl} + \epsilon_{mls}\,a_{ijks} = 0$  

分别乘以$\epsilon_{mit}$、$\epsilon_{mjt}$、$\epsilon_{mkt}$和$\epsilon_{mlt}$，并令$t=i$、$t=j$、$t=k$和$t=l$，得到：  

$2\,a_{ijkl} + a_{jikl} + a_{kjil} + a_{ljki} = a_{sskl}\,\delta_{ij} + a_{sjsl}\,\delta_{ik} + a_{sjks}\,\delta_{il}$ 
$2\,a_{ijkl} + a_{jikl} + a_{ikjl} + a_{iljk} = a_{sskl}\,\delta_{ij} + a_{isks}\,\delta_{jl} + a_{issl}\,\delta_{jk}$ 
$2\,a_{ijkl} + a_{kjil} + a_{ikjl} + a_{ijlk} = a_{ijss}\,\delta_{kl} + a_{sjsl}\,\delta_{ik} + a_{issl}\,\delta_{jk}$ 
$2\,a_{ijkl} + a_{ljki} + a_{ilkj} + a_{ijlk} = a_{ijss}\,\delta_{kl} + a_{isks}\,\delta_{jl} + a_{sjks}\,\delta_{il}$  

由于$a_{sskl}$、$a_{sjsl}$和$a_{sjks}$是二阶各向同性张量，我们有：  

$a_{sskl} = \lambda\,\delta_{kl}$
$a_{sjsl} = \mu\,\delta_{jl}$ 
$a_{sjks} = \nu\,\delta_{jk}$  

因此，  

$a_{ijkl} = \alpha\,\delta_{ij}\,\delta_{kl} + \beta\,\delta_{ik}\,\delta_{jl} + \gamma\,\delta_{il}\,\delta_{jk}$  

其中：  

$\alpha = \frac{4\lambda - \mu - \nu}{10}$ 
$\beta = \frac{4\mu - \nu - \lambda}{10}$ 
$\gamma = \frac{4\nu - \lambda - \mu}{10}$  

### 2. 场论

#### 1.1  

根据算符∇的微分性与矢量性，推导下列公式：
$$
\nabla(\mathbf{A} \cdot \mathbf{B}) = \mathbf{B} \times (\nabla \times \mathbf{A}) + (\mathbf{B} \cdot \nabla) \mathbf{A} + \mathbf{A} \times (\nabla \times \mathbf{B}) + (\mathbf{A} \cdot \nabla) \mathbf{B}
$$

$$
\mathbf{A} \times (\nabla \times \mathbf{A}) = \frac{1}{2} \nabla A^2 - (\mathbf{A} \cdot \nabla) \mathbf{A}
$$

证明：第一个式子从右推左
$$
\mathbf{B} \times (\nabla \times \mathbf{A}) + \mathbf{A} \times (\nabla \times \mathbf{B}) = 
\nabla_{A} (\mathbf{A} \cdot \mathbf{B}) + \nabla_{B} (\mathbf{A} \cdot \mathbf{B}) - (\mathbf{B} \cdot \nabla) \mathbf{A} - (\mathbf{A} \cdot \nabla) \mathbf{B}
$$
其中 $\nabla$ 的下标表示仅对该分量做微分。
$$
\begin{aligned}
&\therefore \,\, \mathbf{B} \times (\nabla \times \mathbf{A}) + (\mathbf{B} \cdot \nabla) \mathbf{A} + \mathbf{A} \times (\nabla \times \mathbf{B}) + (\mathbf{A} \cdot \nabla) \mathbf{B} \\\\
&= \nabla_{A} (\mathbf{A} \cdot \mathbf{B}) + \nabla_{B} (\mathbf{A} \cdot \mathbf{B}) - (\mathbf{B} \cdot \nabla) \mathbf{A} - (\mathbf{A} \cdot \nabla) \mathbf{B} + (\mathbf{B} \cdot \nabla) \mathbf{A} + (\mathbf{A} \cdot \nabla) \mathbf{B} \\\\
&= \nabla_{A} (\mathbf{A} \cdot \mathbf{B}) + \nabla_{B} (\mathbf{A} \cdot \mathbf{B}) = \nabla (\mathbf{A} \cdot \mathbf{B})
\end{aligned}
$$
第二个式子从左推右，为了区分，给两个A加上下标，但是它们本质上是一样的。
$$
\mathbf{A_{1}} \times (\nabla \times \mathbf{A_{2}}) =  \nabla_{\mathbf{A_{2}}} (\mathbf{A_{1}} \cdot \mathbf{A_{2}}) - (\mathbf{A_{1}} \cdot \nabla) \mathbf{A_{2}}
$$

$$
\because \,\, \nabla_{\mathbf{A_{2}}} (\mathbf{A_{1}} \cdot \mathbf{A_{2}}) = \nabla_{\mathbf{A_{1}}} (\mathbf{A_{1}} \cdot \mathbf{A_{2}})
$$

$$
\therefore \,\, \nabla_{\mathbf{A_{2}}} (\mathbf{A_{1}} \cdot \mathbf{A_{2}}) = \frac{1}{2}  (\nabla_{\mathbf{A_{1}}} (\mathbf{A_{1}} \cdot \mathbf{A_{2}}) + \nabla_{\mathbf{A_{2}}} (\mathbf{A_{1}} \cdot \mathbf{A_{2}})) = \frac{1}{2} \nabla A^2
$$

$$
\therefore \,\, \mathbf{A} \times (\nabla \times \mathbf{A}) = \frac{1}{2} \nabla A^2 - (\mathbf{A} \cdot \nabla) \mathbf{A}
$$

#### 1.3 

设 $r=\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}$ 为源点 $x'$ 到场点 $x$ 的距离，$r$ 的方向规定为从源点指向场点。

(1) 证明下列结果，并体会对源变数求微商 $\left(\nabla'=\mathbf{e}_x \frac{\partial}{\partial x'}+\mathbf{e}_y \frac{\partial}{\partial y'}+\mathbf{e}_z \frac{\partial}{\partial z'}\right)$ 与对场变数求微商 $\left(\nabla=\mathbf{e}_x \frac{\partial}{\partial x}+\mathbf{e}_y \frac{\partial}{\partial y}+\mathbf{e}_z \frac{\partial}{\partial z}\right)$ 的关系：

$$
\begin{aligned}
\nabla r &= -\nabla' r = \frac{\mathbf{r}}{r} \\\\
\nabla \frac{1}{r} &= -\nabla' \frac{1}{r} = -\frac{\mathbf{r}}{r^3} \\\\
\nabla \times \frac{\mathbf{r}}{r^3} &= 0 \\\\
\nabla \cdot \frac{\mathbf{r}}{r^3} &= -\nabla' \cdot \frac{\mathbf{r}}{r^3} = 0 \quad (r \neq 0)
\end{aligned}
$$
（最后一式在 $r=0$ 点不成立，见第二章 §5）。

证明：将 $r$ 表示为直角坐标下的分量式  $\vec{r} = (x-x^{'}) \vec{e_{x}} + (y - y^{'}) \vec{e_{y}} + (z - z^{'}) \vec{e_{z}}$ 和 $r=\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}$  
$$
\nabla r = \partial_{i} \sqrt{(x_{i} - x_{i}^{'})^{2}} \vec{e_{i}} = \frac{(x_{i} - x_{i}^{'}) \vec{e_{i}}}{\sqrt{(x_{i} - x_{i}^{'})^{2}}} = \frac{\vec{r}}{r}
$$

$$
\nabla^{'} r = \partial_{i}^{'} \sqrt{(x_{i} - x_{i}^{'})^{2}} \vec{e_{i}} = - \frac{(x_{i} - x_{i}^{'}) \vec{e_{i}}}{\sqrt{(x_{i} - x_{i}^{'})^{2}}} = - \frac{\vec{r}}{r}
$$

$$
\nabla \frac{1}{r} = \partial_{i} \frac{1}{\sqrt{(x_{i} - x_{i}^{'})^{2}}} \vec{e_{i}} = - \frac{(x_{i} - x_{i}^{'}) \vec{e_{i}}}{\sqrt{(x_{i} - x_{i}^{'})^{2}}^{3}} = - \frac{\vec{r}}{r^{3}}
$$

$$
\nabla^{'} \frac{1}{r} = \partial_{i}^{'} \frac{1}{\sqrt{(x_{i} - x_{i}^{'})^{2}}} \vec{e_{i}} = \frac{(x_{i} - x_{i}^{'}) \vec{e_{i}}}{\sqrt{(x_{i} - x_{i}^{'})^{2}}^{3}} = \frac{\vec{r}}{r^{3}}
$$

$$
\nabla \times \frac{\vec{r}}{r^{3}} =  - \nabla \times (\nabla \frac{1}{r}) = 0
$$

$$
\nabla \cdot \frac{\vec{r}}{r^3} = -\nabla' \cdot \frac{\vec{r}}{r^3} = \frac{3}{r^{3}} - 3 \frac{\vec{r}}{r^{5}} \cdot \vec{r} = 0 \,\, (r \neq 0 )
$$



(2) 求 $\nabla \cdot \mathbf{r}$，$\nabla \times \mathbf{r}$，$(\mathbf{a} \cdot \nabla) \mathbf{r}$，$\nabla (\mathbf{a} \cdot \mathbf{r})$，$\nabla \cdot [\mathbf{E}_0 \sin (\mathbf{k} \cdot \mathbf{r})]$ 及 $\nabla \times [\mathbf{E}_0 \sin (\mathbf{k} \cdot \mathbf{r})]$，其中 $\mathbf{a}$、$\mathbf{k}$ 及 $\mathbf{E}_0$ 均为常矢量。
$$
\nabla \cdot \vec{r} = 3
$$

$$
\nabla \times \vec{r} = 0
$$

$$
(\vec{a} \cdot \nabla)\vec{r} = \vec{a} \cdot \overset{\leftrightarrow}{I} = \vec{a}
$$

$$
\nabla (\vec{a} \cdot \vec{r}) = (\vec{a} \cdot \nabla) \vec{r} + (\vec{r} \cdot \nabla) \vec{a} + \vec{a} \times (\nabla \times \vec{r}) + \vec{r} \times (\nabla \times \vec{a}) = \vec{a} + 0 + 0 + 0 = \vec{a} 
$$

$$
\nabla \cdot [\mathbf{E}_0 \sin (\mathbf{k} \cdot \mathbf{r})] = (\nabla \sin(\vec{k} \cdot \vec{r})) \cdot \vec{E_{0}} + \sin(\vec{k} \cdot \vec{r}) \nabla \cdot \vec{E_{0}} = \cos (\vec{k} \cdot \vec{r}) \,\, \nabla(\vec{k} \cdot \vec{r}) \cdot \vec{E_{0}} + 0 = \cos (\vec{k} \cdot \vec{r}) (\vec{k} \cdot \vec{E_{0}})
$$

$$
\nabla \times [\mathbf{E}_0 \sin (\mathbf{k} \cdot \mathbf{r})] = (\nabla \sin(\vec{k} \cdot \vec{r})) \times \vec{E_{0}} + \sin(\vec{k} \cdot \vec{r}) \nabla \times \vec{E_{0}} = \cos (\vec{k} \cdot \vec{r}) \vec{k} \times \vec{E_{0}} + 0 = \cos (\vec{k} \cdot \vec{r}) (\vec{k} \times \vec{E_{0}})
$$



#### 1.6

若 $\mathbf{m}$ 是常矢量，证明除 $R=0$ 点以外，矢量 $\mathbf{A} = \frac{\mathbf{m} \times \mathbf{R}}{R^3}$ 的旋度等于标量 $\varphi = \frac{\mathbf{m} \cdot \mathbf{R}}{R^3}$ 的梯度的负值，即
$$
\nabla \times \mathbf{A} = -\nabla \varphi \qquad (R \neq 0)
$$

其中 $\mathbf{R}$ 为坐标原点到场点的距离，方向由原点指向场点。

证明：
$$
\begin{aligned}
\nabla \times \vec{A} &= - \nabla \times (\vec{m} \times \nabla \frac{1}{r}) =  - (\vec{m} \nabla^{2} \frac{1}{r} - \vec{m} \cdot \nabla \nabla \frac{1}{r} + (\nabla \frac{1}{r}) \cdot (\nabla \vec{m}) - (\nabla \frac{1}{r})(\nabla \cdot \vec{m})) \\\\
&= -(0 - \frac{3 (\vec{m} \cdot \vec{r}) \vec{r}}{r^{5}} + \frac{\vec{m}}{r^{3}} + 0 - 0) = - \frac{\vec{m}}{r^{3}} + \frac{3(\vec{m} \cdot \vec{r})}{r^{5}} \qquad (R \neq 0)
\end{aligned}
$$

$$
\begin{aligned}
- \nabla \varphi &= \nabla (\vec{m} \cdot \nabla \frac{1}{r}) = \vec{m} \times (\nabla \times \nabla \frac{1}{r}) + \nabla \frac{1}{r} \times (\nabla \times \vec{m}) + (\vec{m} \cdot \nabla) \nabla \frac{1}{r} + (\nabla \frac{1}{r} \cdot \nabla) \vec{m} \\\\
&= 0 + 0 + \vec{m} \cdot \nabla \nabla \frac{1}{r} + 0 = - \frac{\vec{m}}{r^{3}} + \frac{3(\vec{m} \cdot \vec{r})}{r^{5}} \qquad (R \neq 0)
\end{aligned}
$$



#### 思考题

$\nabla \cdot \vec{A} > 0$，$\nabla \cdot \vec{A} = 0$，$\nabla \cdot \vec{A} < 0$ 在直观图像上有什么差别？$\nabla \times \vec{A} > 0$，$\nabla \times \vec{A} = 0$，$\nabla \times \vec{A} < 0$ 呢？

$\nabla \cdot \vec{A} > 0$ 在直观上表示为矢量场$\vec{A}$ 在图像上从该点向四周“发射”，总体作用向外的；

$\nabla \cdot \vec{A} = 0$ 在直观上表现为该点的矢量场在打转或者干脆没有，进出相互抵消，总通量为0；

$\nabla \cdot \vec{A} < 0$ 在直观上表现为该点的矢量场向内汇聚，总体作用向内。

$\nabla \times \vec{A} = 0$ 表现为该点的矢量场沿着径向或者为0。

我不知道$\nabla \times \vec{A} > 0$ $\nabla \times \vec{A} < 0$是什么意思。如果是针对一个特定方向定义的话那么代表着二者旋转方向相反。

### 3. $\delta$ 函数

#### 2.14

画出函数 $\frac{\mathrm{d}\delta(x)}{\mathrm{d}x}$ 的图，说明 $\rho = -(\mathbf{p} \cdot \nabla)\delta(\mathbf{x})$ 是一个位于原点的偶极子的电荷密度。

函数  $\frac{\mathrm{d}\delta(x)}{\mathrm{d}x}$ 的图：

![image-20250228141027350](image-20250228141027350.png)

注：因为严格的图像画出后函数曲线和坐标轴不太好分辨，此图是利用高斯函数在极限情况下的一个近似图像，可以体现函数的部分性质。 

证明：
$$
\begin{aligned}
\int \rho \vec{r} \, d \tau &= \int  -(\vec{p} \cdot \nabla)\delta(\vec{r}) \, \vec{r} \, d \tau = \int ( (\nabla \cdot \vec{p}) \delta(\vec{r}) - \nabla \cdot (\delta(\vec{r}) \vec{p})) \vec{r} d \tau \\\\
&= - \int \nabla \cdot (\delta(\vec{r}) \vec{p} \vec{r}) d \tau + \int \delta(\vec{r}) \vec{p} \cdot \nabla \vec{r} \, d \tau = \int \delta(\vec{r}) \vec{p} \, d \tau = \vec{p}
\end{aligned}
$$


#### 思考题：

(1) $\delta(ax) = \frac{1}{|a|}\delta(x), a > 0$. （若 $a < 0$，结果如何？）

证明：
$$
\begin{aligned}
\delta(ax) \, d (ax) &=  \delta (x) \, dx \\\\
\therefore \,\, \delta(ax) &= \frac{1}{|a|}\delta(x), a > 0
\end{aligned}
$$
当 $a < 0$ 时，
$$
\delta(ax) = - \frac{1}{|a|}\delta(x), a > 0
$$


(2) $x\delta(x) = 0$.
$$
\because \,\, f(x) \delta(x-x_{0}) = f(x_{0})
$$

$$
\therefore \,\, x \delta (x-0) = 0
$$


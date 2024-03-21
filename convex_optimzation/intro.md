#　非線性優化
在介紹線性優化前，先來看看優化本身的架構，這個概念跟P屬於NP有87%像。

概念上線性優化可以做的，非線性優化都可以做，反過來不行。

但可以做的，非線性不一定錯的好。

問題的一般性描述：

$$x=(x^{(1)},......x^{(n)})^T \in \mathbb{R^n}$$

x是n維的向量

$$minf_0(x) \quad s.t. \quad f_j(x)=0$$

左邊是主問題 $f_0$，右邊是對應的約束條件

意思是把死小孩關到房間裡面，你才能去求解他在幹麻

如果有一連串的約束條件可以把它寫進一個向量

$$f(x)=(f_1(x),...,fm(x))^T$$

x的可行解區域Q可以寫成

$$\mathscr{F}=\{x \in Q | f_i(x)<=0\}$$

## 線性規劃與二次規劃

線性約束問題是仿射的

也就是它應該可以寫成線性的內積形式

$$f_i(x)=\sum_{i=1}^{n}a_j^{(i)}x_j^{(i)}+b_j=<a_j,x>+b_j$$

如果 $f_0$ 也是仿射的，那就是線性規劃

如果 $f_0$ 是二次的，那就是二次規劃問題

如果 $f_i$ 是二次的 就是二次約束

## 術語
可行：問題可行代表$\mathscr{F}$不是空集合

嚴格可行(Slater 條件)：如果存在 $x \in Q$ 且符合約束條件 

全局解：對於 $x^* \in \mathscr{F} \quad \forall x \in \mathscr{F} \quad f_0(x^*)<=f_0(x)$ 

局部解：對於 $x^* \in \mathscr{F} \quad \exist \mathscr{F_{x'}} \in \mathscr{F}\quad \forall x' \in \mathscr{F_x'} \quad f_0(x^*)<=f_0(x')$

基本上有些問題是很難找全局解的，所以只能做問題切面，想辦法做近似

從子集中摳出解來，會根據做任務的資源與系統的可靠性來決定要怎做

# 通用迭代算法

在解一個問題 $\mathscr{P}$，其中包含問題內容的陳述，函數們的表達 $\sum$， 透過oracle $\mathscr{O}$互動更新狀態 $\mathscr{S}$，並利用算法 $\mathscr{M}$ 直到符合停止準則 $\mathscr{stop}$

輸入：初始點$x_0$和精度$\epsilon$>0
初始化：令$k=0$, $\mathscr{S}=\{\}$
1. 初始點$x_k$調用 $\mathscr{O}$ 
2. 更新信息集 $\mathscr{S_k} \cup(x_k,\mathscr{O}(x_k))$
3. 利用算法 $\mathscr{M}$ 再與 $\mathscr{S_k}$ 互動 生成新點 $x_k+1$
4. 直到符合停止準則$\mathscr{stop}$

## 複雜度
衡量一個演算過程有多複雜可以從以下兩個觀點
解析複雜度：
調用多少次oracle才能達到精度$\epsilon$
算術複雜度：
調用多少次的oracle跟算法$\mathscr{M}$才能達到精度$\epsilon$
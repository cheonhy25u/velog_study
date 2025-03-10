<h2 id="description">Description</h2>
<hr />
<p>이 문제는 사용자에게 문자열 입력을 받아 정해진 방법으로 입력값을 검증하여 correct 또는 wrong을 출력하는 프로그램이 주어집니다.</p>
<p>해당 바이너리를 분석하여 correct를 출력하는 입력값을 알아내세요.</p>
<h2 id="solution">Solution</h2>
<hr />
<p>IDA로 주어진 바이너리를 열어 보면 아래와 같은 그래프 뷰를 확인할 수 있다. rev-basic 지금까지 나왔던 것들과 동일하게 분기가 나뉘기 전에 마지막으로 호출되는 함수 sub_140001000을 들어가 확인해 보는 방식으로 풀이를 전개한다. 
<img alt="" src="https://velog.velcdn.com/images/hy25u/post/9e6f59f7-a182-4daf-9b24-0cb5a798beed/image.png" /></p>
<pre><code>__int64 __fastcall sub_140001000(__int64 a1)
{
  int i; // [rsp+0h] [rbp-18h]

  for ( i = 0; (unsigned __int64)i &lt; 0x18; ++i )
  {
    if ( byte_140003000[i] != (i ^ *(unsigned __int8 *)(a1 + i)) + 2 * i )
      return 0LL;
  }
  return 1LL;
}</code></pre><p>sub_140001000 함수에 들어가 decompile을 하면 위와 같은 pseudocode가 나온다. 확인해 보면 반복문을 돌면서 byte_140003000[i]와 우리가 입력하는 값이 인자로 전해진 a1이 연산을 통해 비교가 되고 있는 것을 알 수 있다. 연산 과정을 구체적으로 살펴보자. </p>
<p>단순하게 표현하자면 byte_140003000[i](이하 비교대상)= (i ^ 입력값)+2*i이 되어야 한다. 
그렇다면 입력값만 한 쪽에 두고 다 이항을 해 보면 비교대상 - 2 * i = i ^ 입력값이 되고 이는 다시 말해 (비교대상 - 2*i)^i = 입력값 과 같은 의미이다. 
비교대상 값을 확인하고 코드를 작성하여 입력값에 무엇이 들어가야 하는지 확인해 보자. </p>
<p><img alt="" src="https://velog.velcdn.com/images/hy25u/post/84c5686b-265d-4b81-bb43-85fa6aac05ed/image.png" />
비교대상을 더블클릭하여 들어가면 이렇게 IDA 기본 뷰로 확인할 수 있는데 편의상 Hex View 를 통해 확인하는 게 더 좋을 것 같다. 
<img alt="" src="https://velog.velcdn.com/images/hy25u/post/52f2bff6-76ae-40ef-80ab-709e0d7d2355/image.png" />
여기에 있는 0x18 개의 값들이 우리가 연산해야 할 값이다. </p>
<p>긁어와서 일일히 포맷팅하기보다는 아래 코드를 이용해서 배열의 형태로 넣을 수 있게 실행했다.</p>
<pre><code class="language-hex_string">hex_value = [f&quot;0x{val}&quot; for val in hex_string.split()]
result = &quot;, &quot;.join(hex_value)
print(result)
</code></pre>
<p>이후 얻은 값들을 배열 형태로 이쁘게 감싸주고 역연산 코드를 작성해서 플래그를 얻을 수 있다!</p>
<pre><code>cmp_list = [0x49, 0x60, 0x67, 0x74, 0x63, 0x67, 0x42, 0x66, 0x80, 0x78, 0x69, 0x69, 0x7B, 0x99, 0x6D, 0x88, 0x68, 0x94, 0x9F, 0x8D, 0x4D, 0xA5, 0x9D, 0x45]

flag = &quot;&quot;
for i in range(len(cmp_list)):
    key = (cmp_list[i] - 2 * i) ^ i
    flag += chr(key)

print(flag)</code></pre><blockquote>
<p>DH{I_am_X0_xo_Xor_eXcit1ng}</p>
</blockquote>
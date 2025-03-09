<h2 id="description">Description</h2>
<hr />
<p>이 문제는 사용자에게 문자열 입력을 받아 정해진 방법으로 입력값을 검증하여 correct 또는 wrong을 출력하는 프로그램이 주어집니다.</p>
<p>해당 바이너리를 분석하여 correct를 출력하는 입력값을 알아내세요.</p>
<h2 id="solution">Solution</h2>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/hy25u/post/c60b3f46-e29a-47b4-a413-4e834ca2fc9c/image.png" /></p>
<p>main함수의 그래프 뷰는 rev-basic-0, 1에서 봤던 것과 비슷하다. 여기서도 마찬가지로 분기 나눠지기 전에 호출되는 함수인 sub_140001000을 중점적으로 분석하여 문제를 풀면 될 것이다. </p>
<pre><code>__int64 __fastcall sub_140001000(__int64 a1)
{
  int i; // [rsp+0h] [rbp-18h]

  for ( i = 0; (unsigned __int64)i &lt; 0x12; ++i )
  {
    if ( *(_DWORD *)&amp;aC[4 * i] != *(unsigned __int8 *)(a1 + i) )
      return 0LL;
  }
  return 1LL;
}</code></pre><p>sub 140001000을 디컴파일하면 위와 같은 코드가 나온다. aC[4*i]와 a1 + i가 같아야 한다. 여기서 a1+i는 우리가 입력하는 문자열 중 인덱싱하여 하나하나 도는 것으로 보면 된다. 
저 aC 배열이 뭔가 싶어 decompile 코드에서 aC를 더블클릭해서 이동해 보니 Comp4re_the_arr4y라는 문자열이 저장되어 있는 배열이었다. 이 값을 입력하면 우리는 Correct를 출력 받을 수 있다! 
<img alt="" src="https://velog.velcdn.com/images/hy25u/post/d05d8dd7-d16e-41c4-908a-426810a07954/image.png" /></p>
<blockquote>
<p>DH{Comp4re_the_arr4y}</p>
</blockquote>
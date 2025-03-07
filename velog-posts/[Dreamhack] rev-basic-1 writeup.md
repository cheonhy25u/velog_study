<p><img alt="" src="https://velog.velcdn.com/images/hy25u/post/68b7e304-7eba-4b0f-8e07-9816b30a4fb3/image.png" /></p>
<h2 id="description">Description</h2>
<hr />
<p>이 문제는 사용자에게 문자열 입력을 받아 정해진 방법으로 입력값을 검증하여 correct 또는 wrong을 출력하는 프로그램이 주어집니다.</p>
<p>해당 바이너리를 분석하여 correct를 출력하는 입력값을 알아내세요.</p>
<h2 id="solution">Solution</h2>
<hr />
<p>main함수의 그래프 뷰는 rev-basic-0에서 보이는 것과 비슷하다. 똑같은 방식으로 분기 결정을 하는 함수 내로 들어가 보면 이렇게 많은 조건문들을 거쳐서 correct를 출력하는 형식이라는 것을 알 수 있다. 
<img alt="" src="https://velog.velcdn.com/images/hy25u/post/cafe737c-933e-4934-be9a-75e4db6ce92a/image.png" />
조건문이 너무 많기 때문에 디컴파일 해서 일단 들어가 보면 C 형태로 psudo code가 작성되어 있는 것을 볼 수 있다. </p>
<pre><code>_BOOL8 __fastcall sub_140001000(_BYTE *a1)
{
  if ( *a1 != 67 )
    return 0LL;
  if ( a1[1] != 111 )
    return 0LL;
  if ( a1[2] != 109 )
    return 0LL;
  if ( a1[3] != 112 )
    return 0LL;
  if ( a1[4] != 97 )
    return 0LL;
  if ( a1[5] != 114 )
    return 0LL;
  if ( a1[6] != 51 )
    return 0LL;
  if ( a1[7] != 95 )
    return 0LL;
  if ( a1[8] != 116 )
    return 0LL;
  if ( a1[9] != 104 )
    return 0LL;
  if ( a1[10] != 101 )
    return 0LL;
  if ( a1[11] != 95 )
    return 0LL;
  if ( a1[12] != 99 )
    return 0LL;
  if ( a1[13] != 104 )
    return 0LL;
  if ( a1[14] != 52 )
    return 0LL;
  if ( a1[15] != 114 )
    return 0LL;
  if ( a1[16] != 97 )
    return 0LL;
  if ( a1[17] != 99 )
    return 0LL;
  if ( a1[18] != 116 )
    return 0LL;
  if ( a1[19] != 51 )
    return 0LL;
  if ( a1[20] == 114 )
    return a1[21] == 0;
  return 0LL;
}</code></pre><p>a1 배열에는 우리가 입력하는 값이 들어가고 67 111 등의 숫자는 ascii 코드에서의 숫자값이다. 각각의 숫자값을 선택한 뒤 단축키 r을 눌러 주면 ascii text로 변환할 수 있다. </p>
<pre><code>_BOOL8 __fastcall sub_140001000(_BYTE *a1)
{
  if ( *a1 != 'C' )
    return 0LL;
  if ( a1[1] != 'o' )
    return 0LL;
  if ( a1[2] != 'm' )
    return 0LL;
  if ( a1[3] != 'p' )
    return 0LL;
  if ( a1[4] != 'a' )
    return 0LL;
  if ( a1[5] != 'r' )
    return 0LL;
  if ( a1[6] != '3' )
    return 0LL;
  if ( a1[7] != '_' )
    return 0LL;
  if ( a1[8] != 't' )
    return 0LL;
  if ( a1[9] != 'h' )
    return 0LL;
  if ( a1[10] != 'e' )
    return 0LL;
  if ( a1[11] != '_' )
    return 0LL;
  if ( a1[12] != 'c' )
    return 0LL;
  if ( a1[13] != 'h' )
    return 0LL;
  if ( a1[14] != '4' )
    return 0LL;
  if ( a1[15] != 'r' )
    return 0LL;
  if ( a1[16] != 'a' )
    return 0LL;
  if ( a1[17] != 'c' )
    return 0LL;
  if ( a1[18] != 't' )
    return 0LL;
  if ( a1[19] != '3' )
    return 0LL;
  if ( a1[20] == 'r' )
    return a1[21] == 0;
  return 0LL;
}</code></pre><blockquote>
<p>DH{Compar3_the_ch4ract3r}</p>
</blockquote>
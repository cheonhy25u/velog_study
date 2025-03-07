<h2 id="description">Description</h2>
<hr />
<p>이 문제는 사용자에게 문자열 입력을 받아 정해진 방법으로 입력값을 검증하여 correct 또는 wrong을 출력하는 프로그램이 주어집니다.</p>
<p>해당 바이너리를 분석하여 correct를 출력하는 입력값을 찾으세요!</p>
<h2 id="solution">Solution</h2>
<hr />
<p align="center"><img src="https://velog.velcdn.com/images/hy25u/post/3c5dbc32-6ddd-41dc-9f2c-a429b0ec29b2/image.png" width="70%" /></p>

<p>주어진 파일을 IDA를 통해 확인하면 위와 같은 그래프 뷰를 확인할 수 있다. (참고 : 그래프 뷰, 텍스트 뷰는 스페이스바를 통해 변환 가능함)</p>
<p>어셈블리 코드를 확인해 보면 Input : 으로 사용자 입력을 받은 후 sub_140001000을 통해 나온 결과값을 바탕으로 아래 두 분기로 나누어진다. 여기서 우리가 확인해야 하는 함수는 sub_140001000이 되는 것이다. 더블 클릭으로 해당 함수에 들어가보면 아래와 같은 그래프 뷰를 확인할 수 있다.
<img alt="" src="https://velog.velcdn.com/images/hy25u/post/c2c9887d-5682-4e3a-8074-79427f1d54af/image.png" />
strcmp 함수를 호출하는 것으로 보아 입력 값을 비교하는 것이라는 걸 알 수 있고 그 대상이 되는 값은 rdx에 담긴 Str2, 즉 &quot;Compar3_the_str1ng&quot; 문자열이라는 것을 알 수 있다. </p>
<p>IDA에서 view &gt; Open subviews &gt; Strings 에서도 확인할 수 있다. <img alt="" src="https://velog.velcdn.com/images/hy25u/post/c1fa097f-0ed0-4840-a3c4-0512ac661d5d/image.png" /></p>
<blockquote>
<p>DH{Compar3_the_str1ng}</p>
</blockquote>
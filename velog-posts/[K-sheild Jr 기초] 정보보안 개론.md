<h1 id="정보보안의-필요성">정보보안의 필요성</h1>
<h3 id="사고-사례-분석">사고 사례 분석</h3>
<ul>
<li>Colonial Pipeline Ransomware
미국 동부 지역 기름의 절반 정도를 책임지는 대형 회사가 랜섬웨어에 감염되어 본 기능을 못 하게 되는 사태가 발생하였다. 
<a href="https://www.boannews.com/media/view.asp?idx=109052">https://www.boannews.com/media/view.asp?idx=109052</a>
<a href="https://0xmh.tistory.com/50">https://0xmh.tistory.com/50</a></li>
<li>Lazarus 방글라데시 중앙은행 해킹 
뉴욕연방준비은행에 보관 중인 계좌에서 거액이 불법적으로 인출되는 사건이 발생하였다. </li>
<li>Log4j 보안 취약점 사태 
Java 라이브러리 Log4j에서 발생한 보안 취약점으로 원격 코드 실행을 시도할 수 있어 해당 시스템의 제어권을 완전히 탈취할 수 있다. </li>
</ul>
<p>세계적으로 사이버 공격이 증가되고 피해액 또한 늘어나고 있는 추세이다. </p>
<h1 id="정보보안이란">정보보안이란</h1>
<p>조직이나 개인이 보유한 정보 자산에 대해 무단으로 접근, 사용, 공개, 파괴, 변조 또는 손실 등을 막기 위한 전략, 절차, 기술을 의미한다. </p>
<h3 id="주요-용어">주요 용어</h3>
<table>
  <tr><th>구분</th><th>설명</th></tr>
  <tr><td>자산</td><td>보호해야 할 가치가 있는 모든 항목<br />물리적 문서, 디지털 파일, 데이터베이스, 시스템, 네트워크 등 정보가 저장되거나 처리되는 모든 매체<br />정보 자산의 가치는 정보를 사용할 수 있는 권한이 누구에게 있는지, 정보가 얼마나 중요한지에 따라 결정</td></tr>

  <tr><td>위협</td><td>정보 자산에 해를 끼칠 수 있는 모든 행위나 사건 <br />자연 재해, 기술적 실패, 공격(해킹, 사회공학, 악성코드 배포 등)으로부터 발생<br />위협은 의도적이지만, 실수나 사고로 인해 발생하기도 함</td></tr>

  <tr><td>취약점</td><td>정보 시스템, 절차, 운영상의 약점이나 결함으로, 취약점을 통해 위협이 자산에 해를 끼치는 것을 가능하게 함<br />소프트웨어 버그, 구성 오류, 물리적 보안의 결핍 등 다양한 형태로 존재<br />사용자의 보안 인식 부족도 포함됨</td></tr>
  <tr><td>위험</td><td>외부의 위협이 내부의 취약점을 이용하여 보유한 자산에 피해를 입힐 수 있는 잠재적인 가능성<br /> 위험 관리는 위험 식별, 평가, 완화 과정을 포함하며, 정보보안 전략의 핵심 요소임</td></tr>
</table>

<h3 id="정보보안-3요소">정보보안 3요소</h3>
<ol>
<li>Confidentiality 기밀성
허가되지 않은 사용자 또는 객체가 정보의 내용을 알 수 없도록 하는 것 
Access control(Permissions, Whitelists/Blacklists, Cryptography)이 필요함</li>
<li>Integrity 무결성
허가되지 않은 사용자 또는 객체가 정보를 함부로 수정할 수 없도록 하는 것 </li>
<li>Availability 가용성 
허가된 사용자 또는 객체가 정보에 접근하려 하고자 할 때 이것이 방해받지 않도록 하는 것</li>
</ol>
<h1 id="위협과-공격">위협과 공격</h1>
<h3 id="위협">위협</h3>
<p>정보 자산에 해를 끼칠 수 있는 모든 행위나 사건을 말한다. 사람의 행위 뿐만 아니라 자연 재해로 인해서도 발생할 수 있다. </p>
<h4 id="분류">분류</h4>
<ul>
<li>의도적 위협 vs 비의도적 위협</li>
<li>외부 위협 vs 내부 위협</li>
<li>활동적 위협, 수동적 위협, 누설, 속임수, 중단, 강탈/탈취, 침입, 악용, 추출<h4 id="종류">종류</h4>
</li>
<li>Phishing 
가짜 웹 사이트나 이메일 통해 민감한 정보 획득하려는 사기</li>
<li>Ransomware
사용자의 데이터를 암호화하고 해독 키를 얻기 위해 금전을 요구하는 악성 소프트웨어</li>
<li>DDoS
분산형 서비스 공격으로 여러 컴퓨터를 이용해 대량의 트래픽을 발생시켜 정상적인 작동을 어렵게 하는 것</li>
<li>Scanning
목표로 하는 네트워크에서 동작 중인 시스템, 서비스를 탐색하는 행위</li>
<li>Sniffing
네트워크 중간에서 남의 패킷 정보를 도청하는 행위</li>
<li>Spoofing
승인 받은 사용자인 것처럼 시스템 접근하거나 허가된 주소로 가장하여 접근 제어를 우회하는 행위</li>
<li>MITM
중간자 공격으로 네트워크 통신을 조작하여 내용을 도청하거나 조작하는 공격</li>
<li>SQL Injection
악의적인 SQL 코드를 주입하여 데이터베이스를 조작하는 공격</li>
<li>XSS
사용자 브라우저에 악성 스크립트를 실행시키는 공격, 서버 측이 아닌 해당 페이지를 방문하게 되는 사용자에게 발생하는 공격이다. </li>
<li>APT
지능형 지속 공격으로 특정 타깃 선정한 후 장기간에 걸쳐 지속적인 공격을 수행하는 것, 앞서 언급되었던 Lazarus의 방글라데시 은행 공격이 이에 해당함 </li>
</ul>
<h4 id="apt-cyber-attack-life-cycle">APT Cyber Attack Life Cycle</h4>
<ul>
<li>Initial Reconnaissance (초기 정찰)</li>
<li>Initial Compromise (초기 침해)</li>
<li>Establish Foothold (발판 마련)</li>
<li>Escalate Privileges (권한 상승)</li>
<li>Internal Reconnaissance (내부 정찰)</li>
<li>Move Laterally (수평 이동)</li>
<li>Maintain Presence (상태 유지)</li>
<li>Complete Mission (임무 완료)</li>
</ul>
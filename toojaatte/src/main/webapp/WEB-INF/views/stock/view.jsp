<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>실시간시세</title>
<link rel="stylesheet" type="text/css" href="/css/stockView.css">
</head>
<body>
	<div class="container-fluid">
		<div class="title-div">
			<span class="stock-code">A${krxData['code'] }</span> <span
				class="stock-name">${krxData['stockInfoData'][0] }</span>
			<p></p>
			<span>실시간 시세 현황</span>
			<p />
			<span>${krxData['getTime'] }</span>기준 <span class="small-text">(${krxData['janggubun'] })</span>
		</div>
		<div class="col-md-9">
			<div class="row">
				<div>
					<div class="now-price">
						<span>현재가 <br>${krxData['stockInfoData'][1] }</span> <span
							class="now-price-arrow small-text"></span> <span
							class="small-text">${krxData['stockInfoData'][3] }
							${krxData['DungRakrate_str'] }</span>
					</div>
					<div class="btn-group btn-group-sm">
						<button type="button" class="btn term" value="days" id="days">10일</button>
						<button type="button" class="btn term" value="month" id="month">1개월</button>
						<button type="button" class="btn term" value="three" id="three">3개월</button>
						<button type="button" class="btn term" value="six" id="six">6개월</button>
						<button type="button" class="btn term" value="year" id="year">1년</button>
					</div>
					<div id="stock_line_chart">
						<!-- <img src="/upload/image/stock/kakao3months.png" class="img-responsive" width="90%"> -->
					</div>
					<div id="stock_bar_chart"></div>
				</div>
			</div>
		</div>
		<div class="col-sm-3">
			<div class="body-div">
				<ul>
					<li class="info-title">주가 정보
						<p />
					</li>
					<li>시가 ${krxData['stockInfoData'][7] }</li>
					<li>고가 ${krxData['stockInfoData'][8] }</li>
					<li>거래량 ${krxData['stockInfoData'][5] }</li>
					<li>거래대금 ${krxData['stockInfoData'][6] }</li>
				</ul>
			</div>
			<div class="invest-info-div">
				<hr width="70%" />
				<div>
					<ul>
						<li class="info-title">투자 정보
							<p />
						</li>
						<li>상한가 ${krxData['stockInfoData'][12] }</li>
						<li>하한가 ${krxData['stockInfoData'][13] }</li>
						<li>52주 최고 ${krxData['stockInfoData'][10] }</li>
						<li>52주 최저 ${krxData['stockInfoData'][11] }</li>
						<li>액면가 ${krxData['stockInfoData'][16] }</li>
						<li>PER ${krxData['stockInfoData'][14] }</li>
						<li>상장주식수 ${krxData['stockInfoData'][15] }</li>
					</ul>
				</div>
			</div>
		</div>
		<div class="row">
			<div class="col-md-6">
				<p class="table-name">거래원 현황</p>
				<table class="table" style="width: 90%;">
					<colgroup>
						<col class="topSell" />
						<col class="topSell" />
						<col class="topBuy" />
						<col class="topBuy" />
					</colgroup>
					<tr style="background-color: white;">
						<th colspan="2">매도상위</th>
						<th colspan="2">매수상위</th>
					</tr>
					<tr>
						<th>증권사</th>
						<th>거래량</th>
						<th>증권사</th>
						<th>거래량</th>
					</tr>
					<c:if test="${krxData['askPrice_length'] > 0}">
						<c:forEach var="askPrice" items="${krxData['askPrice'] }">
							<tr>
								<td>${askPrice[0] }</td>
								<td>${askPrice[1] }</td>
								<td>${askPrice[2] }</td>
								<td>${askPrice[3] }</td>
							</tr>
						</c:forEach>
					</c:if>
				</table>
			</div>
			<div class="col-md-6">
				<p class="table-name">호가</p>
				<table class="table" style="width: 90%;">
					<colgroup>
						<col class="topSell" />
						<col />
						<col class="topBuy" />
					</colgroup>
					<tr style="background-color: white;">
						<th>매도잔량</th>
						<th>호가</th>
						<th>매수잔량</th>
					</tr>
					<c:if
						test="${krxData['hoga'][0] != '' || !krxData['hoga'][0].equals('')}">
						<tr>
							<td>${krxData['hoga'][0]}</td>
							<td class="sell">${krxData['hoga'][1]}</td>
							<td></td>
						</tr>
						<tr>
							<td>${krxData['hoga'][2]}</td>
							<td class="sell">${krxData['hoga'][3]}</td>
							<td></td>
						</tr>
						<tr>
							<td>${krxData['hoga'][4]}</td>
							<td class="sell">${krxData['hoga'][5]}</td>
							<td></td>
						</tr>
						<tr>
							<td>${krxData['hoga'][6]}</td>
							<td class="sell">${krxData['hoga'][7]}</td>
							<td></td>
						</tr>
						<tr>
							<td>${krxData['hoga'][8]}</td>
							<td class="sell">${krxData['hoga'][9]}</td>
							<td></td>
						</tr>
						<tr>
							<td></td>
							<td class="buy">${krxData['hoga'][10]}</td>
							<td>${krxData['hoga'][11]}</td>
						</tr>
						<tr>
							<td></td>
							<td class="buy">${krxData['hoga'][12]}</td>
							<td>${krxData['hoga'][13]}</td>
						</tr>
						<tr>
							<td></td>
							<td class="buy">${krxData['hoga'][14]}</td>
							<td>${krxData['hoga'][15]}</td>
						</tr>
						<tr>
							<td></td>
							<td class="buy">${krxData['hoga'][16]}</td>
							<td>${krxData['hoga'][17]}</td>
						</tr>
						<tr>
							<td></td>
							<td class="buy">${krxData['hoga'][18]}</td>
							<td>${krxData['hoga'][19]}</td>
						</tr>
						<tr style="background-color: white;">
							<td class="down">${krxData['hoga'][20]}</td>
							<td>잔량합계</td>
							<td style="color: #eb8787;">${krxData['hoga'][21]}</td>
						</tr>
					</c:if>
				</table>
			</div>
		</div>
		<div class="col-md-12">
			<p class="table-name">시간대별 체결가</p>
			<table class="table">
				<tr>
					<th>시간</th>
					<th>체결가</th>
					<th>전일대비</th>
					<th>매도호가</th>
					<th>매수호가</th>
					<th>매수잔량</th>
				</tr>
				<c:if test="${krxData['timeConclude_length'] > 0}">
					<c:forEach var="timeConclude" items="${krxData['timeConclude'] }">
						<tr>
							<td>${timeConclude[0] }</td>
							<td>${timeConclude[1] }</td>
							<td>${timeConclude[2] }<input type="hidden" name="lastDay"
								value="${timeConclude[6] }" />
							</td>
							<td>${timeConclude[3] }</td>
							<td>${timeConclude[4] }</td>
							<td>${timeConclude[5] }</td>
						</tr>
					</c:forEach>
				</c:if>
			</table>
		</div>
		<div class="col-md-12">
			<p class="table-name">일자별 체결가</p>
			<table class="table">
				<tr>
					<th>일자</th>
					<th>종가</th>
					<th>전일대비</th>
					<th>시가</th>
					<th>고가</th>
					<th>저가</th>
					<th>거래량</th>
					<th>거래대금</th>
				</tr>
				<c:if test="${krxData['dailyStock_length'] > 0}">
					<c:forEach var="dailyStock" items="${krxData['dailyStock'] }">
						<tr>
							<td class="daily_stock_date">${dailyStock[0] }</td>
							<td class="daily_stock_closing_price">${dailyStock[1] }</td>
							<td>${dailyStock[2] }<input type="hidden"
								name="lastDayDaily" value="${dailyStock[8] }" />
							</td>
							<td>${dailyStock[3] }</td>
							<td>${dailyStock[4] }</td>
							<td>${dailyStock[5] }</td>
							<td class="daily_stock_volume">${dailyStock[6] }</td>
							<td>${dailyStock[7] }</td>
						</tr>
					</c:forEach>
				</c:if>
			</table>
		</div>
		<p class="table-name">${krxData['stockInfoData'][0] } 재무정보</p>
		<div class="col-md-12">
			<p>대차 대조표</p>
			<table class="table">
				<tr>
					<th rowspan="2" valign="middle">재무항목</th>
					<th colspan="3">${financialData['balanceSheetDate'][4] }년 ${financialData['balanceSheetDate'][5] }월</th>
					<th colspan="3">${financialData['balanceSheetDate'][2] }년 ${financialData['balanceSheetDate'][3] }월</th>
					<th colspan="3">${financialData['balanceSheetDate'][0] }년 ${financialData['balanceSheetDate'][1] }월</th>
				</tr>
				<tr>
					<th>금액</th>
					<th>구성비</th>
					<th>증감율</th>
					<th>금액</th>
					<th>구성비</th>
					<th>증감율</th>
					<th>금액</th>
					<th>구성비</th>
					<th>증감율</th>
				</tr>
				<c:if test="${financialData['balanceSheetDataLength'] > 0}">
					<c:forEach items="${financialData['balanceSheetData'] }" var="balanceSheetData">
						<tr>
							<td>${balanceSheetData[0] }</td>
							<td>${balanceSheetData[7] }</td>
							<td><fmt:formatNumber value="${balanceSheetData[8] }" pattern="0.0"></fmt:formatNumber></td>
							<td>${balanceSheetData[9] }</td>
							<td>${balanceSheetData[4] }</td>
							<td><fmt:formatNumber value="${balanceSheetData[5] }" pattern="0.0"></fmt:formatNumber></td>
							<td>${balanceSheetData[6] }</td>
							<td>${balanceSheetData[1] }</td>
							<td><fmt:formatNumber value="${balanceSheetData[2] }" pattern="0.0"></fmt:formatNumber></td>
							<td>${balanceSheetData[3] }</td>
						</tr>
					</c:forEach>
				</c:if>
			</table>
		</div>
		<div class="col-md-12">
			<p>손익 계산서</p>
			<table class="table">
				<tr>
					<th rowspan="2" valign="middle">재무항목</th>
					<th colspan="3">${financialData['incomeStatementDate'][4] }년 ${financialData['incomeStatementDate'][5] }월</th>
					<th colspan="3">${financialData['incomeStatementDate'][2] }년 ${financialData['incomeStatementDate'][3] }월</th>
					<th colspan="3">${financialData['incomeStatementDate'][0] }년 ${financialData['incomeStatementDate'][1] }월</th>
				</tr>
				<tr>
					<th>금액</th>
					<th>구성비</th>
					<th>증감율</th>
					<th>금액</th>
					<th>구성비</th>
					<th>증감율</th>
					<th>금액</th>
					<th>구성비</th>
					<th>증감율</th>
				</tr>
				<c:if test="${financialData['incomeStatementDataLength'] > 0}">
					<c:forEach items="${financialData['incomeStatementData'] }" var="incomeStatementData">
						<tr>
							<td>${incomeStatementData[0] }</td>
							<td>${incomeStatementData[7] }</td>
							<td>${incomeStatementData[8] }</td>
							<td>${incomeStatementData[9] }</td>
							<td>${incomeStatementData[4] }</td>
							<td>${incomeStatementData[5] }</td>
							<td>${incomeStatementData[6] }</td>
							<td>${incomeStatementData[1] }</td>
							<td>${incomeStatementData[2] }</td>
							<td>${incomeStatementData[3] }</td>
						</tr>
					</c:forEach>
				</c:if>
			</table>
		</div>
		<div class="col-md-12">
			<p>현금 흐름표</p>
			<table class="table">
				<tr>
					<th rowspan="2" valign="middle">재무항목</th>
					<th colspan="2">${financialData['cashFlowDate'][4] }년 ${financialData['cashFlowDate'][5] }월</th>
					<th colspan="2">${financialData['cashFlowDate'][2] }년 ${financialData['cashFlowDate'][3] }월</th>
					<th colspan="2">${financialData['cashFlowDate'][0] }년 ${financialData['cashFlowDate'][1] }월</th>
				</tr>
				<tr>
					<th>금액</th>
					<th>증감율</th>
					<th>금액</th>
					<th>증감율</th>
					<th>금액</th>
					<th>증감율</th>
				</tr>
				<c:if test="${financialData['cashFlowDataLength'] > 0}">
					<c:forEach items="${financialData['cashFlowData'] }" var="cashFlowData">
						<tr>
							<td>${cashFlowData[0] }</td>
							<td>${cashFlowData[5] }</td>
							<td>${cashFlowData[6] }</td>
							<td>${cashFlowData[3] }</td>
							<td>${cashFlowData[4] }</td>
							<td>${cashFlowData[1] }</td>
							<td>${cashFlowData[2] }</td>
						</tr>
					</c:forEach>
				</c:if>
			</table>
		</div>
	</div>
	<script type="text/javascript"	src="https://www.gstatic.com/charts/loader.js"></script>
	<script type="text/javascript" src="/js/stock/stock-detail-view.js"></script>
	<script type="text/javascript">
	const now_price = document.querySelector(".now-price");
	const now_price_arrow = document.querySelector(".now-price-arrow");
		document.addEventListener("DOMContentLoaded", function() {
			if ("${krxData['stockInfoData'][2]}" === '1'
				|| "${krxData['stockInfoData'][2]}" === '2') {
					now_price.classList.remove("down");
					now_price.classList.add("up");
					now_price_arrow.innerText = "▲";
				} else if ("${krxData['stockInfoData'][2]}" === '3') {
					now_price_arrow.innerText = "-";
				} else if ("${krxData['stockInfoData'][2]}" === '4'
						|| "${krxData['stockInfoData'][2]}" === '5') {
					now_price_arrow.innerText = "▼";
					now_price.classList.remove("up");
					now_price.classList.add("down");
				}
			});
	</script>
</body>
</html>
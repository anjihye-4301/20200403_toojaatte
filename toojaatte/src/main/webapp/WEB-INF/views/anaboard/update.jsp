<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판 글수정</title>
<style type="text/css">
.fileSpace {
	list-style: none;
}
li{
	margin: 10px;
}
</style>
<script type="text/javascript">
var deleteFileRno="";
var counter = 1;

//첨부파일 미리보기
function readURL(input){
	if(input.files&&input.files[0]){
// 		alert(input);
		var reader = new FileReader();
		var itag="";
		reader.onload = function(e){
			itag = "<img src='"+e.target.result+"' style='max-width:50%'/>";
			$(".preview:last").append(itag);
// 			alert($(this));
		}
		reader.readAsDataURL(input.files[0]);
	}
}
$(function(){
	//파일 리스트를 표시할 객체 저장
	var str = "";
	$("#fileAddBtn").click(function(e){
		str += "<li>"
		str += "<button type='button' class='fileDeleteBtn'><span class='glyphicon glyphicon-remove'></span></button>"
		str += "<input type='file' multiple='multiple' class='file' name='multiFile'/>";
		str += "<div class='preview'>"		
		str += "</div>"
		str += "</li>"
		$(".fileSpace").append(str);
		str="";
	});
	$(document).on("click",".fileDeleteBtn",(function(e){
		$(this).closest("li").remove();	
	}));
	$(document).on("click",".DBFileDeleteBtn",(function(e){
		deleteFileRno += $(this).closest('li').children('input').attr('value');
		deleteFileRno += ",";
// 		alert(deleteFileRno);		
		$(this).closest("li").remove();	
	}));
	$("#updateForm").on("submit", function(e){
		var f_cnt = $(".file").length;
		var f = $(".file");
		for (i=0; i<f_cnt; i++){
			if(f[i].value==null || f[i].value==""){
				f[i].closest("li").remove();
			}
		}
		str += '<input type="hidden" name="deleteFileRno" value="'
		str += deleteFileRno
		str += '"></input>'
		$("#deleteFileNums").append(str);
		//return false;
	});
	$(document).on("change",".file",function(e){
// 		alert("이미지 미리보기");
		$(".file").on("change",readURL(this));	
	});
	$(".back").click(function() {
		//글번호 찾기 - 클릭한 것(this) 안에 글번호 클래스 객체(td)안에 글자(text)
		//var no = $(this).find(".no").text();
		//글보기로 이동 - 글번호를 붙여서
		location = "view.do?no=${dto.no}"
			+"&page=${page }&key=${key }"
			+"&word=${word }"
			+"&gradeType=${gradeType}"
			+"&headerType=${headerType}"
			+"&orderType=${orderType}";
	});
});
</script>
</head>
<body>
	<h1>게시판 글 수정</h1>
	<form method="post" action="update.do" id="updateForm" enctype="multipart/form-data">
		<input type="hidden" name="no" value="${dto.no }"/>
		<!-- bootstrap의 폼 : form-> form-group -> form-control -->
		<!-- 		타입선택 -->
		<div class="form-group">
			<label for="titleType">말머리</label>
			<div>
				<input type="radio" value="1" name="titleType" ${(dto.titleType==1)?"checked":"" }>주식
			</div>
			<div>
				<input type="radio" value="2" name="titleType" ${(dto.titleType==2)?"checked":"" }>가상화폐
			</div>
			<div>
				<input type="radio" value="3" name="titleType" ${(dto.titleType==3)?"checked":"" }>기타
			</div>
		</div>
		<!-- 제목 입력 -->
		<div class="form-group">
			<label for="title">제목</label>
			<!-- 입력한 데이터의 앞뒤 공백문자는 제거(trim())
   			 id, class : 화면 컨트롤을 위해서(빠른 선택), name : 넘어가는 데이터 이름 -->
			<!-- <input type="text" class="form-control" id="title" name="title" required="required" pattern="^.{4,100}$" title="제목을 4~100 글자 사이로 입력하셔야 합니다."> -->
			<input type="text" class="form-control" id="title" name="title"
				value="${dto.title }">
		</div>
		<!-- 내용 입력 -->
		<div class="form-group">
			<label for="content">내용</label>
			<!-- <textarea class="form-control" rows="5" id="content" name="content" required="required" ></textarea> -->
			<textarea class="form-control" rows="5" id="content" name="content">${dto.content }</textarea>
		</div>
		<!-- 작성자 login session->controller -->
		<!-- 첨부파일 -->
		<div class="form-group">
			<label for="multiFile">첨부파일</label>
			<button type="button" id="fileAddBtn">
			<span class="glyphicon glyphicon-plus"/>
			</button>
			<div class="fileSpace">
			<c:forEach items="${flist}" var="fdto">
			<li>
				<button type="button" class="DBFileDeleteBtn"><span class="glyphicon glyphicon-remove"></span></button>
				<label>${fdto.ori_fileName }</label>
				<input type="hidden" value="${fdto.rno }"/>
				<img alt="" src="${fdto.fileName }" style="max-width: 80%; min-width: 30%;"></img>
			</li>
			</c:forEach>
			</div>
			<span id="deleteFileNums"></span>
		</div>
		<div id="hidden">
		<input type="hidden" name="page" value="${param.page }"/>
		<input type="hidden" name="key" value="${param.key }"/>
		<input type="hidden" name="word" value="${param.word }"/>
		<input type="hidden" name="gradeType" value="${param.gradeType}"/>
		<input type="hidden" name="headerType" value="${param.headerType}"/>
		<input type="hidden" name="orderType" value="${param.orderType}"/>
		</div>
		<!-- 버튼 처리 : button은 기본 type이 submit이다.(데이터 넘기는 함수 호출)-->
		<button type="submit" class="next">등록</button>
		<button type="reset">다시입력</button>
		<button type="button" class="back">취소</button>
		
	</form>
	<br/>
</body>
</html>
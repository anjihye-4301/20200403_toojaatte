package com.toojaatte.util.exception;

import org.springframework.http.HttpStatus;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.servlet.NoHandlerFoundException;

import lombok.extern.log4j.Log4j;

/*
 * 자동으로 생성이 되어지게 하는 어노테이션
 * - @Controller : 서버의 uri와 클래스나 메서드를 매칭시켜주는 처리 : @RequesetMapping 등.
 * - @Service : 처리되는 프로세서를 처리해 주는 객체
 * - @Repository : DB연동에 관련된 처리
 * - @Component : 객체의 구성으로 포함시키는 객체
 * - @RestController : 서버의 uri 클래스나 메서드에 매칭시키는 처리. 순수 데이터 전송을 위해 사용
 * - @ControllerAdvice, @RestControllerAdvice : Spring의 예외처리 객체
 */

@ControllerAdvice
@Log4j
public class CommonExceptionAdvice {

	// 500번 오류를 처리를 한다.	
	@ExceptionHandler(Exception.class)
	public String except(Exception e, Model model) {
		log.error("Exception....." + e.getMessage());
		// 예외객체를 JSP에서 사용해서 예외 정보를 출력하려고 한다면 데이터로 넘겨주기 위해서 
		// Model이 필요하다.
		model.addAttribute("exception", e);
		log.error(model);
		// /WEB-INF/views/ + error_page + .jsp
		return "error/error_page";
	}
	
	// 404번 오류 처리를 한다.
	@ExceptionHandler(NoHandlerFoundException.class)
	@ResponseStatus(HttpStatus.NOT_FOUND)
	public String handle404(NoHandlerFoundException e) {
		return "error/custom404";
	}

	
}

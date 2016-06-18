package web.common;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.UNPROCESSABLE_ENTITY)
public final class ResourceUnprocessableEntityException extends RuntimeException {
    //  class definition
}
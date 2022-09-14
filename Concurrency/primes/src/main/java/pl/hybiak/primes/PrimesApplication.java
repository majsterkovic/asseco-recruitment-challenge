package pl.hybiak.primes;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@SpringBootApplication
@RestController
public class PrimesApplication {

	@Autowired
	private PrimesService primesService;

	@GetMapping(value = "/")
	public Integer getUserFeedback(@RequestParam Map<String,String> requestParams) throws Exception {
		String start = requestParams.get("start");
		String end = requestParams.get("end");
		return primesService.primesInRange(start, end);
	}

	public static void main(String[] args) {
		SpringApplication.run(PrimesApplication.class, args);
	}

}

package pl.hybiak.boudingbox;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;

@SpringBootApplication
@RestController
public class BoundingboxApplication {

	@Autowired
	public BoundingboxService boundingboxService;


	@PostMapping(value = "add", consumes="application/json")
	public HttpStatus add(@RequestBody BoundingBox box) {
		if(boundingboxService.add(box))
		{
			return HttpStatus.CREATED;
		}
		else
		{
			return HttpStatus.BAD_REQUEST;
		}
	}

	@PostMapping(value = "/remove", consumes="application/json")
	public HttpStatus remove(@RequestBody Id myid) {
		Integer id = myid.id;
		if(boundingboxService.remove(id))
		{
			return HttpStatus.NO_CONTENT;
		}
		else
		{
			return HttpStatus.BAD_REQUEST;
		}
	}

	@GetMapping(value = "/get", consumes="application/json")
	public BoundingBox get(@RequestBody Id myid) {
		Integer id = myid.id;
		return boundingboxService.get(id);
	}

	@PutMapping(value = "/edit", consumes="application/json")
	public HttpStatus edit(@RequestBody EditBoundingBox box) {
		if(boundingboxService.edit(box))
		{
			return HttpStatus.NO_CONTENT;
		}
		else
		{
			return HttpStatus.BAD_REQUEST;
		}
	}

	@GetMapping(value = "/getAll")
	public HashMap<Integer, BoundingBox> getAll() {
		return boundingboxService.getAll();
	}

	public static void main(String[] args) {
		SpringApplication.run(BoundingboxApplication.class, args);
	}
}

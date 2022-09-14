package pl.hybiak.primes;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;


@Service
public class PrimesService {

    public static boolean isPrime(int num) {
        if (num == 1)
        {
            return false;
        }
        if (num > 2 && num % 2 == 0)
        {
            return false;
        }
        int top = (int)Math.sqrt(num) + 1;
        for(int i = 3; i < top; i+=2)
        {
            if(num % i == 0)
            {
                return false;
            }
        }
        return true;
    }

    public Integer primesInRange(String start, String end)
    {
        int primes_count = 0;
        for (int i = Integer.parseInt(start); i <= Integer.parseInt(end); i++) {
            if (isPrime(i)) {
                primes_count++;
            }
        }
        return primes_count;
    }
}

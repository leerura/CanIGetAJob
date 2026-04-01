import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        // 1. 빠른 입력을 위한 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 2. 한 줄 읽기
        String line = br.readLine();
        if (line == null) return;
        
        // 3. 공백 단위로 데이터 쪼개기
        StringTokenizer st = new StringTokenizer(line);
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 여기서부터 로직 시작!
        System.out.println("N: " + N + ", M: " + M);
    }
}
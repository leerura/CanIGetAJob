import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int R,C;
    static char[][] map;
    static boolean[] used = new boolean[26];
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};

    public static void main(String[] args) throws Exception {
        // 1. 빠른 입력을 위한 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];

        for (int i=0; i<R; i++) {
            map[i] = br.readLine().toCharArray();
        }
        
        System.out.println(dfs(0, 0));
    }

    static int dfs(int row,int col) {

        int charIdx = map[row][col] - 'A';
        used[charIdx] = true;

        int maxDist = 0;

        for (int i=0; i<4; i++) {
            int nr = row + dr[i];
            int nc = col + dc[i];

            if(nr >= 0 && nr < R && nc >= 0 && nc < C && !used[map[nr][nc]-'A']) {
                maxDist = Math.max(maxDist,dfs(nr,nc));
            }
        }

        used[charIdx] = false;

        return 1+maxDist;
    }
}
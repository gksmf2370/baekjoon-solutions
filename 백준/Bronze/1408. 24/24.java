import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 현재 
        String[] nowTime = sc.nextLine().split(":");
        int nowHour = Integer.parseInt(nowTime[0]);
        int nowMinute = Integer.parseInt(nowTime[1]);
        int nowSecond = Integer.parseInt(nowTime[2]);
        
        // 목표 
        String[] goalTime = sc.nextLine().split(":");
        int goalHour = Integer.parseInt(goalTime[0]);
        int goalMinute = Integer.parseInt(goalTime[1]);
        int goalSecond = Integer.parseInt(goalTime[2]);
        

        int nowInSeconds = nowHour * 3600 + nowMinute * 60 + nowSecond;
        int goalInSeconds = goalHour * 3600 + goalMinute * 60 + goalSecond;
        
        int remainingTimeInSeconds;
        if (goalInSeconds >= nowInSeconds) {
            remainingTimeInSeconds = goalInSeconds - nowInSeconds;
        } else {

            remainingTimeInSeconds = (24 * 3600 - nowInSeconds) + goalInSeconds;
        }
        
 
        int remainingHour = remainingTimeInSeconds / 3600;
        remainingTimeInSeconds %= 3600;
        int remainingMinute = remainingTimeInSeconds / 60;
        int remainingSecond = remainingTimeInSeconds % 60;
        
        System.out.printf("%02d:%02d:%02d\n", remainingHour, remainingMinute, remainingSecond);
        
        sc.close();
    }
}

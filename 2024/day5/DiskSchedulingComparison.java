import java.util.*;

interface DiskScheduling {
    int schedule(int head, List<Integer> requests, int diskSize, String direction);
}

class FCFS implements DiskScheduling {
    @Override
    public int schedule(int head, List<Integer> requests, int diskSize, String direction) {
        int seekTime = 0;
        for (int req : requests) {
            seekTime += Math.abs(req - head);
            head = req;
        }
        return seekTime;
    }
}

class SSTF implements DiskScheduling {
    @Override
    public int schedule(int head, List<Integer> requests, int diskSize, String direction) {
        int seekTime = 0;
        List<Integer> tempRequests = new ArrayList<>(requests);

        while (!tempRequests.isEmpty()) {
            // Create a final copy of head for use in lambda
            final int currentHead = head;

            // Find the closest request to the current head
            int closest = tempRequests.stream()
                                       .min(Comparator.comparingInt(r -> Math.abs(r - currentHead)))
                                       .orElseThrow();
            // Add seek time for this request
            seekTime += Math.abs(closest - head);
            head = closest; // Update head position
            tempRequests.remove(Integer.valueOf(closest)); // Remove the processed request
        }

        return seekTime;
    }
}

class SCAN implements DiskScheduling {
    @Override
    public int schedule(int head, List<Integer> requests, int diskSize, String direction) {
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int req : requests) {
            if (req < head) left.add(req);
            else right.add(req);
        }
        Collections.sort(left);
        Collections.sort(right);

        int seekTime = 0;
        if (direction.equals("right")) {
            for (int req : right) {
                seekTime += Math.abs(req - head);
                head = req;
            }
            for (int req : left) {
                seekTime += Math.abs(req - head);
                head = req;
            }
        } else {
            for (int req : left) {
                seekTime += Math.abs(req - head);
                head = req;
            }
            for (int req : right) {
                seekTime += Math.abs(req - head);
                head = req;
            }
        }
        return seekTime;
    }
}

class C_SCAN implements DiskScheduling {
    @Override
    public int schedule(int head, List<Integer> requests, int diskSize, String direction) {
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int req : requests) {
            if (req < head) left.add(req);
            else right.add(req);
        }
        Collections.sort(left);
        Collections.sort(right);

        int seekTime = 0;
        for (int req : right) {
            seekTime += Math.abs(req - head);
            head = req;
        }
        if (!left.isEmpty()) {
            seekTime += Math.abs(head - (diskSize - 1)); // Jump to the end
            head = 0; // Reset head to the start
            for (int req : left) {
                seekTime += Math.abs(req - head);
                head = req;
            }
        }
        return seekTime;
    }
}

class LOOK implements DiskScheduling {
    @Override
    public int schedule(int head, List<Integer> requests, int diskSize, String direction) {
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int req : requests) {
            if (req < head) left.add(req);
            else right.add(req);
        }
        Collections.sort(left);
        Collections.sort(right);

        int seekTime = 0;
        if (direction.equals("right")) {
            for (int req : right) {
                seekTime += Math.abs(req - head);
                head = req;
            }
            for (int req : left) {
                seekTime += Math.abs(req - head);
                head = req;
            }
        } else {
            for (int req : left) {
                seekTime += Math.abs(req - head);
                head = req;
            }
            for (int req : right) {
                seekTime += Math.abs(req - head);
                head = req;
            }
        }
        return seekTime;
    }
}

class C_LOOK implements DiskScheduling {
    @Override
    public int schedule(int head, List<Integer> requests, int diskSize, String direction) {
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int req : requests) {
            if (req < head) left.add(req);
            else right.add(req);
        }
        Collections.sort(left);
        Collections.sort(right);

        int seekTime = 0;
        for (int req : right) {
            seekTime += Math.abs(req - head);
            head = req;
        }
        if (!left.isEmpty()) {
            head = left.get(0); // Jump to the lowest request
            for (int req : left) {
                seekTime += Math.abs(req - head);
                head = req;
            }
        }
        return seekTime;
    }
}

public class DiskSchedulingComparison {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input
        System.out.print("Enter the initial head position: ");
        int head = scanner.nextInt();
        System.out.print("Enter the request sequence (space-separated): ");
        scanner.nextLine(); // Consume the newline
        List<Integer> requests = new ArrayList<>();
        for (String s : scanner.nextLine().split(" ")) {
            requests.add(Integer.parseInt(s));
        }
        System.out.print("Enter the disk size: ");
        int diskSize = scanner.nextInt();
        System.out.print("Enter the initial direction (left/right): ");
        String direction = scanner.next();

        // Algorithms
        DiskScheduling[] algorithms = {
            new FCFS(), new SSTF(), new SCAN(), new C_SCAN(), new LOOK(), new C_LOOK()
        };
        String[] algorithmNames = {
            "FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK"
        };

        // Comparison
        System.out.println("\nAlgorithm Performance:");
        for (int i = 0; i < algorithms.length; i++) {
            int seekTime = algorithms[i].schedule(head, requests, diskSize, direction);
            System.out.printf("%-10s : Total Seek Time = %d\n", algorithmNames[i], seekTime);
        }
    }
}

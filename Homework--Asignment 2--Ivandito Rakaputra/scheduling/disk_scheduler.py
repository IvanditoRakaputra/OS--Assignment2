def fcfs(head, requests):
    total_distance = 0
    current_cylinder = head
    distance=[]
    for req in requests:
        total_distance += abs(req - current_cylinder)
        #distance.append(abs(req - current_cylinder))
        current_cylinder = req
    #print (distance)  
    return total_distance

def scan(head, requests):
    total_distance = 0
    requests.sort()
    direction = 1  # 1 for right, -1 for left
    current_cylinder = head
    while requests:
        if direction == 1:
            for req in requests[:]:
                if req >= current_cylinder:
                    total_distance += abs(req - current_cylinder)
                    current_cylinder = req
                    requests.remove(req)
            direction = -1
        else:
            for req in reversed(requests):
                if req <= current_cylinder:
                    total_distance += abs(req - current_cylinder)
                    current_cylinder = req
                    requests.remove(req)
            direction = 1
    return total_distance

def cscan(head, requests):
    total_distance = 0
    requests.sort()
    current_cylinder = head
    while requests:
        for req in requests[:]:
            if req >= current_cylinder:
                total_distance += abs(req - current_cylinder)
                current_cylinder = req
                requests.remove(req)
                break
        else:  # No request found in current direction
            total_distance += abs(4999 - current_cylinder)  # Move to the end
            current_cylinder = 0  # Start from 0 again
    return total_distance

def rearrange_requests_fcfs(initial_position, requests):
    return requests

def rearrange_requests_scan(initial_position, requests):
    requests.sort()
    requests.append(0)  # Add the starting cylinder to the end
    requests.insert(0, 4999)  # Add the ending cylinder to the beginning
    return requests

def rearrange_requests_cscan(initial_position, requests):
    requests.sort()
    return requests

def main(initial_position, file_name):
    with open(file_name, 'r') as file:
        requests = [int(line.strip()) for line in file]

    print("Task 1 - FCFS:", fcfs(initial_position, requests.copy()))
    print("Task 1 - SCAN:", scan(initial_position, requests.copy()))
    print("Task 1 - C-SCAN:", cscan(initial_position, requests.copy()))

    print("\nTask 2 - FCFS:", fcfs(initial_position, rearrange_requests_fcfs(initial_position, requests.copy())))
    print("Task 2 - SCAN:", scan(initial_position, rearrange_requests_scan(initial_position, requests.copy())))
    print("Task 2 - C-SCAN:", cscan(initial_position, rearrange_requests_cscan(initial_position, requests.copy())))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduler.py initial_position file_name")
    else:
        initial_position = int(sys.argv[1])
        file_name = sys.argv[2]
        main(initial_position, file_name)

from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    current_tools = tools.popleft()
    current_sub = substances.pop()
    current_value = current_sub * current_tools

    if current_value in challenges:
        challenges.remove(current_value)
    else:
        current_tools += 1
        tools.append(current_tools)
        current_sub -= 1
        if current_sub > 0:
            substances.append(current_sub)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x)for x in challenges)}")
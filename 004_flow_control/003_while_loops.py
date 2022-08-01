# Simple sample of a while loop
# Imagine you nee to walk somewhere and would like to count your steps.

distance_to_target = float(input('Please enter how many kilometers you need to walk: '))
current_position = 0

step = 0.5  # Lets assume than length of a step is 0.5 meeters
step_cnt = 0
distance_in_meters = distance_to_target * 1000  # Convert distance to meters

# while loop will continue doing everything under it when current position is less than target
while current_position < distance_in_meters:

    # simple if statement will print every 100 steps
    # if step % 100 == 0:
    #     print(int(step_cnt))
    print(step_cnt)
    current_position += step  # add step length to current position
    step_cnt += 1  # add step length to step. this will become counter

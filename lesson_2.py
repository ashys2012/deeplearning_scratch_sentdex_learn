#Lesson 2

input = [1.0, 2.0, 3.0, 4.2]

weight1 = [4.2, 3.8, -2.5, 1.0]
weight2 = [-1.2, 6.8, -2.5, 3.0]
weight3 = [1.2, 0.8, -2.5, 2.0]


bias1 = 3
bias2 = 6
bias3 = 2

output = [input[0]*weight1[0]+input[1]*weight1[1]+input[2]*weight1[2]+input[3]*weight1[3]+bias1,
          input[0]*weight2[0]+input[1]*weight2[1]+input[2]*weight2[2]+input[3]*weight2[3]+bias2,
          input[0]*weight3[0]+input[1]*weight3[1]+input[2]*weight3[2]+input[3]*weight3[3]+bias3
          ]

print(output)


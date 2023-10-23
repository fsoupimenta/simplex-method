# Simplex Method Application
This repository provides a practical solution to the [Knapsack Problem](#knapsack-problem) using Python and the simplex method. The Knapsack Problem is a well-known combinatorial optimization challenge often encountered in logistics and resource allocation scenarios. It involves selecting a combination of items from a set, each with its weight and value, to maximize the total value while adhering to a constraint, such as a maximum weight or volume.

## Knapsack Problem: 
### 1. Problem Context:
A large electronics company is relocating from Brazil to Portugal and needs to move its assets to the new facilities. The company has hired container shipments to transport furniture and equipment. After sending the shipments, there is some leftover space in the containers with a weight capacity of 500 kg and a volume of 830 m3. In this case, it would be beneficial to fill this space with items available in the company's inventory, as the entire inventory cannot be shipped.
### 2. Problem Data:
| Item | Unit | Weight (unit) | Volume (unit) | Quantity in Stock |
|------|------|---------------|---------------|-------------------|
| 1    | Static Actuator     | Box    | 0.7           | 4.5           | 10                |
| 2    | Rotational Actuator | Box    | 1.7           | 2.1           | 18                |
| 3    | Pneumatic Actuator  | Box    | 0.1           | 3.7           | 13                |
| 4    | Galvanized T-Base   | Package| 0.8           | 4.7           | 14                |
| 5    | Butterfly Valve     | Package| 0.9           | 1.4           | 16                |
| 6    | Slide Switch        | Package| 2.2           | 3.6           | 18                |
| 7    | Key Switch          | Package| 3.8           | 2.5           | 9                 |
| 8    | Inverter            | Box    | 3.6           | 2.4           | 12                |
| 9    | 7-Way Harness       | Box    | 2.2           | 4.9           | 15                |
| 10   | 4-Way Harness       | Box    | 2.8           | 2.8           | 11                |
| 11   | Double Switch       | Box    | 0.1           | 3.6           | 13                |
| 12   | Inverter Switch     | Box    | 1.4           | 3.6           | 10                |
| 13   | Ignition Switch     | Box    | 3.4           | 2.1           | 10                |
| 14   | Split Valve         | Package| 1.1           | 2.2           | 8                 |
| 15   | Monobloc Valve      | Package| 3.2           | 1.3           | 17                |
| 16   | Expansion Joint     | Box    | 2.7           | 2.1           | 18                |
| 17   | Galvanized X-Base   | Package| 3.9           | 3.1           | 9                 |
| 18   | Micro Router        | Box    | 1.3           | 1.1           | 13                |
| 19   | Micro Switch        | Box    | 1.6           | 3.1           | 9                 |
| 20   | 2-Axis Terminal     | Package| 1.6           | 1.2           | 8                 |
| 21   | 4-Axis Terminal     | Package| 0.5           | 2.3           | 10                |
| 22   | 6-Axis Terminal     | Package| 0.3           | 1.7           | 10                |
| 23   | Pressure Sensor     | Box    | 1.2           | 3.8           | 15                |
| 24   | Proximity Sensor    | Box    | 1.1           | 1.3           | 18                |
| 25   | Flexinity           | Package| 1.2           | 1.3           | 12                |
| 26   | Flexinity Mini      | Package| 3.6           | 4.3           | 9                 |
| 27   | Oscillator          | Box    | 0.8           | 2.3           | 10                |
| 28   | Timer               | Box    | 1.1           | 3.6           | 17                |
| 29   | Thermistor          | Box    | 3.6           | 2.6           | 18                |
| 30   | Slide Potentiometer | Box    | 2.2           | 3.2           | 11                |

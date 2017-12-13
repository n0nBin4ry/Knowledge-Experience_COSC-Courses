% matlab testing

format long
N = 100000000;

%prompt = 'Enter an integer N: ';
%N = input(prompt);

sum = 0;
tic
for i = 1:N
    sum = sum + i + i^2 + i^3;
end
toc

sum 

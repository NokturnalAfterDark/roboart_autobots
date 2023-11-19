% I, Daniel Andre, edit the code for one robot to follow coordinates that was click on
% figure widow the rest of the comment is showing who wrote the orginal
% code

% Initializing the agents to random positions with barrier certificates. 
% This script shows how to initialize robots to a particular point.
% Sean Wilson
% 07/2019
clear
clc
figure(1)

%Plot the boundaries for the area 
coordinatesX=[1.6,1.6,-1.6,-1.6,-1.6];
coordinatesY=[-1,1,1,-1,1];
plot(coordinatesX,coordinatesY);
[xi,yi] = getpts;
Nxiyi=length(xi);
initial_positions = [xi(1),yi(1),1]';
N = 1;

r = Robotarium('NumberOfRobots', N, 'ShowFigure', true, 'InitialConditions', initial_positions);

% Create a barrier certificate so that the robots don't collide
si_barrier_certificate = create_si_barrier_certificate();
si_to_uni_dynamics = create_si_to_uni_dynamics();
        

% We'll make the rotation error huge so that the initialization checker
% doesn't care about it
args = {'PositionError', 0.02, 'RotationError', 50};
init_checker = create_is_initialized(args{:});
controller = create_si_position_controller();

% Get initial location data for while loop condition.
x=r.get_poses();
r.step();
for p=2:1:Nxiyi
    k=[xi(p),yi(p),1]';
l(1,1)=[xi(1)];
l(2,1)=[yi(1)];

while(~init_checker(x, k))

    x = r.get_poses();
    dxi = controller(x(1:2, :), k(1:2, :));
    
    dxi = si_barrier_certificate(dxi, x(1:2, :));      
    dxu = si_to_uni_dynamics(dxi, x);

    r.set_velocities(1:N, dxu);
    r.step();
    l(1,p)=[x(1)];
    l(2,p)=[x(2)];
    
    
end
h = drawpolyline('Position',l');
end
% We can call this function to debug our experiment!  Fix all the errors
% before submitting to maximize the chance that your experiment runs
% successfully.
r.debug();


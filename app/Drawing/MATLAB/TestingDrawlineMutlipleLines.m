%This is a test of using multpies points in the drawcanvas function
clear
clc
%setting boundaries
figure(1)
coordinatesX=[1.6,1.6,-1.6,-1.6,-1.6];
coordinatesY=[-1,1,1,-1,1];
plot(coordinatesX,coordinatesY);
RGB="white-empty-canvas.jpg";
[xi,yi] = getpts;

%Setting up the canvas class
worldcoordinatesBoundaries=[1.6,-1.6,1.6,-1.6];
obj=canvas(worldcoordinatesBoundaries,RGB);

%extracting the 
for k=1:1:length(xi)
if (((2*k)-1)<=length(xi))&&(((2*k))<=length(xi))
x1(k)=xi((2*k)-1);
y1(k)=yi((2*k)-1);
x2(k)=xi((2*k));
y2(k)=yi((2*k));
end 

end 
pts1=[x1,y1];
pts2=[x2,y2];
for l=1:1:numel(pts1)

if (((2*l))<=numel(pts1))
pilXY=worldToPixel(obj,x1(l),y1(l));
plXY((2*l-1),1)=pilXY(1);
plXY((2*l-1),2)=pilXY(2);
pilXY2=worldToPixel(obj,x2(l),y2(l));
plXY(2*l,1)=pilXY2(1);
plXY(2*l,2)=pilXY2(2);
end 
end

pixelXY=plXY;


image=drawcanvasline(obj,pixelXY,1);

%note

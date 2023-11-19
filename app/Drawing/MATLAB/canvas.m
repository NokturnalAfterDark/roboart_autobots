classdef canvas
    properties
    pixelboundaries
    worldcoordinatesBoundaries
    imaged
    end
     methods
      function obj=canvas(worldcoordinatesBoundaries,imaged)
              obj.imaged=imread(imaged);
             obj.pixelboundaries=size(obj.imaged);
             obj.worldcoordinatesBoundaries=worldcoordinatesBoundaries;
   
      end
       function pixelXY=worldToPixel(obj,x,y)
                     pixelboundaries=obj.pixelboundaries;
                     Xrange=[-1.6,1.6]';
                     Yrange=[-1.6,1.6]';

                  

                if (x<=1.6)&&(x>=-1.6)&&(y<=1.6)&&(y>=-1.6)
                    pixelXY(1) = interp1(Xrange,[1,pixelboundaries(1)],x);
                    pixelXY(2) = interp1(Yrange,[1,pixelboundaries(2)],y);

                elseif (x<=1.6)&&(x>=-1.6)&&(y<=-1.6)
                    pixelXY(1) = interp1(Xrange,[1,pixelboundaries(1)],x);
                    pixelXY(2) = 1;

                 elseif (x<=1.6)&&(x>=-1.6)&&(y>=1.6)
                    pixelXY(1) = interp1(Xrange,[1,pixelboundaries(1)],x);
                    pixelXY(2) = pixelboundaries(2);  
                 elseif (y<=1.6)&&(y>=-1.6)&&(x>=1.6)
                    pixelXY(1) = pixelboundaries(1);
                    pixelXY(2) = interp1(Yrange,[1,pixelboundaries(2)],y);
                elseif (y<=1.6)&&(y>=-1.6)&&(x<=-1.6)
                    pixelXY(1) = 1; 
                    pixelXY(2) = interp1(Yrange,[1,pixelboundaries(2)],y);
                elseif (y>=1.6)&&(x>=1.6)
                    pixelXY(1) = pixelboundaries(1);
                    pixelXY(2) = pixelboundaries(2);
                 elseif (y>=1.6)&&(x<=-1.6)
                    pixelXY(1) = 1;
                    pixelXY(2) = pixelboundaries(2);
                 elseif (y<=-1.6)&&(x>=1.6)
                    pixelXY(1) = pixelboundaries(1);
                    pixelXY(2) = 1;
                 elseif (y<=-1.6)&&(x<=-1.6)
                    pixelXY(1) = 1;
                    pixelXY(2) = 1;                



                end
           
       end
       function image=drawcanvasline(obj,pts1,color)
               if color==1
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["black"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==2
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["white"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==3
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["yellow"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==4
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["magenta"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==5
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["green"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==6
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["cyan"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==7
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["red"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==8
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["blue"],Opacity=0.7);
               imshow(image);
               axis xy

               elseif color==9
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["green"],Opacity=0.7);
               imshow(image);
               axis xy

               else
               image = insertShape(obj.imaged,"line",{[pts1]},...
               Color=["black"],Opacity=0.7);
               imshow(image);
               axis xy

               end 
           end
           
     end
end
 

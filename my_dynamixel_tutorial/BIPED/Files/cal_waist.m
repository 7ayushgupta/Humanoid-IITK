function waist=cal_waist(
        %waist--------------------------------------------------
        waist(:,1) = [xc;y;z+25;1];
        waist(:,2) = [xc;y;z;1];
        waist(:,3) = rleg(:,1);
        waist(:,4) = lleg(:,1);

%variables --------------
% bu is the position of stance leg ankle before taking the lift.

%bu=-5.289560701428371;
Rh=zeros(4 , 6);
lh=zeros(4 , 6);
rha =zeros(4,1);
lha =zeros(4,1);
waist=zeros(4,4);
rleg=zeros(4,8);
lleg=zeros(4,8);
l0=zeros(7,1);
r0=zeros(7,1);
rfoot=zeros(4,8);
lfoot=zeros(4,8);
xcom=zeros(4,1);
z=42.6370;
h=z;
y=0;
t=0;
t0 = [1 0 0 0;0 1 0 0; 0 0 1 0;0 0 0 1];
rf = [1 0 0 0;0 0 1 0; 0 -1 0 0;0 0 0 1];
wa1=0.001;
wa2=0.001;
sl=16;
z__1=zeros(4,1);
z_1=zeros(4,1);

load('Angles');

    %###############################################################
    %######    right leg as swing leg                          #####
    %###############################################################
while 1
    %DSP phase 1 --------------------------------------------------------
    x=0;
    l=x*10;l=1; 
    k=l+6*10;
    for t=l:k
        
        x=(t)/10;x=x*sl/16;
        y=-(3*t)/60;
        
        %left hand and right hand angles-----------------------------------
        lha(3)= 10*pi/180 - x*20*pi/(16*180);
        lha(4)= 5*pi/180+(x/16)*(pi/180)*5;
        rha(3)=x/16*(20*pi/180)-10*pi/180;
        rha(4)=-x/16*(5*pi/180)+10*pi/180;
        
        l0=la(:,t);
        r0=ra(:,t);

        %position calculation ---------------------------------------------
        rf(:,4)=rleg(:,7);
        [rleg, rfoot, xcom] = calc_pos(r0,rf,-1);
        t0(:,4)=xcom;
        [lleg, lfoot] = calc_lpos(l0,t0);
        lh=cal_lh(lha,t0);
        Rh=cal_rh(rha,t0);
        waist(:,1) = xcom;
        waist(3,1) = waist(3,1) + 25;
        waist(:,2) = xcom;
        waist(:,3) = rleg(:,1);
        waist(:,4) = lleg(:,1);
        zmp = waist(:,2);
        zmp(3)=0;
        
        [z__1, z_1] = plot_final(Rh,lh,rleg,lleg,waist,zmp,rfoot,lfoot,z__1,z_1);
        pause(wa1);
        
    end
    
    bur = mod(lleg(:,5),8);
    bu = bur(1);
    %SSP phase 1 --------------------------------------------------------
    l=x*10;
    k=l+6*10;
    for t=l+1:k
        x=(t)/10;x=x*sl/16;
        
        %left hand and right hand angles --------------------------------
        lha(3)= 10*pi/180 - x*20*pi/(16*180);
        lha(4)= 5*pi/180+(x/16)*(pi/180)*5;
        rha(3)=x/16*(20*pi/180)-10*pi/180;
        rha(4)=-x/16*(5*pi/180)+10*pi/180;
        
        l0=la(:,t);
        r0=ra(:,t);
        
        %position calculation ---------------------------------------------
        rf(:,4)=rleg(:,7);
        [rleg, rfoot, xcom] = calc_pos(r0,rf,-1);
        t0(:,4)=xcom;
        [lleg, lfoot] = calc_lpos(l0,t0);
        lh=cal_lh(lha,t0);
        Rh=cal_rh(rha,t0);
        waist(:,1) = xcom;
        waist(3,1) = waist(3,1) + 25;
        waist(:,2) = xcom;
        waist(:,3) = rleg(:,1);
        waist(:,4) = lleg(:,1);
        zmp = waist(:,2);
        zmp(3)=0;
        
        [z__1, z_1] = plot_final(Rh,lh,rleg,lleg,waist,zmp,rfoot,lfoot,z__1,z_1);
        pause(wa2);
    end

    %DSP phase 2 ---------------------------------------------
    l=x*10;
    k=l+4*10;
    for t=l+1:k
        x=(t)/10;x=x*sl/16;
        y=(3*(t-120))/40-3;
        
        
         %left hand and right hand angles
        lha(3)= 10*pi/180 - x*20*pi/(16*180);
        lha(4)= 5*pi/180+(x/16)*(pi/180)*5;
        rha(3)=x/16*(20*pi/180)-10*pi/180;
        rha(4)=-x/16*(5*pi/180)+10*pi/180;
        
        l0=la(:,t);
        r0=ra(:,t);
        
        %position calculation ---------------------------------------------
        rf(:,4)=rleg(:,7);
        [rleg, rfoot, xcom] = calc_pos(r0,rf,-1);
        t0(:,4)=xcom;
        [lleg, lfoot] = calc_lpos(l0,t0);
        lh=cal_lh(lha,t0);
        Rh=cal_rh(rha,t0);
        waist(:,1) = xcom;
        waist(3,1) = waist(3,1) + 25;
        waist(:,2) = xcom;
        waist(:,3) = rleg(:,1);
        waist(:,4) = lleg(:,1);
        zmp = waist(:,2);
        zmp(3)=0;
        
        [z__1, z_1] = plot_final(Rh,lh,rleg,lleg,waist,zmp,rfoot,lfoot,z__1,z_1);
        pause(wa1);
    end

    %###############################################################
    %######    left leg as swing leg                         ######
    %###############################################################

    %DSP phase 1 --------------------------------------------------------
    x=0;
    l=x*10;l=1;
    k=l+6*10;
    for t=l:k
        x=(t)/10;x=x*sl/16;
        y=(3*(t))/60;
        
        
        %-------------------hand angles---------------
        lha(3)=x/16*(20*pi/180)-10*pi/180;
        lha(4)=-x/16*(5*pi/180)+10*pi/180;
        rha(3)= 10*pi/180 - x*20*pi/(16*180);
        rha(4)= 5*pi/180+(x/16)*(5*pi/180);
        
        l0=la(:,t+160);
        r0=ra(:,t+160);
        
        %position calculation ---------------------------------------------
        rf(:,4)=lleg(:,7);
        [lleg, lfoot, xcom] = calc_pos(l0,rf,1);
        t0(:,4)=xcom;
        [rleg, rfoot] = calc_rpos(r0,t0);
        
        lh=cal_lh(lha,t0);
        Rh=cal_rh(rha,t0);
        waist(:,1) = xcom;
        waist(3,1) = waist(3,1) + 25;
        waist(:,2) = xcom;
        waist(:,3) = rleg(:,1);
        waist(:,4) = lleg(:,1);
        zmp = waist(:,2);
        zmp(3)=0;
        
        [z__1, z_1] = plot_final(Rh,lh,rleg,lleg,waist,zmp,rfoot,lfoot,z__1,z_1);
        pause(wa1);
    end
    
    bur = mod(rleg(:,5),8);
    bu = bur(1);
    %SSP phase 1 --------------------------------------------------------
    l=x*10;
    k=l+6*10;
    for t=l+1:k
        x=(t)/10;x=x*sl/16;
        
        
       % -----------hand angles-----------
        lha(3)=x/16*(20*pi/180)-10*pi/180;
        lha(4)=-x/16*(5*pi/180)+10*pi/180;
        rha(3)= 10*pi/180 - x*20*pi/(16*180);
        rha(4)= 5*pi/180+(x/16)*(5*pi/180);
        
        l0=la(:,t+160);
        r0=ra(:,t+160);
        
        %position calculation ---------------------------------------------
        rf(:,4)=lleg(:,7);
        [lleg, lfoot, xcom] = calc_pos(l0,rf,1);
        t0(:,4)=xcom;
        [rleg, rfoot] = calc_rpos(r0,t0);
        lh=cal_lh(lha,t0);
        Rh=cal_rh(rha,t0);
        waist(:,1) = xcom;
        waist(3,1) = waist(3,1) + 25;
        waist(:,2) = xcom;
        waist(:,3) = rleg(:,1);
        waist(:,4) = lleg(:,1);
        zmp = waist(:,2);
        zmp(3)=0;
        
        [z__1, z_1] = plot_final(Rh,lh,rleg,lleg,waist,zmp,rfoot,lfoot,z__1,z_1);
        pause(wa2);
    end

    %DSP phase 2 ---------------------------------------------
    l=x*10;
    k=l+4*10;
    for t=l+1:k
        x=t/10;x=x*sl/16;
        y=-((3*(t-120))/40-3);
        
        
        %----------hand angles----------
        lha(3)=x/16*(20*pi/180)-10*pi/180;
        lha(4)=-x/16*(5*pi/180)+10*pi/180;
        rha(3)= 10*pi/180 - x*20*pi/(16*180);
        rha(4)= 5*pi/180+(x/16)*(5*pi/180);
        
        l0=la(:,t+160);
        r0=ra(:,t+160);
        
        
        %position calculation ---------------------------------------------
        rf(:,4)=lleg(:,7);
        [lleg, lfoot, xcom] = calc_pos(l0,rf,1);
        t0(:,4)=xcom;
        [rleg, rfoot] = calc_rpos(r0,t0);
        lh=cal_lh(lha,t0);
        Rh=cal_rh(rha,t0);
        waist(:,1) = xcom;
        waist(3,1) = waist(3,1) + 25;
        waist(:,2) = xcom;
        waist(:,3) = rleg(:,1);
        waist(:,4) = lleg(:,1);
        zmp = waist(:,2);
        zmp(3)=0;
        
        [z__1, z_1] = plot_final(Rh,lh,rleg,lleg,waist,zmp,rfoot,lfoot,z__1,z_1);
        pause(wa1);
    end
    end
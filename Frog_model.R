#set working directory
setwd('C:/Users/smpra/Documents/Research/Frog')
getwd()

#Read in data
sppe_csv <- read.csv('C:/Users/smpra/Documents/Research/Frog/2012_sppe_alldata.csv')
str(sppe_csv)
View(sppe_csv)
y <- sppe_csv[,2:4]
y

#site covs
site_covs <- sppe_csv[,20:83]
site_covs

sppe_csv$windsp1s <- scale(sppe_csv$windsp1)
sppe_csv$windsp2s <- scale(sppe_csv$windsp2)
sppe_csv$windsp3s <- scale(sppe_csv$windsp3)

sppe_csv$dabovrain1s <- scale(sppe_csv$dabovrain1)
sppe_csv$dabovrain2s <- scale(sppe_csv$dabovrain2)
sppe_csv$dabovrain3s <- scale(sppe_csv$dabovrain3)

sppe_csv$drain1s <- scale(sppe_csv$drain1)
sppe_csv$drain2s <- scale(sppe_csv$drain2)
sppe_csv$drain3s <- scale(sppe_csv$drain3)

sppe_csv$tsunset1s <- scale(sppe_csv$tsunset1)
sppe_csv$tsunset2s <- scale(sppe_csv$tsunset2)
sppe_csv$tsunset3s <- scale(sppe_csv$tsunset3)

sppe_csv$temp1s <- scale(sppe_csv$temp1)
sppe_csv$temp2s <- scale(sppe_csv$temp2)
sppe_csv$temp3s <- scale(sppe_csv$temp3)

#Obs covs
obs_covs_scaled <- list(windsp=sppe_csv[,c("windsp1s", "windsp2s", "windsp3s")], daar=sppe_csv[,c("dabovrain1s", "dabovrain2s", "dabovrain3s")], daysrain=sppe_csv[,c("drain1s", "drain2s", "drain3s")], timesun=sppe_csv[,c("tsunset1s", "tsunset2s", "tsunset3s")], temp=sppe_csv[,c("temp1s", "temp2s", "temp3s")])
obs_covs_scaled

library(unmarked)
sppe_2011 <- unmarkedFrameOccuMS(y=y, siteCovs=site_covs, obsCovs=obs_covs_scaled)

sppe_2011                     # look at data
summary(sppe_2011)            # summarize      
sppe_2011@numStates           # check number of occupancy states detected

#obs covs
null_det <- c('~1','~1','~1')

tsunset_det <- c('~timesun','~timesun','~timesun')
temp_det <- c('~temp','~temp','~temp')
tsunsetwind_det <-  c('~timesun+windsp', '~timesun+windsp', '~timesun+windsp')
tsunset_temp_det <- c('~timesun+temp', '~timesun+temp', '~timesun+temp')
tsunset_tempwind_det <- c('~timesun+temp+windsp', '~timesun+temp+windsp', '~timesun+temp+windsp')
wind_det <- c('~windsp','~windsp','~windsp')
dabovrain_det <- c('~daar','~daar','~daar')
drain_det <- c('~daysrain','~daysrain','~daysrain')
null_tsunset_temp <- c('~1', '~timesun+temp', '~timesun+temp')
nul_tsunset_temp <- c('~timesun+temp', '~1', '~1')

#sitecovs
null_state <- c('~1','~1')

percan_state <- c('~PerCanopy','~PerCanopy')
pondarea_state <- c('~PondArea','~PondArea')
perim_state <- c('~Perimeter','~Perimeter')
wet_state <- c('~Wetland','~Wetland')
prop_forest_state <- c('~For_500','~For_500')
percan_forest_state <- c('~For_500+PerCanopy','~For_500+PerCanopy')


#Modeling
null_fit <- occuMS(null_det, null_state, data=sppe_2011, parameterization="multinomial")
null_fit

#detection
time_fit <- occuMS(tsunset_det, null_state, data=sppe_2011, parameterization="multinomial")
time_fit

time_wind_fit <- occuMS(tsunsetwind_det, null_state, data=sppe_2011, parameterization="multinomial")
time_wind_fit

temp_fit <- occuMS(temp_det, null_state, data=sppe_2011, parameterization="multinomial")
temp_fit

temp_forfit <- occuMS(temp_det, prop_forest_state, data=sppe_2011, parameterization="multinomial")
temp_forfit

temp_tsunset_fit <- occuMS(tsunset_temp_det, null_state, data=sppe_2011, parameterization="multinomial")
temp_tsunset_fit

nulltemp_tsunset_fit <- occuMS(null_tsunset_temp, null_state, data=sppe_2011, parameterization="multinomial")
nulltemp_tsunset_fit

nultemp_tsunset_fit <- occuMS(nul_tsunset_temp, null_state, data=sppe_2011, parameterization="multinomial")
nultemp_tsunset_fit

temp_wind_time_fit <- occuMS(tsunset_tempwind_det, null_state, data=sppe_2011, parameterization="multinomial")
temp_wind_time_fit

wind_fit <- occuMS(wind_det, null_state, data=sppe_2011, parameterization="multinomial")
wind_fit

drain_fit <- occuMS(drain_det, null_state, data=sppe_2011, parameterization="multinomial")
drain_fit

dabovrain_fit <- occuMS(dabovrain_det, null_state, data=sppe_2011, parameterization="multinomial")
dabovrain_fit

#occupancy
temp_tsunsetpercan_fit <- occuMS(tsunset_temp_det, percan_state, data=sppe_2011, parameterization="multinomial")
temp_tsunsetpercan_fit

temp_tsunsetpond_fit <- occuMS(tsunset_temp_det, pondarea_state, data=sppe_2011, parameterization="multinomial")
temp_tsunsetpond_fit

temp_tsunsetfor_fit <- occuMS(tsunset_temp_det, prop_forest_state, data=sppe_2011, parameterization="multinomial")
temp_tsunsetfor_fit

time_windforest_fit <- occuMS(tsunsetwind_det, prop_forest_state, data=sppe_2011, parameterization="multinomial")
time_windforest_fit

time_windpond_fit <- occuMS(tsunsetwind_det, pondarea_state, data=sppe_2011, parameterization="multinomial")
time_windpond_fit

time_windpercan_fit <- occuMS(tsunsetwind_det, percan_state, data=sppe_2011, parameterization="multinomial")
time_windpercan_fit

time_windwetland_fit <- occuMS(tsunsetwind_det, wet_state, data=sppe_2011, parameterization="multinomial")
time_windwetland_fit

time_windpercan_fit <- occuMS(tsunsetwind_det, percan_forest_state, data=sppe_2011, parameterization="multinomial")
time_windpercan_fit

twind_percanfor_fit <- occuMS(tsunsetwind_det, percan_forest_state, data=sppe_2011, parameterization="multinomial")
twind_percanfor_fit

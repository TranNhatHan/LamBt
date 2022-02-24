Wingcrd <- c(59, 55, 53.5, 55, 52.5, 57.5, 53, 55)
Tarsus <- c(22.3, 19.7, 20.8, 20.3, 20.8, 21.5, 20.6,21.5)
Head <- c(31.2, 30.4, 30.6, 30.3, 30.3, 30.8, 32.5,NA)
Wt <- c(9.5, 13.8, 14.8, 15.2, 15.5, 15.6, 15.6,15.7)
BirdData <- c(Wingcrd, Tarsus, Head, Wt)
Id <- rep(1 : 4, each = 8)
VarNames <- c("Wingcrd", "Tarsus", "Head", "Wt")
Id2 <- rep(VarNames, each = 8)
Z <- cbind(Wingcrd, Tarsus, Head, Wt)
dim(Z)
Z2 <- rbind(Wingcrd, Tarsus, Head, Wt)
Dmat2 <- as.matrix(cbind(Wingcrd, Tarsus, Head, Wt))
Dfrm <- data.frame(WC = Wingcrd,
TS = Tarsus,
HD = Head,
W = Wt)
Dfrm <- data.frame(WC = Wingcrd,
TS = Tarsus,
HD = Head,
W = Wt,
Wsq = sqrt(Wt))
Dfrm$W
x1 <- c(1, 2, 3)
x2 <- c("a", "b", "c", "d")
x3 <- 3
x4 <- matrix(nrow = 2, ncol = 2)
x4[, 1] <- c(1, 2)
x4[, 2] <- c( 3, 4)
Y <- list(x1 = x1, x2 = x2, x3 = x3, x4 = x4)
M <- lm(WC ~ Wt, data = Dfrm)
names(M)

library(RODBC)
setwd("C:/RBook")
channel1 <- odbcConnectAccess(file =
"MyDb.mdb", uid = "", pwd = "")
Channel1 <- odbcConnect("MyDb.mdb")
MyData <- sqlFetch(channel1, "MyTable")
MyData


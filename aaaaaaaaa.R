data=read.table("tache5.5_frequences.csv", sep=",", header=T)
grp = read.table("grp.csv", sep=",", header=T)
aa= FreqAA$AA

perg = c()

for (i in 1:length(data$acide_amine) ){
  
  sur = grp$frequence_surface[i]/sum(grp$frequence_surface)
  int = grp$frequence_interface[i]/sum(grp$frequence_interface)
  perg = append(perg,log2(sur/int))
  
}

barplot(per, names.arg = aa, main="diagramme à barres des propensions relatives pour chaque AA")

points(1:20,perg)

dataFreqAAdi = data.frame(acide_amine=unique(freqAASurfaceInterfaceDi$acide_amine))

for (i in 1:20){
  dataFreqAAdi$interface1[i] = sum(freqAASurfaceInterfaceDi$frequence_interface[
    which(freqAASurfaceInterfaceDi$acide_amine ==
                 dataFreqAAdi$acide_amine[i])])
  
}

dataFreqAAtri = data.frame(acide_amine=unique(freqAASurfaceInterfaceTri$acide_amine))

for (i in 1:20){
  dataFreqAAtri$surface[i] = sum(freqAASurfaceInterfaceTri$frequence_surface[
    which(freqAASurfaceInterfaceTri$acide_amine ==
            dataFreqAAtri$acide_amine[i])])
  
}


# bind the two dataframes together by row and aggregate
res <- aggregate(cbind(,y,z) ~ rn, rbind(df1,df2), sum)
# or (thx to @alistaire for reminding me):
res <- aggregate(. ~ rn, rbind(df1,df2), sum)

# assign the rownames again
rownames(res) <- res$rn

# get rid of the 'rn' column
res <- res[, -1]

FreqAA %>%
  pivot_longer(c(`surface`,`interface1`,"interface2"))  %>%
  ggplot(aes(x=AA, y=value, fill=name, group=name)) +
  geom_col(position = position_dodge())
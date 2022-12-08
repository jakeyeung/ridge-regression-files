# 2015-08-05
# Run MARA on DHS signal 

source('/Home/jyeung/projects/ridge-regression/ridgeInR.R')

args <- commandArgs(trailingOnly = TRUE)
exp <- args[1]
site <- args[2]

print("Loading files")
E = read.table(exp)
N = read.table(site)
print("Loaded matrix")

print(E[1:5, 1:5])
print(N[1:5, 1:5])

E = log2(as.matrix(E) + 0.0001)

E = as.matrix(E)
N = as.matrix(N)

# center the rows
E = t(scale(t(E), center = TRUE, scale = FALSE))

opt = optimize.lambda(N, E)
r = ridge.regression(N, E, opt$lambda.opt)
top20 = sort(r$combined.Zscore, decreasing=TRUE)[1:30]

save(r, E, N, exp, site, file = "r.Robj")

for(n in names(r$combined.Zscore)){
      write(paste(n, r$combined.Zscore[n], sep='\t'), "Zscores", append=TRUE)
}

write(paste(c('', colnames(E)), collapse = "\t"), "Activities", append=TRUE)
for(n in names(r$combined.Zscore)){
      x = paste( r$Ahat[n, ], collapse="\t")
      write(paste(n, x, sep='\t'), "Activities", append=TRUE)
}

write(paste(c('', colnames(E)), collapse = "\t"), "StandardError", append=TRUE)
for(n in names(r$combined.Zscore)){
      x = paste( r$AhatSE[n, ], collapse="\t")
      write(paste(n, x, sep='\t'), "StandardError", append=TRUE)
}

write(toString(mean(r$fov)), 'FOV')
write(toString(opt$lambda.opt), "Lambda")



import java.util.Arrays;

public class Individual implements Comparable{
    private int noGenes;
    private int fitnessScore;
    private Gene[] genes;

    public int getNoGenes() {
        return noGenes;
    }

    public int getFitnessScore() {
        return fitnessScore;
    }

    public Gene[] getGenes() {
        return genes;
    }

    public Individual(int _noGenes) {
        this.noGenes = _noGenes;
        this.genes = new Gene[_noGenes];
        initGenes();
    }

    public Individual(Individual _copy) {
        this.fitnessScore = _copy.getFitnessScore();
        this.genes = _copy.getGenes();
        this.noGenes = _copy.getNoGenes();
    }
    public Individual(Individual p1, Individual p2, int crossPoint) {
        Gene[] temp1 = Arrays.copyOfRange(p1.getGenes(), 0, crossPoint);
        // Gene[] temp2 = Arrays.copyOfRange(p2.getGenes(), crossPoint, p2.getGenes().length);
        Gene[] temp2 = p2.getGenes();
        for (int i = crossPoint; i < p2.getGenes().length; i++) {
            temp1[i] = temp2[i];
        }
        this.genes = temp1;
        this.noGenes = temp1.length;
    }

    public void initGenes() {
        for(int i = 0; i < this.noGenes; i++)
            this.genes[i] = new Gene();
    }

    public void computeFitness() {
        int res = 0;
        for (int i = 0; i < this.noGenes; i++) {
            res += 2^i * this.genes[i].getValue();
        }
        this.fitnessScore = res;
    }

    @Override
    public String toString() {
        String res = "";
        for(int i = 0; i < this.noGenes; i++)
            res += this.genes[i];
        return res;
    }

    @Override
    public int compareTo(Object o) {
        this.computeFitness();
        Individual temp = new Individual((Individual)o);
        if(this.fitnessScore > temp.getFitnessScore()) {
            return 1;
        }
        else if (this.fitnessScore < temp.getFitnessScore()) {
            return -1;
        }
        else {
            return 0;
        }
    }
}

import java.util.Arrays;
import java.util.Random;

public class Population {
    private int size;
    private int sizeOfPoolGen;
    Individual[] population;

    public Population(int _size, int _sizeOfPoolGen) {
        this.size = _size;
        this.sizeOfPoolGen = _sizeOfPoolGen;
        this.population = new Individual[_size];
        initEmptyPop();
    }

    public void initEmptyPop() {
        for(int i = 0; i < this.size; i++) {
            this.population[i] = new Individual(this.sizeOfPoolGen);
        }
    }

    public Individual roulette() {
        Arrays.sort(this.population);
        int sum = 0;
        for (int i = 0 ; i < this.population.length ; i++) {
            this.population[i].computeFitness();
            sum += this.population[i].getFitnessScore();
        }
        int[] temp = new int[sum];
        int sumLoop = 0;
        for (int i = 0 ; i < this.population.length ; i++) {
            for (int j = 0 ; j < this.population[i].getFitnessScore() ; j++) {
                temp[sumLoop] = this.population[i].getFitnessScore();
                sumLoop++;
            }
        }
        int index = new Random().nextInt(sum);
        int intChoice = temp[index];
        int indexRes = -1;
        for (int i = 0 ; i < this.population.length ; i++) {
            if(this.population[i].getFitnessScore() == intChoice)
            {
                indexRes = i;
            }
        }
        return this.population[indexRes];
    }

    public void reproduction() {
        Individual parent1 = this.roulette();
        Individual parent2 = this.roulette();
        while (parent1.getFitnessScore() == parent2.getFitnessScore()) {
            parent2 = this.roulette();
        }
        System.out.println(parent1 + " | " + parent2);
    }

    @Override
    public String toString() {
        String res = "";
        for(int i=0; i < this.size; i++)
            res += "Individu "+ i +": "+ this.population[i] + "\n";
        return res;
    }
}

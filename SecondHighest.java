import java.util.*;

class SecondHighest
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the size of array : ");
		int size=sc.nextInt();
		int[] array=new int[size];
		for(int i=0;i<size;i++)
		{
			System.out.println("Enter the element of array["+i+"]");
			array[i]=sc.nextInt();
		}
		System.out.println("Array is : "+Arrays.toString(array));
		//Arrays.sort(array);
		//System.out.println("Second highest element of array is : "+array[size-2]);
		for(int i=0;i<size;i++)
		{
			for(int j=i+1;j<size;j++)
			{
				if(array[i]>array[j])
				{
					int temp=array[i];
					array[i]=array[j];
					array[j]=temp;
				}
			}
		}
		System.out.println("Second highest element of array is : "+array[size-2]);
	}
}
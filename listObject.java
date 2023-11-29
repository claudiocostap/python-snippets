import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.ObjectListing;
import com.amazonaws.services.s3.model.S3ObjectSummary;

public class ListS3Objects {

    public static void main(String[] args) {
        // Defina as credenciais da AWS
        String accessKey = "SEU_ACCESS_KEY";
        String secretKey = "SEU_SECRET_KEY";

        // Defina a região
        String region = "us-east-1"; // Substitua pela sua região

        // Defina o nome do bucket
        String bucketName = "SEU_BUCKET_NAME";

        // Crie o cliente AmazonS3
        AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                .withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("https://s3." + region + ".amazonaws.com", region))
                .withCredentials(new AWSStaticCredentialsProvider(new BasicAWSCredentials(accessKey, secretKey)))
                .build();

        // Liste os objetos no bucket
        listObjects(s3Client, bucketName);
    }

    private static void listObjects(AmazonS3 s3Client, String bucketName) {
        ObjectListing objectListing = s3Client.listObjects(bucketName);

        for (S3ObjectSummary objectSummary : objectListing.getObjectSummaries()) {
            System.out.println("Nome do objeto: " + objectSummary.getKey());
            System.out.println("Tamanho: " + objectSummary.getSize());
            System.out.println("Última modificação: " + objectSummary.getLastModified());
            System.out.println("---");
        }
    }
}

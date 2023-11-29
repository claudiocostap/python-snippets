import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.HeadObjectRequest;
import software.amazon.awssdk.services.s3.model.HeadObjectResponse;

public class GetS3ObjectMetadata {

    public static void main(String[] args) {
        // Defina as credenciais da AWS
        String accessKey = "SEU_ACCESS_KEY";
        String secretKey = "SEU_SECRET_KEY";

        // Defina o nome do bucket e o caminho do objeto
        String bucketName = "SEU_BUCKET_NAME";
        String objectKey = "SEU_OBJECT_KEY";

        // Crie o cliente S3
        S3Client s3Client = S3Client.builder()
                .region(Region.US_EAST_1) // Substitua pela sua região
                .credentialsProvider(() -> AwsBasicCredentials.create(accessKey, secretKey))
                .build();

        // Obtenha os metadados do objeto
        getObjectMetadata(s3Client, bucketName, objectKey);
    }

    private static void getObjectMetadata(S3Client s3Client, String bucketName, String objectKey) {
        HeadObjectRequest headObjectRequest = HeadObjectRequest.builder()
                .bucket(bucketName)
                .key(objectKey)
                .build();

        try {
            HeadObjectResponse headObjectResponse = s3Client.headObject(headObjectRequest);

            System.out.println("Metadados do objeto:");
            System.out.println("Nome do objeto: " + objectKey);
            System.out.println("Tamanho: " + headObjectResponse.contentLength());
            System.out.println("Tipo de conteúdo: " + headObjectResponse.contentType());
            System.out.println("Última modificação: " + headObjectResponse.lastModified());
        } catch (Exception e) {
            System.err.println("Erro ao obter metadados do objeto: " + e.getMessage());
        }
    }
}
